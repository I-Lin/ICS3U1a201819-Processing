"""
-------------------------------
Name: clouds.py
Purpose: Create a function in processing that
will be called three times to draw animated clouds.

Author: Lin.I

Created: 16/11/2018
-------------------------------
"""

# variables for cloud animation
cloud_speed = 5
cloud_delta_x = -850


def setup():
    size(800, 450)


def draw():
    global cloud_speed, cloud_delta_x
    background(11, 132, 232)

    # Drawing clouds at different locations with drawCloud function
    drawCloud(cloud_delta_x*5/6, height/2, "#e89d09")
    drawCloud(width/3+cloud_delta_x, height/4, "#c842f4")
    drawCloud(width*2/3+cloud_delta_x*3/4, height*2/3, "#d62222")

    # Cloud movement
    cloud_delta_x += cloud_speed

    # When clouds are off the screen, reset cloud locations
    if cloud_delta_x > 1200:
        cloud_delta_x = -850


def drawCloud(cloud_pos_x, cloud_pos_y, cloud_colour):
    noStroke()
    fill(cloud_colour)
    ellipse(cloud_pos_x-50, cloud_pos_y, 120, 70)
    ellipse(cloud_pos_x+25, cloud_pos_y+10, 120, 70)
    ellipse(cloud_pos_x, cloud_pos_y-25, 120, 70)