import requests
import os
from dotenv import load_dotenv
from google.transit import gtfs_realtime_pb2
from datetime import datetime
import time

load_dotenv()
API_ENDPOINT = "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-nqrw"
STOP_ID = os.environ["STOP_ID"]
feed = gtfs_realtime_pb2.FeedMessage()
DATA_FILE_PATH = "/home/sophiashovkovy/datafile.txt"

MAX_RETRY_ATTEMPTS = 3


def main():
    minutes_remaining = get_train_schedule()
    if minutes_remaining is not None:
        with open(DATA_FILE_PATH, "w") as f:
            f.write(str(minutes_remaining))


def get_train_schedule():
    retry_attempt = 0
    while retry_attempt < MAX_RETRY_ATTEMPTS:
        try:
            response = requests.get(
                API_ENDPOINT, headers={"x-api-key": os.environ["MTA_API_KEY"]}
            )
            response.raise_for_status()  # Raise an exception for HTTP errors
            feed_json = feed.FromString(response.content)

            stop_time_update_arrivals = [
                stop_time_update
                for entity in feed_json.entity
                for stop_time_update in entity.trip_update.stop_time_update
                if stop_time_update.stop_id == STOP_ID
            ]

            # Sort the list from soonest to latest
            sorted_arrivals = sorted(
                stop_time_update_arrivals, key=lambda x: x.arrival.time
            )
            minutes_remaining = calculate_minutes_until_next_arrival(sorted_arrivals)

            response.close()
            # print(f"{minutes_remaining} MIN")
            return minutes_remaining
        except Exception as e:
            print(f"An error occurred: {str(e)}")

            retry_attempt += 1
            if retry_attempt < MAX_RETRY_ATTEMPTS:
                time.sleep(10)
            else:
                print(f"Failed after max retry attempts.")
                break

    return None


def calculate_minutes_until_next_arrival(sorted_arrivals):
    current_timestamp = datetime.now().timestamp()
    arrival_timestamp = sorted_arrivals[0].arrival.time
    minutes_until_arrival = max(0, round((arrival_timestamp - current_timestamp) / 60))

    if minutes_until_arrival < 2 and len(sorted_arrivals) > 1:
        arrival_timestamp = sorted_arrivals[1].arrival.time
        minutes_until_arrival = max(
            0, round((arrival_timestamp - current_timestamp) / 60)
        )

    return minutes_until_arrival


if __name__ == "__main__":
    main()
