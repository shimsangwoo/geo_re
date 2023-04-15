import cv2
cap = cv2.VideoCapture(0)

frameSize =(int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
            int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))

print('frameSize=', frameSize)

while True:

    reval, frame = cap.read()

    if not reval:
        break

    cv2.imshow('frame',frame)

    key = cv2.waitKey(25)
    if key == 27:     # 아래의 키번호를 참조
        break
if cap.isOpened():
    cap.release()
cv2.destroyAllWindows()


##### 다음은 컴퓨터 키보드에서 일반적으로 사용되는 일부 키에 대한 ASCII 코드입니다.
# 27 - 탈출(Esc) 키
# 8 - 백스페이스 키
# 9 - 탭 키
# 13 - 엔터 키
# 32 - 스페이스 키
# 48 ~ 57 - 숫자 키(0-9)
# 65 ~ 90 - 알파벳 키(A-Z)
# 91 ~ 93 - Windows 키
# 112 ~ 123 - 기능 키(F1-F12)