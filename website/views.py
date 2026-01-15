from flask import Blueprint, render_template, request
from luma.core.interface.serial import spi
from luma.led_matrix.device import max7219
from luma.core.render import canvas  # <-- important

views = Blueprint("views", __name__)

# SPI interface: CS0=24, CLK=11, DIN=10 (Raspberry Pi pins)
serial = spi(port=0, device=0, cs_gpio=24) 
device = max7219(serial, cascaded=1, block_orientation=0, rotate=0)

def idxToGrid(idx, width):
    return idx%width, idx//width

@views.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        json = request.json

        device.clear()
        with canvas(device) as draw:
            for idx, bool in enumerate(json):
                x, y = idxToGrid(idx, 8)
                draw.point((x, y), fill=1 if bool else 0)
        device.show()

    return render_template("home.html")

# Links:
# https://en.wikipedia.org/wiki/Serial_Peripheral_Interface (spi)