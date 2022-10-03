# Prerequisites
The instructions assume the following:
- You can solder.
- You have set up and tested [KMK](https://github.com/KMKfw/kmk_firmware) on the Raspberry Pi Pico you intend to use.

# Instructions
1. Print one of “top” and “bottom”
    - If you have a smaller print bed, print one of top_l, top_r, bottom_l, bottom_r, in addition to 4x pins
    - Please note that they are designed around a 0.1mm tolerance. The .f3d files are hosted here if you would like to change that.
    - Print settings: 
        - Body - 3+3, no more than 15% infill
        - Pins - 2 horizontal, 3 vertical, no more than 10% infill
2. Glue top_l, to top_r, and bottom_l to bottom_r together using pins. 
    - Sanding where the parts come together is recommended for fit and bond strength
    - If needed, use a box cutter to deburr the holes/edges
3. Add heat set inserts to “top”
4. Install switches with the LED slots at the bottom
5. Handwire according to
6. download the main.py and kb.py files from and transfer to the pi pico
