"""
-------------------------------
Name: exploring_processing.py
Purpose: Demonstrate I can code the following tasks:
- setting the background to an image
- draw 3 different shapes
- 1 animated shape, try to get it to bounce off the walls of the window.
- 1 animated image
- 1 mouse event (i.e change direction of animated shape or animated image)
- an event initiated by a keypress
- display text

Author: Lin.I

Created: 11/11/2018
-------------------------------
"""

# Mouse event variable
slide_number = 1

# Variables for image animation
image_width = 290
image_height = 235
image_delta_x = 0
image_delta_y = 0
image_speed_x = 5
image_speed_y = 3

# Variables for face animation
face_size_x = 100
face_size_y = 100
face_pos_x = 400
face_pos_y = 250
face_speed_x = 7
face_speed_y = 5

background_colour = 0
background_colour_increment = 20
face_colour = 255
face_colour_increment = 20

# Plane animation variables
plane_delta_x = 500
plane_delta_y = -100
plane_speed_x = -4
plane_speed_y = 2

cloud_delta_x = 0
cloud_speed = 1


# Functions for face animation
def change_background_colour(background_colour):
    global background_colour_increment
    background_colour += background_colour_increment
    # keep rgb value inside 0 - 255
    if background_colour >= 255 or background_colour <= 0:
        background_colour_increment *= -1
        if background_colour > 255:
            background_colour = 255
        else:
            background_colour = 0
    return background_colour


def change_face_colour(face_colour):
    global face_colour_increment
    face_colour -= face_colour_increment
    # keep rgb value inside 0 - 255
    if face_colour >= 255 or face_colour <= 0:
        face_colour_increment *= -1
        if face_colour > 255:
            face_colour = 255
        else:
            face_colour = 0
    return face_colour


def setup():
    global apple, groot
    size(800, 500)
    apple = loadImage("apple.jpg")
    apple.resize(width, height)
    groot = loadImage("groot.gif")


def draw():
    global slide_number
    global image_width, image_height
    global image_delta_x, image_delta_y, image_speed_x, image_speed_y
    global face_pos_x, face_pos_y, face_speed_x, face_speed_y
    global background_colour, face_colour
    global plane_delta_x, plane_delta_y, plane_speed_x, plane_speed_y
    global cloud_delta_x, cloud_speed

    if slide_number == 1:
        # Instructions for how to navigate
        background(255)
        fill(0)
        textSize(35)
        textAlign(CENTER)
        text("Click Mouse or Press ENTER to go Forward", 400, 100)
        text("Press BACKSPACE to go Back", 400, 160)
        text("Press \"i\" to Invert Colours", 400, 220)
        text("Press \"g\" for Grayscale", 400, 280)
        text("Press \"b\" to Blur", 400, 340)
        text("Press \"r\" to Reset Filter Effects", 400, 400)

    elif slide_number == 2:
        # Sets the background to a picture of apples
        background(apple)

    elif slide_number == 3:
        background(255)
        image(groot, image_delta_x, image_delta_y, image_width, image_height)

        # Animating image of groot
        image_delta_x += image_speed_x
        image_delta_y += image_speed_y

        # Bounce image if it hits the sides
        if image_delta_x < 0 or image_delta_x > width-image_width:
            image_speed_x *= -1
        elif image_delta_y < 0 or image_delta_y > height-image_height:
            image_speed_y *= -1

    elif slide_number == 4:
        background(0, 128, 0)

        # Large white square for board
        fill(255)
        rect(150, 0, 500, 500)

        # Black squares overlaid on white square
        for x_black in range(150, 601, 100):
            for y_black in range(50, 451, 100):
                fill(0)
                rect(x_black, y_black, 50, 50)
        for x_black in range(200, 601, 100):
            for y_black in range(0, 451, 100):
                fill(0)
                rect(x_black, y_black, 50, 50)

        # Checkers Pieces
        for red_piece in range(225, 626, 100):
            for red_row in range(25, 150, 100):
                fill(240, 60, 50)
                ellipse(red_piece, red_row, 30, 30)
        for red_piece in range(175, 626, 100):
            ellipse(red_piece, 75, 30, 30)

        for white_piece in range(175, 601, 100):
            for white_row in range(375, 500, 100):
                fill(255)
                ellipse(white_piece, white_row, 30, 30)
        for white_piece in range(225, 626, 100):
            ellipse(white_piece, 425, 30, 30)

    elif slide_number == 5:
        # Face Animation
        background(background_colour)
        fill(face_colour)
        noStroke()

        # Draw face
        ellipse(face_pos_x, face_pos_y, face_size_x, face_size_y)

        # Draw eyes
        fill(background_colour)
        ellipse(face_pos_x - 20, face_pos_y - 10, 10, 10)
        ellipse(face_pos_x + 20, face_pos_y - 10, 10, 10)

        # Draw mouth
        for i in range(20):
            ellipse(face_pos_x - 10 + i, face_pos_y + 20, 5, 5)

        # Animate face
        face_pos_x += face_speed_x
        face_pos_y += face_speed_y

        # Change shade of background and face when face bounces off the side
        if face_pos_x <= face_size_x/2 or face_pos_x >= width - face_size_x/2:
            face_speed_x *= -1
            background_colour = change_background_colour(background_colour)
            face_colour = change_face_colour(face_colour)

        elif (face_pos_y <= face_size_y/2 or
              face_pos_y >= height - face_size_y/2):
            face_speed_y *= -1
            background_colour = change_background_colour(background_colour)
            face_colour = change_face_colour(face_colour)

    elif slide_number == 6:
        background(0, 191, 255)
        noStroke()
        # Ground
        fill(100)
        rect(0, 350, width, 150)
        fill(255)
        rect(0, 450, width, 10)

        # Airport
        fill(165)
        quad(0, 300, 450, 300, 370, 350, 0, 350)
        fill(190)
        rect(10, 230, 30, 120)
        fill(180)
        quad(-15, 210, 65, 210, 55, 260, -5, 260)

        # Sun
        fill(255, 211, 25)
        ellipse(780, 0, 150, 150)

        # Clouds
        fill(255)
        ellipse(-300+cloud_delta_x, 65, 100, 25)
        ellipse(-220+cloud_delta_x, 90, 80, 16)
        ellipse(-150+cloud_delta_x, 100, 100, 30)
        ellipse(cloud_delta_x, 80, 40, 25)
        ellipse(160+cloud_delta_x, 40, 120, 40)
        ellipse(300+cloud_delta_x, 50, 110, 45)
        ellipse(540+cloud_delta_x, 30, 60, 19)
        ellipse(700+cloud_delta_x, 55, 130, 30)

        # Animate clouds
        cloud_delta_x += cloud_speed

        # Plane
        fill(255)

        # Back wing
        quad(580+plane_delta_x, 120+plane_delta_y, 650+plane_delta_x,
             120+plane_delta_y, 680+plane_delta_x, 40+plane_delta_y,
             650+plane_delta_x, 40+plane_delta_y)

        # Plane body
        rect(550+plane_delta_x, 100+plane_delta_y, 165, 50)
        stroke(2)
        line(595+plane_delta_x, 99+plane_delta_y,
             660+plane_delta_x, 99+plane_delta_y)

        # Front wing
        quad(580+plane_delta_x, 130+plane_delta_y, 650+plane_delta_x,
             130+plane_delta_y, 680+plane_delta_x, 200+plane_delta_y,
             650+plane_delta_x, 200+plane_delta_y)
        noStroke()

        # Plane back
        quad(710+plane_delta_x, 100+plane_delta_y, 715+plane_delta_x,
             150+plane_delta_y, 765+plane_delta_x, 70+plane_delta_y,
             745+plane_delta_x, 70+plane_delta_y)

        # Plane front
        triangle(550+plane_delta_x, 100+plane_delta_y, 550+plane_delta_x,
                 150+plane_delta_y, 500+plane_delta_x, 140+plane_delta_y)
        stroke(1)

        # Back wing
        quad(705+plane_delta_x, 110+plane_delta_y, 735+plane_delta_x,
             110+plane_delta_y, 745+plane_delta_x, 140+plane_delta_y,
             735+plane_delta_x, 140+plane_delta_y)

        # Windows
        fill(200)
        for windows in range(555, 700, 15):
            rect(windows+plane_delta_x, 105+plane_delta_y, 7, 10, 7)

        # Front window
        noStroke()
        quad(550+plane_delta_x, 105+plane_delta_y, 550+plane_delta_x,
             115+plane_delta_y, 530+plane_delta_x, 115+plane_delta_y,
             543+plane_delta_x, 105+plane_delta_y)

        # Plane movement
        plane_delta_x += plane_speed_x
        plane_delta_y += plane_speed_y
        if plane_delta_y >= 300:
            plane_speed_y = 0
        # Reset animations after plane is out of screen
        if plane_delta_x <= -850:
            plane_delta_x = 500
            plane_delta_y = -100
            plane_speed_x = -4
            plane_speed_y = 2
            cloud_delta_x = 0
            cloud_speed = 1

    # Filter effect from key enter
    if key == "i":
        filter(INVERT)
    elif key == "g":
        filter(GRAY)
    elif key == "b":
        filter(BLUR, 6)
    elif key == "r":
        noTint()


def mouseClicked():
    global slide_number
    # Advance slide if mouse is clicked
    if slide_number < 6:
        slide_number += 1


def keyPressed():
    global slide_number
    # Advance slide if ENTER is pressed
    if key == ENTER and slide_number < 6:
        slide_number += 1
    # Go back if BACKSPACE is pressed
    elif key == BACKSPACE and slide_number > 1:
        slide_number -= 1
