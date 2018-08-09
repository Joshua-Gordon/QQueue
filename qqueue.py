from playsound import playsound
from glob import glob
import pyquil
from pyquil.parser import parse_program
from pyquil.api import QVMConnection
import os
from math import log, ceil

topdir = os.path.dirname(os.path.realpath(__file__))

def getFileList():
    files = glob(topdir+"\\*.mp3")
    return files

def getRandomNum(num):
    q = QVMConnection()
    s = "".join(["H " + str(i) + "\n" for i in range(num)])
    s += "".join(["MEASURE " + str(i) + " [" + str(i) + "]\n" for i in range(num)])
    #print(s)
    p = parse_program(s)
    res = None
    try:
        res = str(q.wavefunction(p).amplitudes)[1:-1].split(" ").index("1.+0.j")
    except:
        print(q.wavefunction(p).amplitudes)
        return -1
    return res
    
def quantumShuffle(files):
    shuffled = []
    while len(files) > 0:
        num = len(files)
        numlog = ceil(log(num)/log(2))
        rand = num
        while rand >= num:
            rand = getRandomNum(numlog)
        shuffled.append(files[rand])
        files.remove(files[rand])
        print(shuffled)
    return shuffled

def playFiles(files):
    for f in files:
        playsound(f)

if __name__ == "__main__":
    files = getFileList()
    shuffled = quantumShuffle(files)
    playFiles(shuffled)
