from collections import defaultdict
import os
from os.path import dirname, abspath
nestedDict = defaultdict(dict)

nestedDict['A']['A'] = 1
nestedDict['A']['B'] = 1
nestedDict['A']['C'] = 1
nestedDict['B']['A'] = 1
nestedDict['B']['B'] = 1
nestedDict['B']['C'] = 1
nestedDict['C']['A'] = 1
nestedDict['C']['N'] = 5


for edge in nestedDict:
    for friend in nestedDict[edge]:
        print(nestedDict[edge][friend], end = ' ')
    print()
    
def read_input():
    directory = dirname(dirname(abspath(__file__)))
    namafile = str(input("Masukkan nama file : "))
    pathfile = os.path.join(directory, 'test\\' + namafile)
    f = open(pathfile,"r")
    return True

if __name__ == "__main__":
    read_input()