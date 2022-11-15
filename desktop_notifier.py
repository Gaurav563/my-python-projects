from plyer import notification
import time 


if __name__ == '__main__':
    while True:
         notification.notify(
             title ='**** Take Rest ****',
            message= "scan the code .............................",
            # app_icon='you can provide iamge
            # '
            timeout = 5
         )
         time.sleep(60*60)

