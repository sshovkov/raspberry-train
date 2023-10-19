import requests
import os
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.legacy import text
from luma.core.legacy.font import proportional, LCD_FONT
from luma.core.render import canvas
from dotenv import load_dotenv
from google.transit import gtfs_realtime_pb2
from datetime import datetime
import time

load_dotenv()
API_ENDPOINT = "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-nqrw"
STOP_ID = os.environ["STOP_ID"]
feed = gtfs_realtime_pb2.FeedMessage()


def main():
    while True:
        minutes_remaining = get_train_schedule()
        display_minutes(minutes_remaining)
        time.sleep(60)


def get_train_schedule():
    response = requests.get(
        API_ENDPOINT, headers={"x-api-key": os.environ["MTA_API_KEY"]}
    )
    feed_json = feed.FromString(response.content)

    stop_time_update_arrivals = [
        stop_time_update
        for entity in feed_json.entity
        for stop_time_update in entity.trip_update.stop_time_update
        if stop_time_update.stop_id == STOP_ID
    ]

    # Sort the list from soonest to latest
    sorted_arrivals = sorted(stop_time_update_arrivals, key=lambda x: x.arrival.time)
    minutes_remaining = calculate_minutes_until_next_arrival(sorted_arrivals)

    # print(f"{minutes_remaining} MIN")
    return minutes_remaining


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


def display_minutes(minutes):
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(
        serial,
        cascaded=4,
        block_orientation=90,
        rotate=0,
        blocks_arranged_in_reverse_order=True,
    )

    message = f"{minutes} MIN"

    with canvas(device) as draw:
        text(draw, (3, 1), message, fill="white", font=proportional(LCD_FONT))


if __name__ == "__main__":
    main()
