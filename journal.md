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
```aprox 3h```
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

Now I will be drawing a little sketch of the idea I have in mind. It will show how I plan to make it. And also show the formfactor im aiming for. 
Here is the sketch:
![Sketch](/img/sketch.png)

# 2025-06-26: Pinout and components
```aprox 2,5h```
Quick pinout of the Radxa ZERO 3W and how I plan to connect the components:
```
+3.3V (Pin 1) -------------------+-------------------------+---------------------------+-------------------------+----------------+
                                 |                         |                           |                         |
                             Button 1 (CH+)             Button 2 (CH–)             Button 3 (DVR)           Button 4 (BW toggle)
                              (Pin 15 / GPIO22)         (Pin 16 / GPIO23)           (Pin 18 / GPIO24)          (Pin 32 / GPIO12)
                                 |                         |                           |                         |
                               Input                    Input                      Input                     Input
                                 |                         |                           |                         |
                                GND                       GND                         GND                       GND
                               (Common ground pins: 6,9,14)

+5V (Pin 2) ---------------- Fan + (5V supply)

GND (Pin 6 or 9) ----------- Fan – (Ground)

OLED Display (I²C):
    SDA: GPIO2 (Pin 3)
    SCL: GPIO3 (Pin 5)
    VCC: 3.3V (Pin 1)
    GND: Ground (Pin 6)

Status LED:
    Anode (+) → +5V
    Cathode (–) → 1kΩ resistor → GPIOAO_2 (Pin 28) → GND

Recording LED:
    Anode (+) → +5V
    Cathode (–) → 330Ω resistor → GPIO21 (Pin 40) → GND
```

Ive also added a status LED and a recording LED to indicate the status of the device. The status LED will be connected to GPIOAO_2 (Pin 28) and the recording LED will be connected to GPIO21 (Pin 40). Both LEDs will be powered by the +5V pin. There will be a python script running on the Radxa ZERO 3W to control the LEDs + Oled display and read the button inputs.

Im now planning to start modeling the case in OnShape. I have already downloaded some models of the components I will be using. So that the case will make them fit perfectly! See you in a minute!

Just downloaded also a models for the fan and buttons. The buttons will be 6x6mm and the fan will be 40x40x11mm or so. Have to make dinner now, so I will continue CAD-ng later. 

Back, I have uploaded all the models to OnShape and I will start with the modeling.
So far Ive only made the footprint of the fan and the radxa ZERO 3W. This will be enough for modeling the case. The other components and holes are from the side so they will be added later. Now I can make the base and the top of the case. The wifi modules will be probably just double sided tape to the case.

![footprints](/img/footprints.png)


# 2025-06-27: Case modeling
```aprox 2h```
Ive added the rest of the footprints of the components. Im not really sure with the oled now, we will see. Here are the footprints:
![footprints](/img/footprints2.png)

Few hours later...

And Ive kind of started with the case. I somehow lost track of time and kinda just pushed through the modeling. I now have the base nearly nearlyyyy done. But the top looks really nice. I will try to add the buttons and the oled screen now. Here is the current state of the case:

![case](/img/case.png)

# 07-01-2025: Case progress
```aprox 2h```

Ive made it so there is a lot of space for cables. Also a lot of holes for the air to flow. The top will be removable, so it will be easy to access the components inside. 
There are mounts for the Radxa zero, wifi module and power bank module. I will be probably adding more mounts for the HDMI and USB ports. But that will be again easier to do when the components are in the case. But in the current state it should already work great. The 47,5x85 is a case for batteries. I will be using 2x 21700 batteries in it. The antennas will be mounted on the top of the case. On the right top side. There will be ufl to sma cable going from the wifi module to the antenna.
So that it will support easy antenna replacement.
Now I will be adding the buttons and the oled screen. The screen and buttons will be located in the space between the powerbank module and the wifi module. It will allow me to wire it to the GPIO pins easily. Still deciding how many buttons I will need. Because one might be just enough. And I will add status LEDs.

Lets see how it goes.

Okayyy and screen mount and buttons are now added. I will be now working on the links for the products to make a bom and and a table with all the components.
I hope I fit in the 150us budget. I will be trying to keep it as low as possible. And optimize the components.


![added screen and buttons](/img/screen_buttons.png)

I will also try to extrude the case to make somewhat of a preview for you :)

It looks amazing actually! I will be adding the holes and stuff later on. But take a look at this:

![extruded case](/img/extruded_case.png)

adding the table with the components later, see you soon!

# 07-01-2025: Components table
```aprox 1h```

Here is the table with the components I will be using for the SkyBase project.

| Component Name          | Description                                  | Price (USD) | Link                                                                 |
|-------------------------|----------------------------------------------|-------------|----------------------------------------------------------------------|
| Radxa ZERO 3W - 2GB 16GB eMMC with HAT        | Main board for the base station               | 23       | [Radxa ZERO 3W](https://www.aliexpress.com/item/1005008926850854.html)                           |
| RTL8812AU WiFi Module   | External WiFi module for reciving       | 10          | [RTL8812AU](https://www.aliexpress.com/item/1005008617329103.html)                                   |
| Power Bank Module        | For charging and powering the box          | 2          | [Power Bank Module](https://www.aliexpress.com/item/1005005672785825.html)                           |
| 0.96" OLED Display       | For displaying status information          | 3          | [OLED Display](https://www.aliexpress.com/item/1005006141235306.html)                                 |
| 40x40x11mm 5V Fan          | For cooling the Radxa ZERO 3W              | 5          | [40x40x11mm Fan](https://www.aliexpress.com/item/1005002625465685.html)                               |
| 6x6mm Push Buttons       | For user input (2 buttons)                | 2          | [Push Buttons](https://www.aliexpress.com/item/4001166999847.html)                                 |
| Battery Holder for 2x 21700 | For battery storage                        | 2          | [Battery Holder](https://www.aliexpress.com/item/1005007474702125.html)                               |
| Rocker Switch            | For power control                          | 3          | [Rocker Switch](https://www.aliexpress.com/item/1005006360929070.html)                               |
| Ufl to SMA Cable 2x | For connecting antennas                   | 8         | [Ufl to SMA Cable](https://www.aliexpress.com/item/4000848776660.html)                             |
| USB C Male to 4 wires 2x | For power and data connections | 4          | [USB C](https://www.aliexpress.com/item/1005005912113279.html)                                 |
| High Quality Wires for connections | For connecting components | 15          | [Wires](https://www.aliexpress.com/item/1005005450270866.html)                                 |
| SD Card 128GB | For storage of video recordings | 15          | [SD Card](https://www.aliexpress.com/item/1005005947146666.html)                                 |
| TOTAL                   |                                              | **92US$**     |                                                                      |

# 07-02-2025: Final words before pitch
Hey there, ive exported the box. And uploaded it into the 3D-files folder. Ive also made the README explain the project well. And added a bom with the same table as here. I hope yall like it. Im looking forward to building it!

I will be continuing with desinging the case with the components on hand. So if you want to build it your self be ready for a guide and a final case design. I will be writing it all to this jornal :).

Thanks HC!

# 07-04-2025: Changes to get approved
My project was reviewed, but I was missing the electronics in the drawing. I added them to the 3d and I will update the pictures here. Hopefully It will get accepted this time.
I was told it is cool, well I knew that :P. Soo after these little changes I think it will be AOK! Now I will add the screenshots and update it also in the readme.

> New screenshots:
![top](/img/top.png)
![front](/img/front.png)
![back](/img/back.png)

the work on the case will still continue, but now I will be able to order the components and start building it. I will be updating this journal with the progress of the build and the case design. So you can build it too!