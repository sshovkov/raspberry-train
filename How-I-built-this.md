## Materials

- Raspberry Pi Zero W
  - I chose this one because was affordable, included built-in Wi-Fi, and was sufficient for my requirements. I picked [a starter kit on Amazon](https://www.amazon.com/gp/product/B0748MBFTS/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1) that included a power supply, HDMI cord, and clear case.
- 32GB MicroSD card
  - You can buy [one with the Raspberry Pi OS pre-installed](https://www.amazon.com/gp/product/B09VG5M4WV/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1) or install the [operating system](https://www.raspberrypi.com/software/) on a blank one.
- A display screen
  - I chose the [HiLetgo MAX7219 Dot Matrix Module](https://www.amazon.com/gp/product/B07FFV537V/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)

## Setup and connecting the Raspberry Pi

There's a few different ways to connect the Raspberry Pi to your computer (gadget mode, ssh, etc). I found that enabling SSH and connecting via IP was easiest method, as well as the most efficient. You can find my setup approach [here](setup.md).

## Development

To connect via IP, I use `ssh sophiashovkovy@raspberrypi`.

If it doesn't work, use`ping raspberrypi.lan` to get the IP address and ssh in with `ssh sophiashovkovy@<ip-address>`.
