from machine import Pin, I2C
import ustruct

class INA219(object):
    def __init__(self, i2c=None, scl=None, sda=None,Rsh=0.1,BRNG=1,PG=3,BADC=3,SADC=3,MODE=7, addr=64):
        if not scl:
            scl = Pin(5)
        if not sda:
            sda = Pin(4)
        # construct an I2C bus
        if not i2c:
            i2c = I2C(scl=scl, sda=sda, freq=100000)
        self.i2c = i2c
        
        self.Rsh = Rsh
        self.addr = addr
        
        #write cal
        calstr = bytearray(3)
        calstr[1] = ((BRNG&0x01)<<5)+((PG&0x03)<<3)+((BADC>>1)&0x07)
        calstr[2] = ((BADC&0x01)<<7)+((SADC&0x0F)<<3)+(MODE&0x07)
        self.i2c.writeto(self.addr, calstr)
        
    def readI(self):
        self.i2c.writeto(self.addr, '\1') #select Reg1 Shunt Voltage
        data = self.i2c.readfrom(self.addr, 2)
        data = ustruct.unpack('!h', data)[0]
        return data*self.Rsh #100uV/0.1Ω=1mA
    
    def readV(self):
        self.i2c.writeto(self.addr, '\2') #select Reg2 Bus Voltage
        data = self.i2c.readfrom(self.addr, 2)
        data = ustruct.unpack('!h', data)[0]
        return (data>>3)*4.0 #mV
    
    def read(self):
      return self.readI(), self.readV()
