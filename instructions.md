# Prerequisites
- You know how to solder.
# Instructions
1. Print one of “top” and “bottom” and the pi pico holder.
    - If you have a smaller print bed, print one of top_l, top_r, bottom_l, bottom_r, in addition to 4x pins instead of "top" and "bottom"
    - There are two variations of the top: one with a HHKB-inspired layout and one that is for ortholinear (all 1u) keycap sets.
2. If you haven't, set up and test [KMK](https://github.com/KMKfw/kmk_firmware/blob/master/docs/Getting_Started.md) on the Raspberry Pi Pico you intend to use. Also, make sure your computer has a text editor that supports circuitpython with a serial window. I used [Mu](https://codewith.mu/).
3. If applicable, glue top_l, to top_r, and bottom_l to bottom_r together using the 4 pins. 
    - Sanding where the parts come together is recommended for fit and bond strength.
    - If needed, use a box cutter to deburr the holes/edges.
    - Feel free to sand the outside once the glue is cured.
4. Add heat set inserts to the 8 holes in “top”
5. Install switches with the LED slots at the bottom
6. insert the Pi Pico into the holder, and the holder into the bottom. Note that the Pi Pico will only go in one way.
![pico holder](/images/hodl_the_pico.jpg)
![mounted](/images/pico_mounted.jpg)
    - It is optional, but hightly reccomended that the Pi Pico is fastened to the insert by the use of pins made of short lengths of 1.75mm filament. You will likely need to ream the holes in the holder with a 2mm drill bit before the filament will fit. Make sure that the filament is cut flush with the top of the holder as shown below.
    - The bottom corners will likely need some sanding.
7. Handwire according to the pictures below. Make sure the wires are long enough to reach the pi when both halves' front halves when they are touching.
![wiring](/images/all_wired.jpg)
![wiring diagram](/images/splaynck_wiring.png)
    - **each switch needs to have a diode that points towards the rows**
    - **Note that the wiring in the middle of the second to topmost row is bent to clear the support in the bottom half of the case**
    - from left to right, the columns are wired to the pico on pins 
    - from top to bottom, the rows are wired to the pico on pins 
8. Transfer all the files from "Splaynck Code" to the pi pico. Test the keyboard while everything is acessible.
    - **Make sure that "old main.py" is renamed to "main.py" or "code.py"**
    - The default layout is Colemak-DH. If you use another layout, now is the time to change it.
    - boot.py hides the Pi Pico's drive unless the upper leftmost key is held when plugged in. You do not need to have this, but it is reccomended to make sure that the keyboard will immediately work when plugged in.
9. assemble and add the keycaps
    - be careful when closing the upper and lower halves. Take time to nudge the wires into the case before tightening the screws. **Do not overtighten**    
10. Familiarize yourself with the key arrangement.
    - Here are some websites that I have used for typing practice:
        - https://gnusenpai.net/colemakclub/
            - Use the ortho setting
        - https://keybr.com/
    - Here is a cheatsheet for the included firmware:
![keymap](/images/cheatsheet.PNG)
