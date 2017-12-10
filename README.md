# clocky
A simple RPi0 clock-thing using i2c-connected 7-segment LED display

This is a simple LED clock based on Raspberry Pi 0, using the [Adafruit 4-Digit 7-Segment Display with I2C backpack](https://www.adafruit.com/product/878). On the RPi0, enable I2C in Interfacing Options via raspi-config and connect Power, SDA (D), and SCL (C). Easy. We're using libraries here from Adafruit:

```
https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code/blob/legacy/Adafruit_I2C/Adafruit_I2C.py
https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code/tree/legacy/Adafruit_LEDBackpack
```

Note: these are the older (legacy) libraries and are no longer being maintained. See the [Adafruit Github](https://github.com/search?q=org%3Aadafruit+python) for updated Python things. I've included the necessary libraries here; as long as you keep them in the directory with clocky.py, everything should "just work".

clocky.py is essentially the example code in the LEDBackpack .git, with logic added to trap SIGTERM, SIGINT, and SIGHUP and turn off the display when the script is ended. 

![alt text](https://raw.githubusercontent.com/kenkl/clocky/master/IMG_0433_noexif.jpg "action shot")
