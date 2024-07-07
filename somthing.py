import cv2

# Step 1: Capture or Load an Image
image_path = r'C:\Users\adhvi\Downloads\Screenshot 2024-07-07 221727.jpg'  # Use raw string literals to avoid unicode escape errors
image = cv2.imread(image_path)

# Verify that the image was loaded correctly
if image is None:
    print("Error: Unable to open image. Check the file path and file integrity.")
    exit()

# Step 2: Preprocess the Image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Step 3: Threshold the Image
_, thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)

# Step 4: Find Contours
contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Step 5: Draw Bounding Box around Detected Contours
for contour in contours:
    if cv2.contourArea(contour) > 100:  # Adjust the contour area threshold as needed
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Step 6: Save the Output Image
output_image_path = r'C:\Users\adhvi\Downloads\output_image.jpg'  # Use raw string literals to avoid unicode escape errors
cv2.imwrite(output_image_path, image)

# Display the input and output images
cv2.imshow('Input Image', cv2.imread(image_path))
cv2.imshow('Output Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
