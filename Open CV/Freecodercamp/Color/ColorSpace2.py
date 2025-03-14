import cv2

img = cv2.imread("F:/SHIKHER-VS/Advance-Python-SJ/Open CV/Freecodercamp/Photos/gatewayOfIndia.jpg")

# Get all color conversion flags
color_spaces = [attr for attr in dir(cv2) if attr.startswith('COLOR_')]

# Apply each conversion
for space in color_spaces:
    try:
        converted_img = cv2.cvtColor(img, getattr(cv2, space))
        cv2.imshow(space, converted_img)
    except Exception as e:
        print(f"Cannot convert using {space}: {e}")
                    
# Wait for key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
