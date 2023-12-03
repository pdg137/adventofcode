This code was developed under the following firmware version:

```
MicroPython v1.22.0-preview-8-g05cb1406a build 231113-f852876; with ulab 6.4.0a05ec05; Pololu Zumo 2040 Robot
```

For best compatibility, start by installing a complete Zumo 2040
firmware; this firmware will run fine on Pico and you can just install
it from Thonny. You will need to [install the thonny-pololu
plugin](https://www.pololu.com/docs/0J87/5.3) for Thonny to recognize
this custom version of MicroPython.

You can also start by installing the [Zumo 32U4 example
code](https://github.com/pololu/zumo-2040-robot/tree/master/micropython_demo
) from GitHub into some other MicroPython installation.

For my custom OLED connection using pins 14-17, replace the modified
`zumo_2040_robot/display.py` with the version here.

Copy the other files into the top level and restart the board.

The display code has the following license:

```
Copyright (c) 2023 Pololu Corporation (www.pololu.com)

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.
```
