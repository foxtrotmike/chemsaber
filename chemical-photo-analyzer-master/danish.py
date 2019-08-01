import serial
import time
import numpy as np
import serial.tools.list_ports
import random

def writeRGB(x,y,z):
        RGBvalue = x,y,z          
        setRGB = str(RGBvalue)
        ard.write(setRGB.encode())
def readVoltage():
    ard.flush()
    time.sleep(0.2)
    a = ard.readline()
    return a    
    
def RW(x,y,z):
    writeRGB(x,y,z)
    time.sleep(0.1)
    return readVoltage()

def sample(R=None):
    if R is None:
        R = [[255,0,0],[0,255,0],[0,0,255],[255,255,255]]
    Z = []
    rr = None
    RW(0,0,0)
    for x,y,z in R:        
        for _ in range(2): #set value and read twice, keep second reading only
            r = RW(x,y,z)
            try:
                rr = list(np.array(np.array(r.strip().split())[[1,3,5,9,10,11,12,16,17,18,19]],dtype=np.int))                
            except Exception as e:
                print(e)
        print(rr)
        if rr is not None:
            Z.append(rr)
    RW(0,0,0)
    Z = np.array(Z)
    
    Z = Z[:,[0,1,2,5,6,9,10]]
    rgb = Z[:,[0,1,2]]
    s1 = np.mean(Z[:,3:4],axis=1)
    s2 = np.mean(Z[:,5:6],axis=1)
    ZR = np.hstack((rgb,np.atleast_2d(s1).T,np.atleast_2d(s2).T))
    return Z

if __name__=='__main__':
    # code for automatic discovery and connection. 
    try:
        ard
    except NameError:
        port = 'COM20'
        ports = list(serial.tools.list_ports.comports())
        for p in ports:
            if 'CH340' in p.description or 'arduino' in p.description.lower():
                port = p.device
                ard = serial.Serial(port,9600,timeout=1)
                print("Device Connected on %s."%(port))
                print("Initiating Startup Sequence (0RGBW0). Standby!")
                time.sleep(2)
                sample()
                time.sleep(1)
                print("Startup Sequence Completed. Ready!")
                break    
        else:
            raise Exception("Device not found!")

    

    sample_name = "methyl_alcohol"
    
    seeds = [7,random.randrange(2**32-1)]
    for seed in seeds:
        np.random.seed(seed)
        R = np.random.randint(0,255,size=(50,3))#[[0,0,0],[0,0,255],[0,255,0],[0,255,255],[255,0,0],[255,0,255],[255,255,0],[255,255,255]]
        ZR = sample(R)
        fname = sample_name+"#"+str(seed)+".spv"
        np.savetxt(fname,ZR,fmt="%d")
        print(fname+" Saved.")