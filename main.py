import requests
import os
from dotenv import load_dotenv
from google.transit import gtfs_realtime_pb2

# import urllib
# from luma.led_matrix.device import max7219
# from luma.core.interface.serial import spi, noop
# from time import sleep

load_dotenv()
API_ENDPOINT = "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-nqrw"
feed = gtfs_realtime_pb2.FeedMessage()


def main():
    get_train_schedule()
    # minutes_remaining = get_train_schedule()
    # display_minutes(minutes_remaining)


def get_train_schedule():
    response = requests.get(
        API_ENDPOINT, headers={"x-api-key": os.environ["MTA_API_KEY"]}
    )
    print(response.text)
    minutes_remaining = 10  # Example value, replace this with your logic
    return minutes_remaining


# def display_minutes(minutes):
#     serial = spi(port=0, device=0, gpio=noop())
#     device = max7219(serial, cascaded=1, block_orientation=-90)
#     device.contrast(10)
#     device.show_message(
#         f"Next Q train: {minutes} min", fill="white", font=None, scroll_delay=0.05
#     )


if __name__ == "__main__":
    main()
