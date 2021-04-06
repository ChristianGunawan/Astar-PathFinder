from read_input import *
from PathFinder import *
from graph import *

while True:
    a = treeDict
    listTempat = [nodes for nodes in a]
    # List nama tempat
    print("LIST NAMA TEMPAT")
    for i in listTempat:
        num = 1
        print(f"{num}. {i}")
        num += 1
    # Input tempat awal
    string_awal = str(input("Masukkan tempat awal : "))
    while(string_awal not in listTempat):
        print("Salah memasukkan nama tempat awal")
        string_awal = str(input("Masukkan tempat awal : "))
    # Input tempat akhir
    string_akhir = str(input("Masukkan tempat awal : "))
    while(string_akhir not in listTempat):
        print("Salah memasukkan nama tempat awal")
        string_akhir = str(input("Masukkan tempat awal : "))
    # Membentuk graph
    graphMaker(string_awal, string_akhir)
    break