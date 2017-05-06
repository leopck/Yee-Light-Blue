import pexpect
from subprocess import Popen, call
import time

class YeeLightBlue:
    
    def __init__(self, mac_str, device_no):
        self.connect(mac_str, device_no)
        pass
    
    def discover(self):
        # TODO: Some codes to use lescan to find the YeeLightBlue
        pass

    def connect(self, mac_str, device_no):
	call(['sudo', 'hciconfig', device_no, 'down'])
	call(['sudo', 'hciconfig', device_no, 'up'])
        call(['sudo', 'hcitool', '-i', device_no, 'lecc', mac_str])
        time.sleep(1)
        self.con = pexpect.spawn('sudo gatttool -i ' + device_no + ' -b ' + mac_str + ' -I')
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
        self.con.sendline('char-write-cmd 0x0025 2c2c2c302c2c2c2c2c2c2c2c2c2c2c2c2c2c')      

    def turnOn(self):
        self.con.sendline('char-write-cmd 0x0025 2c2c2c3130302c2c2c2c2c2c2c2c2c2c2c2c')
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

    def white(self,temperature,brightness):
        a_str = "CLTMP " + temperature + ',' + brightness + ','
        for letter in range(len(a_str),18):
            #print letter
            a_str += ','
            #print a_str
        self.str2hex(a_str)
	print a_str
        print self.hexStr
        self.con.sendline('char-write-cmd 0x0012 ' + self.hexStr)
