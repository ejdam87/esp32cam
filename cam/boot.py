
import camera

camera.init(0)
buf = camera.capture()
with open("photo.jpg", "wb") as f:
    f.write(buf)

with open("photo.jpg", "rb") as f:
    print(f.read() == buf)
