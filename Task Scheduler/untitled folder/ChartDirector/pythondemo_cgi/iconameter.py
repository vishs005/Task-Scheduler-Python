#!/usr/bin/python
from pychartdir import *

# The value to display on the meter
value = 85

# Create an AugularMeter object of size 70 x 90 pixels, using black background with a
# 2 pixel 3D depressed border.
m = AngularMeter(70, 90, 0, 0, -2)

# Set directory for loading images to current script directory
# Need when running under Microsoft IIS
m.setSearchPath(os.path.dirname(sys.argv[0]))

# Use white on black color palette for default text and line colors
m.setColors(whiteOnBlackPalette)

# Set the meter center at (10, 45), with radius 50 pixels, and span from 135 to 45
# degress
m.setMeter(10, 45, 50, 135, 45)

# Set meter scale from 0 - 100, with the specified labels
m.setScale2(0, 100, ["E", " ", " ", " ", "F"])

# Set the angular arc and major tick width to 2 pixels
m.setLineWidth(2, 2)

# Add a red zone at 0 - 15
m.addZone(0, 15, 0xff3333)

# Add an icon at (25, 35)
m.addText(25, 35, "<*img=gas.gif*>")

# Add a yellow (ffff00) pointer at the specified value
m.addPointer(value, 0xffff00)

# Output the chart
print("Content-type: image/png\n")
binaryPrint(m.makeChart2(PNG))

