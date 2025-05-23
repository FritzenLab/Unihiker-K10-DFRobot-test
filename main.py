from unihiker_k10 import button,temp_humi,light,rgb,screen,acce,camera
import time

sequence= 0
screen.init(dir=2)
screen.show_bg(color=0xFFFFFF)
screen.clear()

camera.init()#Init camera

#Display the camera image onto the screen
screen.show_camera(camera)

bt_a=button(button.a)#Init button A
bt_b=button(button.b)#Init button B

statusa= 0
statusb= 0

while True:
    
    #Read (temp ℃/temp ℉/humi)
    print(temp_humi.read_temp())#℃
    print(temp_humi.read_temp_f())#℉
    print(temp_humi.read_humi())
    print(light.read())
    
    if(sequence == 1):
        rgb.write(num = 0,color=0x0000FF)
        rgb.write(num = 1,color=0x00FF00)
        rgb.write(num = 2,color=0xFF0000)
    elif(sequence == 2):
        rgb.write(num = 0,color=0x00FF00)
        rgb.write(num = 1,color=0xFF0000)
        rgb.write(num = 2,color=0x0000FF)
    else:
        rgb.write(num = 0,color=0xFF0000)
        rgb.write(num = 1,color=0x0000FF)
        rgb.write(num = 2,color=0x00FF00)
        sequence= 0
    sequence= sequence + 1
    
    screen.draw_text(text="Temp=" + str(temp_humi.read_temp())+ " oC",line=1, font_size=30,color=0xFF0000)
    screen.draw_text(text=" Humi=" + str(temp_humi.read_humi())+ " %RH",line=2, font_size=30,color=0xFF0000)
    screen.draw_text(text="Light=" + str(light.read())+ " Lux",line=3, font_size=30,color=0xFF0000)
    
    screen.draw_text(text="ax=" + str(acce.read_x()*10),line=5, font_size=30,color=0x5500AA)
    screen.draw_text(text="ay=" + str(acce.read_y()*10),line=6, font_size=30,color=0x5500AA)
    screen.draw_text(text="az=" + str(acce.read_z()*10),line=7, font_size=30,color=0x5500AA)
    
    screen.draw_text(text="Button 1=" + str(bt_a.status()),line=9, font_size=30,color=0x00AA00)
    screen.draw_text(text="Button 2=" + str(bt_b.status()),line=10, font_size=30,color=0x00CC00)
    screen.show_draw()
    time.sleep(0.1)
    pass