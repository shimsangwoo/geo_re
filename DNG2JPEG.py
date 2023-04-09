import numpy as np
import cv2
import rawpy

# DNG 파일은 압축될 수 있으므로(무손실 형식일지라도) 먼저 dng 이미지를 디코딩해야 합니다.
# https://pypi.org/project/rawpy/
path = '.\imageFile\DJI_0583.DNG'    
with rawpy.imread(path) as raw:
    rgb = raw.postprocess()


# # 결과값 확인하기
# cv2.imshow('원본파일', rgb)
# cv2.waitKey()
# cv2.destroyAllWindows()

# 결과값 저장하기
cv2.imwrite('.\imageFile\DJI_0583.PNG', rgb,
            [cv2.IMWRITE_PNG_COMPRESSION, 5])
cv2.imwrite('.\imageFile\DJI_0583.jpg', rgb,
            [cv2.IMWRITE_JPEG_QUALITY,90])
