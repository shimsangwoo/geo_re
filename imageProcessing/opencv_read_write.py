# 이 코드는 jpeg파일에 적용하시오. RAW파일 또는 DNG파일은 적용할 경우 해상도 현저한 저하가 있을 수 있습니다.
# >>>>  DNG2JPEG.py 사용할 것

import numpy as np
import cv2
from matplotlib import pyplot as plt

imageFile = '.\imageProcessing\imageFile\이서.jpg'

img = cv2.imread(imageFile)   # 이미지파일을 img에 할당
# img2 = cv2.imread(imageFile, 0)  # 이미지파일을 흑백으로 할당

# 경로에 한글이 있을 경우 인코딩-디코딩 과정을 거쳐야 한다. 교과서p.22 참조
encode_img = np.fromfile(imageFile, np.uint8)
img = cv2.imdecode(encode_img, cv2.IMREAD_UNCHANGED)

#### 맷플롯으로 보면 파랗게 나온다.RGB
# plt.imshow(img)
# plt.show()

#### 씨브이투로 보면 정상으로 나온다.BRG
# cv2.imshow('hhh', img)
# cv2.waitKey()
# cv2.destroyAllWindows()

#### 크기를 조정해보자
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.figure(figsize= (9,9))
plt.axis('off')
plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
plt.imshow(img2)
plt.show()


