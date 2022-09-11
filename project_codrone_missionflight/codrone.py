from codrone_edu.drone import *
import time
drone = Drone()
drone.pair()
dataset = "color_data"
colors = ["green", "purple", "red", "lightblue", "blue", "yellow", "black", "white"]
for color in colors:
    data = []
    samples = 500
    for i in range(1):
        print("샘플: ", i+1)
        next = input("다음 색상을 보정하려면 Enter 키를 누르세요 " + color)
        print("0% ", end="")
        for j in range(samples):
            color_data = drone.get_color_data()[0:9]
            data.append(color_data)
            time.sleep(0.005)
            if j % 10 == 0:
                print("-", end="")
        print(" 100%")
    drone.new_color_data(color, data, dataset)
print("보정이 완료되었습니다.")