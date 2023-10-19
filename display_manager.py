from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.legacy import text
from luma.core.legacy.font import proportional, LCD_FONT
from luma.core.render import canvas
import time

serial = spi(port=0, device=0, gpio=noop())
device = max7219(
    serial,
    cascaded=4,
    block_orientation=90,
    rotate=0,
    blocks_arranged_in_reverse_order=True,
)

DATA_FILE_PATH = "/home/sophiashovkovy/datafile.txt"


def main():
    while True:
        try:
            with open(DATA_FILE_PATH, "r") as f:
                minutes_remaining = int(f.read().strip())
            display_minutes(minutes_remaining)
            time.sleep(58)
        except Exception as e:
            print(f"Error in display_manager: {e}")
            time.sleep(10)


def display_minutes(minutes):
    message = f"{minutes} MIN"
    with canvas(device) as draw:
        text(draw, (3, 1), message, fill="white", font=proportional(LCD_FONT))
