import RPi.GPIO as GPIO
import tkinter as tk

# Setup GPIO
GPIO.setmode(GPIO.BCM)
RED_PIN = 4
GREEN_PIN = 17
BLUE_PIN = 27

# Set up the GPIO pins as outputs
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)

# Function to update LED states based on toggle button states
def update_leds():
    GPIO.output(RED_PIN, red_var.get())
    GPIO.output(GREEN_PIN, green_var.get())
    GPIO.output(BLUE_PIN, blue_var.get())

# Function to exit the GUI and cleanup GPIO
def exit_gui():
    GPIO.output(RED_PIN, GPIO.LOW)
    GPIO.output(GREEN_PIN, GPIO.LOW)
    GPIO.output(BLUE_PIN, GPIO.LOW)
    GPIO.cleanup()
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("LED Control")

# Create Boolean variables for toggle buttons
red_var = tk.BooleanVar(value=False)
green_var = tk.BooleanVar(value=False)
blue_var = tk.BooleanVar(value=False)

# Create toggle buttons for LED control
red_toggle = tk.Checkbutton(root, text="Red LED", variable=red_var, command=update_leds)
green_toggle = tk.Checkbutton(root, text="Green LED", variable=green_var, command=update_leds)
blue_toggle = tk.Checkbutton(root, text="Blue LED", variable=blue_var, command=update_leds)

# Create an exit button
exit_button = tk.Button(root, text="Exit", command=exit_gui)

# Layout
red_toggle.pack(anchor=tk.W)
green_toggle.pack(anchor=tk.W)
blue_toggle.pack(anchor=tk.W)
exit_button.pack()
root.protocol("WM_DELETE_WINDOW", exit_gui)
# Start the GUI loop
root.mainloop()

