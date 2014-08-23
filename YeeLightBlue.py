import pexpect
from subprocess import Popen
import time

class YeeLightBlue:
    
    def __init__(self, mac_str):
        self.connect(mac_str)
        pass
    
    def discover(self):
        # TODO: Some codes to use lescan to find the YeeLightBlue
        pass

    def connect(self,mac_str):
        output = Popen(['sudo', 'hcitool', 'lecc', s_str])
        time.sleep(1)
        self.con = pexpect.spawn('sudo gatttool -b ' + s_str + ' -I')
        self.con.expect('\[LE\]>', timeout=600)
        self.con.sendline('connect')
        self.con.expect('\[LE\]>', timeout=600)
        #pass
    
    def disconnect(self):
        self.con.sendline('disconnect')
        self.con.expect('\[LE\]>', timeout=600)
        self.con.sendline('exit')
        #pass
    
    def turnOff(self):
        self.con.sendline('char-write-cmd 0x0025 ,,,0,,,,,,,,,,,,,,')      

    def turnOn(self):
        self.con.sendline('char-write-cmd 0x0025 ,,,100,,,,,,,,,,,,')
        #pass
        
    def str2hex(self, a_str):
        hexStr = ''
        for letter in a_str:
            hexStr += format(ord(letter), 'x')
        self.hexStr = hexStr

    def control(self, red, green, blue, brightness):
        a_str = red + ',' + green + ',' + blue + ',' + brightness + ','
        for letter in range(len(a_str),18):
            #print letter
            a_str += ','
            #print a_str
        self.str2hex(a_str)
        print self.hexStr
        self.con.sendline('char-write-cmd 0x0025 ' + self.hexStr)
    
    def delayON(self, time, status):
        '''TODO: Function is missing UUID/Handle'''
        '''Boolean checker'''
        if status > 1 or status < 0:
            print 'Values for status in delayON(time, status = BOOLEAN) must be in Boolean!'
            pass
        else :           
            a_str = str(time) + ',' + str(status) + ','
            for letter in range(len(a_str),8):
                #print letter
                a_str += ','
                #print a_str
            self.str2hex(a_str)
            print self.hexStr
            self.con.sendline('char-write-cmd 0x0025 ' + self.hexStr)

    def delayOnStatusQuery(self):
        '''TODO: Function is missing UUID/Handle'''
        self.con.sendline('char-write-cmd 0x00__ RT')



'''Enter your Mac Address inside the YeeLightBlue'''
x = YeeLightBlue("CD:B7:2E:58:0D:32")
'''Use control to change the RGB and brightness'''
x.control('255','0','0','100')
time.sleep(2)
x.control('0','255','0','100')
time.sleep(2)
x.control('0','0','255','100')
time.sleep(2)
'''Creates a delayed switch on time; delayON(time, 0 or 1);'''
'''Function not ready'''
#x.delayON(5,1)


#Disconnecting from the YeeLightBlue
x.disconnect()

