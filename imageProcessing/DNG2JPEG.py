import numpy as np
import cv2
import rawpy

# DNG 파일은 압축될 수 있으므로(무손실 형식일지라도) 먼저 dng 이미지를 디코딩해야 합니다.
# https://pypi.org/project/rawpy/
path = '.\imageFile\DJI_0583.DNG'    
with rawpy.imread(path) as raw:
    rgb = raw.postprocess()


# # 결과값 확인하기(1번)
# cv2.imshow('원본파일', rgb)
# cv2.waitKey()
# cv2.destroyAllWindows()

## 결과값 확인하기(2번)
from matplotlib import pyplot as plt
plt.axis('off')
plt.imshow(rgb)
plt.show()

# 이미지 포맷변경 : 이것 안하면 색깔이 뒤바뀌어서 저장된다.
transImage2 = cv2.cvtColor(rgb, cv2.COLOR_BGR2RGB)

# # 결과값 저장하기
cv2.imwrite('.\imageFile\DJI_0583666.PNG', transImage2,
            [cv2.IMWRITE_PNG_COMPRESSION, 5])
# cv2.imwrite('.\imageFile\DJI_0583.jpg', rgb,
#             [cv2.IMWRITE_JPEG_QUALITY,90])