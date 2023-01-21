# esp32-cam board

![https://github.com/ejdam87/esp32cam/blob/master/photos/cover.jpeg](Cover photo)

## Repository consists of several parts:
- micropython **firmware** ( already built .bin file in firmware directory )
- micropython implementation of test program ( morse code with LEDs on camera )
- micropython implementation of **camera webserver**

## Camera setup
- cable connection is described in file **plug.txt**
- to program the board I used **MU editor**
- to connect the board to PC via serial port I used **FTDI programmer** ( little board with USB present )
- as a source of power I used classic **phone powerbank** ( while programming, board is getting power from your PC )

## Flashing
- When using the board for the first time, you will need to "flash" the firmware ( for example the one located in firmware directory ) in order to communicate with the board.
- For this purpose, there are several tools available. I used **esptool** program ( which is also built-in in MU editor ).
- You will need to plug one extra cable in order to flash the firmware ( as stated in plug.txt file ). After flashing, you can easily remove it.

