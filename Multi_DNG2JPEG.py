import numpy as np
import cv2
import rawpy
# from matplotlib import pyplot as plt

# DNG 파일은 압축될 수 있으므로(무손실 형식일지라도) 먼저 dng 이미지를 디코딩해야 합니다.
# https://pypi.org/project/rawpy/

##### 아래의 입력값을 넣어주세요 ####
startNo = 582 
endNo = 585
compressure = 90
########################################
for i in range(startNo, endNo+1):
    img = f'.\imageFile\DJI_0{i}.DNG'
    with rawpy.imread(img) as raw:     # raw데이터를 읽는다.
        bgr = raw.postprocess()        # 들여쓰기 할 것
    rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
    cv2.imwrite(f'.\imageFile\postProcessImage\DJI_0{i}.jpg', rgb, [cv2.IMWRITE_JPEG_QUALITY,compressure])
# 파일 하나씩 저장(postProcessImage 폴더안)

########################################

# 결과값 저장하기___PNG파일
# cv2.imwrite(f'.\imageFile\postProcessImage\DJI_0{i}.png', rgb, [cv2.IMWRITE_PNG_COMPRESSION, 5]) # 압축률 0~9

# 결과값 저장하기___BMP파일
# cv2.imwrite(f'.\imageFile\postProcessImage\DJI_0{i}.bmp', rgb)

# 작성일 : 2023.4.10.
# 색상이 이상하게 나온다. RGB 컬러 변환으로 생기는 현상으로 생각됨. 푸르게 나옴
# 작성일 : 2023. 4. 11.
# cv2.cvtcolor()를 이용해서 BGR->RGB로 변환