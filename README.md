# LED-matrix-website
## description
Website served on rasberry pi connected to a LED matrix

## hardware
-rasberry pi 4  
-MAX7219 LED Dot Matrix

## versions
```
blinker==1.9.0
cbor2==5.8.0
click==8.3.1
colorama==0.4.6
Flask==3.1.2
itsdangerous==2.2.0
Jinja2==3.1.6
luma.core==2.5.3
luma.led-matrix==1.7.1
MarkupSafe==3.0.3
pillow==12.1.0
RPi.GPIO==0.7.1
smbus2==0.6.0
spidev==3.8
Werkzeug==3.1.5
```
## installation
```
git clone https://github.com/ddxMusic68/LED-matrix-website
cd project
pip install -r requirements.txt
python -u ./server.py
```
## structure
```
src
├── README.md    -you are here
├── requirements.txt    -dependency versions
├── server.py    -runs server
└── website
    ├── __init__.py
    ├── static
    │   ├── main.css    -css for html
    │   └── main.js    -js for html
    ├── templates
    │   ├── base.html    -links styles and scripts 
    │   └── home.html    -main html page
    └── views.py    -defines routes and methods
```
## Contributing
Pull requests are welcome!

## Licence
MIT

## pictures
<img width="456" height="853" alt="image" src="https://github.com/user-attachments/assets/fd1b15b0-5f54-496c-92d5-5e8eee94718b" />
<a href="https://www.youtube.com/shorts/7CoS2LFYXOQ">
  <img src="https://img.youtube.com/vi/7CoS2LFYXOQ/0.jpg" width="600" alt="LED Matrix Demo">
</a>

