import numpy as np
import cv2
from PIL import ImageGrab

path = './imageProcessing/imageFile/postProcessImage/'  # 역슬래쉬를 하면 오류가 생긴다???
x, y, width, height = (0, 0, 800, 600)  # 스크린샷 크기를 조정할 수 있다. 왼쪽상단이 기준점이다.

# Capture the entire screen
screen = np.array(ImageGrab.grab(bbox=(x, y, x + width, y + height)))

# Save the screenshot as a PNG file
cv2.imwrite(path +'screenshot.png', screen)
