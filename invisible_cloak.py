import cv2
import numpy as np
import time

# Initialize webcam
cap = cv2.VideoCapture(1)
time.sleep(5)  # Allow camera to adjust

# Capture stable background (median over 50 frames)
background_frames = []
for _ in range(50):
    ret, frame = cap.read()
    if not ret:
        continue
    background_frames.append(np.flip(frame, axis=1))  # Flip for consistency

background = np.median(background_frames, axis=0).astype(np.uint8)

try:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = np.flip(frame, axis=1)  # Flip frame
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # Convert to HSV

        # Define red color range
        lower_red1 = np.array([0, 100, 50])
        upper_red1 = np.array([15, 255, 255])

        lower_red2 = np.array([165, 100, 50])
        upper_red2 = np.array([180, 255, 255])

        # Create masks
        mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
        mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
        mask = mask1 + mask2

        # Apply Gaussian blur to smooth edges
        mask = cv2.GaussianBlur(mask, (15, 15), 0)  

        # Create an inverse mask
        mask_inv = cv2.bitwise_not(mask)

        # Feathering the mask (Weighted mask for soft edges)
        mask_f = cv2.GaussianBlur(mask, (21, 21), 0) / 255.0
        mask_inv_f = cv2.GaussianBlur(mask_inv, (21, 21), 0) / 255.0

        # Apply feathered mask to frame and background
        res1 = frame.astype(float) * mask_inv_f[..., np.newaxis]
        res2 = background.astype(float) * mask_f[..., np.newaxis]

        # Blend the results smoothly
        final_output = cv2.addWeighted(res1.astype(np.uint8), 1, res2.astype(np.uint8), 1, 0)

        # Display output
        cv2.imshow("Invisible Cloak - Smooth", final_output)

        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except Exception as e:
    print(f"Error: {e}")

finally:
    cap.release()
    cv2.destroyAllWindows()
