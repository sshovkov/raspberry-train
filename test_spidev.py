import spidev
import time

# Open SPI bus
spi = spidev.SpiDev()
spi.open(0, 0)  # Use CE0 (Chip Enable 0) as the slave select line

# Send data (for example, 0x01) to the MAX7219 module
spi.xfer2([0x01])

# Close SPI bus
spi.close()

print("SPI communication test successful.")
