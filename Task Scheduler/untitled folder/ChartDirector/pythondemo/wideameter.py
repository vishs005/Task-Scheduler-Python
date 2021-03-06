#!/usr/bin/python
from pychartdir import *

def createChart(img) :

    # The value to display on the meter
    value = 6.5

    # Create an AugularMeter object of size 200 x 100 pixels with rounded corners
    m = AngularMeter(200, 100)
    m.setRoundedFrame()

    # Set meter background according to a parameter
    if img == "0" :
        # Use gold background color
        m.setBackground(goldColor(), 0x000000, -2)
    elif img == "1" :
        # Use silver background color
        m.setBackground(silverColor(), 0x000000, -2)
    elif img == "2" :
        # Use metallic blue (9898E0) background color
        m.setBackground(metalColor(0x9898e0), 0x000000, -2)
    elif img == "3" :
        # Use a wood pattern as background color
        m.setBackground(m.patternColor2("wood.png"), 0x000000, -2)
    elif img == "4" :
        # Use a marble pattern as background color
        m.setBackground(m.patternColor2("marble.png"), 0x000000, -2)
    else :
        # Use a solid light purple (EEBBEE) background color
        m.setBackground(0xeebbee, 0x000000, -2)

    # Set the meter center at (100, 235), with radius 210 pixels, and span from -24
    # to +24 degress
    m.setMeter(100, 235, 210, -24, 24)

    # Meter scale is 0 - 100, with a tick every 1 unit
    m.setScale(0, 10, 1)

    # Set 0 - 6 as green (99ff99) zone, 6 - 8 as yellow (ffff00) zone, and 8 - 10 as
    # red (ff3333) zone
    m.addZone(0, 6, 0x99ff99, 0x808080)
    m.addZone(6, 8, 0xffff00, 0x808080)
    m.addZone(8, 10, 0xff3333, 0x808080)

    # Add a title at the bottom of the meter using 10 pts Arial Bold font
    m.addTitle2(Bottom, "OUTPUT POWER LEVEL\n", "arialbd.ttf", 10)

    # Add a semi-transparent black (80000000) pointer at the specified value
    m.addPointer(value, 0x80000000)

    # Output the chart
    m.makeChart("wideameter%s.png" % img)


createChart("0")
createChart("1")
createChart("2")
createChart("3")
createChart("4")
createChart("5")

