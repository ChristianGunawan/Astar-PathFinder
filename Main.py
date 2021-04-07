from read_input import *
from PathFinder import *
from graph import *

status = True
while status:
    a = treeDict
    listTempat = [nodes for nodes in a]
    # List nama tempat
    print("LIST NAMA TEMPAT")
    num = 1
    for i in listTempat:
        print(f"{num}. {i}")
        num += 1
    # Input tempat awal
    string_awal = str(input("Masukkan tempat awal : "))
    while(string_awal not in listTempat):
        print("Salah memasukkan nama tempat awal")
        string_awal = str(input("Masukkan tempat awal : "))
    # Input tempat akhir
    string_akhir = str(input("Masukkan tempat akhir : "))
    while(string_akhir not in listTempat):
        print("Salah memasukkan nama tempat akhir")
        string_akhir = str(input("Masukkan tempat awal : "))
    # Membentuk graph
    graphMaker(string_awal, string_akhir)
    
    repeat = str(input("Mau mencoba dengan test-case lain ? : (Y/N): "))
    if(repeat == 'Y' or status == 'y'):
        a = treeDict
    elif(repeat =="N" or repeat == "n"):
        status = False