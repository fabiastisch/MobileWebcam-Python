import cv2
import numpy as np
import pyvirtualcam

url = 'https://10.27.203.2:8080/video'
video_stream = cv2.VideoCapture(url)

with pyvirtualcam.Camera(width=1920, height=1080, fps=30) as cam:
    print(f'Using virtual camera: {cam.device}')
    while True:
        x, frame = video_stream.read()


        cv2.imshow('smartphone', frame)

        cam.send(frame)
        cam.sleep_until_next_frame()

        if cv2.waitKey(1) & 0xFF == ord('q'):
            frame = np.zeros((cam.height, cam.width, 3), np.uint8)  # RGBA
            cam.send(frame)
            cam.sleep_until_next_frame()

            break

video_stream.release()
cv2.destroyAllWindows()
