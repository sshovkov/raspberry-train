# Using a Raspberry Pi to display Q-train arrival time

## Materials

- Raspberry Pi Zero W
  - I chose this one because was affordable, included built-in Wi-Fi, and was sufficient for my requirements. I picked [a starter kit on Amazon](https://www.amazon.com/gp/product/B0748MBFTS/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1) that included a power supply, HDMI cord, and clear case.
- 32GB MicroSD card
  - You can buy [one with the Raspberry Pi OS pre-installed](https://www.amazon.com/gp/product/B09VG5M4WV/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1) or install the [operating system](https://www.raspberrypi.com/software/) on a blank one.
- A display screen
  - I chose the [HiLetgo MAX7219 Dot Matrix Module](https://www.amazon.com/gp/product/B07FFV537V/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)

## Development

I connected to the Raspberry Pi with SSH. The [setup guide to enable SSH is here](setup.md).

## Resources

- https://api.mta.info/#/subwayRealTimeFeeds
