# 이 코드는 jpeg파일에 적용하시오. RAW파일 또는 DNG파일은 적용할 경우 해상도 현저한 저하가 있을 수 있습니다.
# >>>>  DNG2JPEG.py 사용할 것

import numpy as np
import cv2


imageFile = '.\imageFile\DJI_0582.DNG'
img = cv2.imread(imageFile)   # 이미지파일을 img에 할당
# img2 = cv2.imread(imageFile, 0)  # 이미지파일을 흑백으로 할당

# 경로에 한글이 있을 경우 인코딩-디코딩 과정을 거쳐야 한다. 교과서p.22 참조

# encode_img = np.fromfile(imageFile, np.uint8) 
# img = cv2.imdecode(encode_img, cv2.IMREAD_UNCHANGED)

cv2.imshow('보여줘', img)
cv2.waitKey()
cv2.destroyAllWindows()
