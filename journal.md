---
title: "SkyBase"
author: "Wrexik"
description: "An open-ipc video base station for SkyScan drone. To recive video on the fly!"
created_at: "2025-06-20"
time_spent: "h"
---

# Inital idea & explanation
## Initial Idea
- small box with a Radxa ZERO 3W
- external wifi module for better signal (Custom pcb)
- small fan for cooling
- power bank module for power supply & external USB power out
- oled status display???
  
## Explanation
This will be a seperate device to record and view the video feed from the drone. It will have a custom case with an anthenna and Radxa ZERO 3W. With some fan for cooling. And a power bank module to power it. And possibly a small external lcd display. So it will also have some kind of USB power out.

The case will be 3d printed to support customization. There will be connectors for the antennas on the body of the box. The Radxa ZERO 3W will be inside, the ports of the board will not be accessible apart from the part of the gpio pins. I want to have it more like a closed box, so only hdmi, power and usb will be accessible.

The box will have a small fan to cool the Radxa ZERO 3W. The fan will be powered by the power bank module. The power bank module will also have a USB port to power other devices. The box will have a small oled display to show the status of the device. The display will show the battery level, wifi signal strength and other information.

# 2025-06-24: Planing the components and buttons
## Components
- Radxa ZERO 3W
- RTL8812AU on an external pcb, connected to the Radxa ZERO 3W via USB
- Power bank module with USB output - 5V 3A 10000mAh
- Small fan for cooling - 5V 0.2A
- OLED display - 0.96" I2C 128x64
- Buttons - 4x push buttons
- Leds - might be replaced with the oled display

## Buttons
- channel increase
- channel decrease
- start/stop DVR
- toggle bandwidth

> here is the button layout
![Gpio pinout](/img/gpio.png)

the pins 27 and 28 will be used by the oled display. 

will be continuing in a minute...