# Importing the libraries for the script

import pygame
import serial

# Initialize Pygame
pygame.init()

# Define the screen size (you can adjust this based on your requirements)
screen_width, screen_height = 520, 520
screen = pygame.display.set_mode((screen_width, screen_height))

# Define the font
font = pygame.font.Font(None, 25)

# Initial values for the throttle, yaw, pitch, and roll.
throttle = 0
yaw = 127
pitch = 127
roll = 127

# Movement speed of the quadcopter(increment/decrement step size for the throttle, yaw, pitch )
movement_speed = 5

# Define the colors for the text
black = (0, 0, 0)
white = (255, 255, 255)

# Set up the serial connection with the ESP32
ser_1, ser_2 = None, None

try:
    ser_1 = serial.Serial('COM7', 9600)
    ser_2 = serial.Serial('COM9', 9600)
except:
    print("No serial port detected")

# Set up the game loop
running = True

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                yaw = pitch = roll = 127
                throttle = 0

            if event.key == pygame.K_w:
                throttle += movement_speed
                if throttle > 255:
                    throttle = 255
            elif event.key == pygame.K_s:
                throttle -= movement_speed
                if throttle < 0:
                    throttle = 0
            elif event.key == pygame.K_UP:
                pitch += movement_speed
                if pitch > 255:
                    pitch = 255
            elif event.key == pygame.K_DOWN:
                pitch -= movement_speed
                if pitch < 0:
                    pitch = 0
            elif event.key == pygame.K_LEFT:
                roll -= movement_speed
                if roll < 0:
                    roll = 0
            elif event.key == pygame.K_RIGHT:
                roll += movement_speed
                if roll > 255:
                    roll = 255
            elif event.key == pygame.K_a:
                yaw -= movement_speed
                if yaw < 0:
                    yaw = 0
            elif event.key == pygame.K_d:
                yaw += movement_speed
                if yaw > 255:
                    yaw = 255

    throttle = round(throttle, 2)
    yaw = round(yaw, 2)
    pitch = round(pitch, 2)
    roll = round(roll, 2)

    # Send the values to the serial ports
    if ser_1 and ser_2:
        ser_2.write(f"{yaw},{throttle}\n".encode())   # "val1,val2"
        ser_1.write(f"{roll},{pitch}\n".encode())
    else:
        print(f"{yaw},{throttle}\n")   # "val1,val2"
        print(f"{roll},{pitch}\n")

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the text
    text_throttle = font.render(f"Throttle: {throttle}", True, black)
    text_yaw = font.render(f"Yaw: {yaw}", True, black)
    text_pitch = font.render(f"Pitch: {pitch}", True, black)
    text_roll = font.render(f"Roll: {roll}", True, black)

    screen.blit(text_throttle, [10, 10])
    screen.blit(text_yaw, [10, 30])
    screen.blit(text_pitch, [10, 50])
    screen.blit(text_roll, [10, 70])

    # Update the screen
    pygame.display.flip()


# Quit Pygame
pygame.quit()
