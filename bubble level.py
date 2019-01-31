import microbit
import math

while True:
    x = microbit.accelerometer.get_x()
    y = microbit.accelerometer.get_y()
    z = microbit.accelerometer.get_z()


    def calculate_angle(x,y,z):
        a1 = math.atan2(x,math.sqrt((y ** 2) + (z ** 2)))
        print(math.degrees(a1))
        return math.degrees(a1)


    def bubble_display(x_angle,y_angle):
        if (x_angle <= math.degrees(10.0) and y_angle <= math.degrees(10.0)):
            microbit.display.show(microbit.Image.HEART)
        if (y_angle > 10.0):
            microbit.display.show(microbit.Image.ARROW_N)
        elif (x_angle < 0):
            microbit.display.show(microbit.Image.ARROW_W)


    x_angle = calculate_angle(x,y,z)
    y_angle = calculate_angle(y,x,z)
    print((x_angle,y_angle))
    bubble_display(x_angle,y_angle)
    microbit.sleep(200)

