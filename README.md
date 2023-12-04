This code was developed under the following firmware version:

```
MicroPython v1.22.0-preview-8-g05cb1406a build 231113-f852876;
 with ulab 6.4.0a05ec05; Pololu Zumo 2040 Robot
```

For best compatibility, start by installing a complete Zumo 2040
firmware; this firmware will run fine on Pico and you can just install
it from Thonny. You will need to [install the thonny-pololu
plugin](https://www.pololu.com/docs/0J87/5.3) for Thonny to recognize
this custom version of MicroPython.

You can also start by installing the [Zumo 32U4 example
code](https://github.com/pololu/zumo-2040-robot/tree/master/micropython_demo
) from GitHub into some other MicroPython installation.

For my custom OLED connections using pins 14-17, replace the modified
`zumo_2040_robot/display.py` with the version here.

Copy the other files into the top level and restart the board.
