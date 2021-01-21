import time
import activateCamera as ct
    wait = [0, 0, 255]
    go = [0, 255, 0]
    red = [255, 0, 0]

    basePath = "test/image_{Y}_{X}.png"
    waitTime = int(input("Enter wait time (in sec): "))
    num = int(input("Number of images to take: "))
for i in range(num):
        time.sleep(waitTime)
        time.sleep(2)
        ct.takePic(basePath.format(Y="L", X=(i+1)))