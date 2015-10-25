#!/usr/bin/python
from pychartdir import *
import cgi

# Get HTTP query parameters
query = cgi.FieldStorage()

# Determine the starting angle and direction based on input parameter
angle = 0
clockwise = 1
if query["img"].value != "0" :
    angle = 90
    clockwise = 0

# The data for the pie chart
data = [25, 18, 15, 12, 8, 30, 35]

# The labels for the pie chart
labels = ["Labor", "Licenses", "Taxes", "Legal", "Insurance", "Facilities",
    "Production"]

# Create a PieChart object of size 280 x 240 pixels
c = PieChart(280, 240)

# Set the center of the pie at (140, 130) and the radius to 80 pixels
c.setPieSize(140, 130, 80)

# Add a title to the pie to show the start angle and direction
if clockwise :
    c.addTitle("Start Angle = %s degrees\nDirection = Clockwise" % (angle))
else :
    c.addTitle("Start Angle = %s degrees\nDirection = AntiClockwise" % (angle))

# Set the pie start angle and direction
c.setStartAngle(angle, clockwise)

# Draw the pie in 3D
c.set3D()

# Set the pie data and the pie labels
c.setData(data, labels)

# Explode the 1st sector (index = 0)
c.setExplode(0)

# Output the chart
print("Content-type: image/png\n")
binaryPrint(c.makeChart2(PNG))

