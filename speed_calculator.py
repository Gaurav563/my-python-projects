from time import *
import random as r


def mistake( parm ,user):
    error = 0
    for i in range(len(parm)):
        try:
            if parm[i] != user[i]:
                error =+1
        except :
            error = error+1
    return error

def speed_times(time_s ,time_e,userinput):
    time_delay = time_e -time_s
    time_R = round(time_delay)
    speed = len(userinput)/time_R
    return round(speed)


test=[ " this is nothing a","s nothing asdns jdjsdhjklahjj,,","erkkerrddssa fkjsdjala"]
test2 = r.choice(test)
print('**** typing speed *****')
print(test2)

print()
time_1= time()
testinput = input(" Enter : ")
time_2 = time()

print('Speed : ', speed_times(time_1,time_2,testinput),'w/sec')
print('error,:',mistake(test2,testinput))