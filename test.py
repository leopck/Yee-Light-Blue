import yeelightblue
import time

'''Enter your Mac Address & USB device inside the YeeLightBlue'''
x = yeelightblue.YeeLightBlue("00:17:EA:91:03:86", "hci1")
'''Use control to change the RGB and brightness'''
x.control('255','0','0','100')
time.sleep(2)
x.control('0','255','0','100')
time.sleep(2)
x.control('0','0','255','100')
time.sleep(2)
x.control('255', '255', '255', '50')
time.sleep(2)
x.turnOff()
time.sleep(2)
x.turnOn()
'''Creates a delayed switch on time; delayON(time, 0 or 1);'''
'''Function not ready'''
#x.delayON(5,1)


#Disconnecting from the YeeLightBlue
x.disconnect()
