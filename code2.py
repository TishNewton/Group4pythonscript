import pygame
import serial
import time

# Set up the serial connection with the ESP32
# Replace 'COMX' with the correct serial port name (e.g., 'COM3' on Windows or '/dev/ttyUSB0' on Linux)
ser = serial.Serial('COMX', 9600, timeout=0.1)

# Initialize Pygame
pygame.init()

# Define the screen size (you can adjust this based on your requirements)
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Function to send commands to the ESP32


def send_command(command):
    # Send the command as a byte
    ser.write(bytes([command]))


# Main loop
running = True
while running:
    # Handle events (e.g., keyboard inputs)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Check for specific keys
            if event.key == pygame.K_UP:
                print("Moving Up")
                # Replace this value with the appropriate command for moving up
                send_command(255)
            elif event.key == pygame.K_DOWN:
                print("Moving Down")
                # Replace this value with the appropriate command for moving down
                send_command(0)
            elif event.key == pygame.K_RIGHT:
                print("Moving Right")
                # Replace this value with the appropriate command for moving right
                send_command(128)
            elif event.key == pygame.K_LEFT:
                print("Moving Left")
                # Replace this value with the appropriate command for moving left
                send_command(128)

    # You can add other controls or functions here if needed

    # Add a small delay to prevent the loop from running too fast
    time.sleep(0.05)

# Close the serial connection and quit Pygame
ser.close()
pygame.quit()
