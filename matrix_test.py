from luma.core.interface.serial import spi
from luma.led_matrix.device import max7219
from time import sleep

# SPI interface: CS0=24, CLK=11, DIN=10 (Raspberry Pi pins)
serial = spi(port=0, device=0, cs_gpio=24) 
device = max7219(serial, cascaded=1, block_orientation=0, rotate=0)

# Clear the display
device.clear()

# Clear display
device.clear()

# Example: Turn on the first row fully
for x in range(8):
    device.pixel(x, 0, 1)

device.show()
sleep(5)
# device.clear()

# Links:
# https://en.wikipedia.org/wiki/Serial_Peripheral_Interface (spi)