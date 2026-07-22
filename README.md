``` 
 ____  ____   __    ____  
(_  _)(  _ \ /__\  (  _ \ 
  )(   )___//(__)\  )(_) )
 (__) (__) (__)(__)(____/                              
```
<sub> just a hackpad but better </sub>

so im made this macropad as a challenge, and it did NOT go well.
made this repo to show yall my progress   <sub> (its only made to submit this project) </sub>    i also couldnt make the knob work because i originally had the wrong 3d model for the rotary encoder.. (i made the knob :D)
anyways ignore all that,
# the pcb.
<figure> <img src="https://github.com/skoped/tpad/blob/main/images%20for%20readme/pcb.png" width="30%" height="30%"/> <figcaption>pcb</figcaption> </figure>  the schematics <img src="https://github.com/skoped/tpad/blob/main/images%20for%20readme/schematic.png" width="30%" height="30%"/>

i made this thing using kicad and tried to make it as tidy as possible which obviously i failed at that. this was probably the easiest part but i kept going back to it because i really didnt do it correctly at first.
# the case.
the case fully put together <img src="https://github.com/skoped/tpad/blob/main/images%20for%20readme/case-full.png" width="30%" height="30%"/> the case laid out in parts <img src="https://github.com/skoped/tpad/blob/main/images%20for%20readme/entire-case-laid-out.png" width="30%" height="30%"/>

worst part of this entire thing, fusion360 was too hard and i decided to experiment a bit with different software. i went on my dads ipad and found the absolute best app for this (very expensive so i used the trial :D). the app is shapr3d, i couldnt use fusion mostly because im using it on a pc with no touchscreen, making it harder to design what i wanted exactly.
# the firmware.
wasnt hard, kmk is easy and has alot of documentation to help with it. hopefully i can someday be good enough at programming to make a gui interface for remapping the keys. i only used layers to add about double the functionality to the keyboard (sixth button changes the entire keymap, and when the knob is pressed it changes brightness instead of volume, i just thought it was a cool way to make this different)
# BOM
6x Cherry MX Switches
6x through-hole 1N4148 diodes
1x Seeed Studios XIAO RP2040
1x 0.91" OLED display SSD1306
1x EC11 rotary encoder
4x Keycaps
4x M3x5x4 headset inserts
4x M3x16mm screws
1x Case (2 part build, top and bottom)
### dont recommend this but will definitely do it again. 0/10
 *pcb and schematics made in kicad, case made in shapr3d, and the firmware made using kmk*

 this is not over, the screen basically doesnt do anything (just shows current keyboard layer) currently so im looking forward to edit its usecase. i also really wanna make that gui app for remapping everything :D
 
