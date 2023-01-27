# Prerequisites
- You know how to solder.
# Instructions
1. Print one of “top” and “bottom”
    - If you have a smaller print bed, print one of top_l, top_r, bottom_l, bottom_r, in addition to 4x pins
    - Please note that they are designed around a 0.1mm tolerance. The .f3d files are hosted here if you would like to change that.
    - Print settings: 
        - Body - 3+3, no more than 15% infill
        - Pins - 2 horizontal, 3 vertical, no more than 10% infill
2. If you haven't, set up and test [KMK](https://github.com/KMKfw/kmk_firmware/blob/master/docs/Getting_Started.md) on the Raspberry Pi Pico you intend to use. Also, make sure your computer has a text editor that supports circuitpython with a serial window. I used [Mu](https://codewith.mu/).
3. If applicable, glue top_l, to top_r, and bottom_l to bottom_r together using the 4 pins. 
    - Sanding where the parts come together is recommended for fit and bond strength
    - If needed, use a box cutter to deburr the holes/edges
4. Add heat set inserts to “top”
5. Install switches with the LED slots at the bottom
6. Handwire according to the picture below. Make sure the wires are long enough to reach the pi when both halves' front halves when they are touching.
    - each switch needs to have a diode that points towards the rows
    - from left to right, the columns are wired to the pico as follows:
    - from top to bottom, the rows are wired to the pico as follows:
7. Transfer all the files from "Splaynck Code" to the pi pico.
    - The default layout is Colemak-DH. If you use another layout, now is the time to change it.
    - boot.py hides the Pi Pico unless the upper leftmost key is held when plugged in.
8. assemble and add the keycaps
    - be careful when closing the upper and lower halves. Take time to nudge the wires into the case before tightening the screws.    
9. Familiarize yourself with the key arrangement
    - Here are some websites that I have used for typing practice:
        - https://gnusenpai.net/colemakclub/
            - Use the ortho setting
        - https://keybr.com/
    - Here is a cheatsheet for the included firmware
