import cv2
import numpy as np
import pyautogui

#I love cum!!!!
# Function to select a color using mouse click
def get_color_at_position(x, y):
    screenshot = pyautogui.screenshot(region=(x, y, 1, 1))  # Capture a 1x1 pixel at (x, y)
    frame = np.array(screenshot)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)  # Convert to BGR for OpenCV
    color_bgr = frame[0, 0]  # Extract the color at the clicked position
    return color_bgr

# Function to track color (you can adjust lower/upper bounds later)
def track_color(lower_color, upper_color):
    while True:
        # Capture the screen
        screenshot = pyautogui.screenshot()
        frame = np.array(screenshot)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)  # Convert to BGR for OpenCV

        # Convert the frame to HSV color space
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Create a mask for the specified color range
        mask = cv2.inRange(hsv_frame, lower_color, upper_color)

        # Find contours of the detected color
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # Draw bounding boxes around the detected color
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Display the live stream with the tracked color
        cv2.imshow("Screen Capture with Color Tracking", frame)

        # Exit on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    cv2.destroyAllWindows()

# Function to interactively choose a color to track
def choose_color():
    print("Click on a point on the screen to select the color for tracking.")
    # Wait for a click (you could use pyautogui to get screen position)
    x, y = pyautogui.position()  # Get the current mouse position
    print(f"Color selected at position ({x}, {y})")
    selected_color_bgr = get_color_at_position(x, y)
    print(f"Selected color (BGR): {selected_color_bgr}")
    
    # Convert the selected BGR color to HSV to define the range
    selected_color_hsv = cv2.cvtColor(np.uint8([[selected_color_bgr]]), cv2.COLOR_BGR2HSV)[0][0]
    print(f"Selected color (HSV): {selected_color_hsv}")

    # Define a range for the color (you can tweak these values)
    lower_color = np.array([selected_color_hsv[0] - 10, 50, 50])  # Lower bound (H-10)
    upper_color = np.array([selected_color_hsv[0] + 10, 255, 255])  # Upper bound (H+10)

    track_color(lower_color, upper_color)

# Call the function to choose a color
#al;kslkjasdf;ljkasdjklfsad;fjksadlfkj;sdfjl;kasfdlkj;a
choose_color()