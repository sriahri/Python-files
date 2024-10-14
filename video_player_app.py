import cv2

capture = cv2.VideoCapture(
    "F://videos/videos/#AlaVaikunthapurramuloo_-_ButtaBomma_Full_Video_Song_(4K)__Allu_Arjun__Thaman_S__Armaan_Malik("
    "360p)(1).mp4")

if not capture.isOpened():
    print(' Error Opening the file!')

while capture.isOpened():
    ret, frame = capture.read()
    if ret:
        cv2.imshow(frame)
        if cv2.waitKey(0) & 0xFF == ord('q'):
            break
    else:
        break

capture.release()
cv2.destroyAllWindows()
