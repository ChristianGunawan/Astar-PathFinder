import os
from collections import defaultdict
from os.path import dirname, abspath
    
# def read_input():
#     directory = dirname(abspath(__file__))
#     namafile = str(input("Masukkan nama file : "))
#     pathfile = os.path.join(directory, 'test\\' + namafile + '.txt')
#     f = open(pathfile,"r")

#     # Parsing The input
#     """
#     Input : Connection between places with distance, and heuristic values
#     Output : adjacency matrix and dictionary of heuristic values per places
#     Guide : Index 0 for pathDictionary index 1 for heuristic Dictionary
#     """
#     pathDict = defaultdict(dict)
#     heuristicDict = dict()
#     oneWayPathDict = defaultdict(dict)
#     toParse = f.readlines()

#     #Parsing nilai heurisitik
#     toParseHeuristik = toParse[toParse.index("HEURISTIK\n") + 1:]
#     for word in toParseHeuristik:
#         heuristicParse = word.replace("\n", "").split(" ")
#         heuristicDict[heuristicParse[0]] = int(heuristicParse[1])
#     #Parsing nilai jalur 
#     toParseJalur = toParse[:toParse.index("HEURISTIK\n")]
#     for word in toParseJalur:
#         wordParse = word.replace("\n", "").split(" ")
#         # Jalur dianggap bisa 2 arah
#         pathDict[wordParse[0]][wordParse[1]] = int(wordParse[2])
#         pathDict[wordParse[1]][wordParse[0]] = int(wordParse[2])
#         oneWayPathDict[wordParse[0]][wordParse[1]] = int(wordParse[2])
    
#     return pathDict, heuristicDict, oneWayPathDict

coordinateDict = defaultdict(dict)
def read_input2():
    directory = dirname(abspath(__file__))
    namafile = str(input("Masukkan nama file : "))
    pathfile = os.path.join(directory, 'test\\' + namafile + '.txt')
    f = open(pathfile,"r")

    # Parsing The input
    """
    Input : Connection between places with distance, and heuristic values
    Output : adjacency matrix and dictionary of heuristic values per places
    Guide : Index 0 for pathDictionary index 1 for heuristic Dictionary
    """
    weightDict = defaultdict(dict)
    
    # Mendapatkan jumlah nodes
    toParse = f.readline()
    jumlahNodes = int(toParse)

    # Mendapatkan list dari seluruh tempat, PENTING !
    parsedNodes = f.readline().replace("\n", "").split(" ")

    # Parsing koordinat
    toParse = f.readlines()
    koordinatParse = toParse[:toParse.index("MATRIKS\n")]
    for placeCoordinate in koordinatParse:
        parsed = placeCoordinate.replace("\n","").split(" ")
        coordinateDict[parsed[0]]["lat"] = int(parsed[1])
        coordinateDict[parsed[0]]["lng"] = int(parsed[2])

    # Parsing matriks
    MATRIKS = []
    matrixParse = toParse[toParse.index("MATRIKS\n") + 1:]
    for elem in matrixParse:
        elemParse = elem.replace("\n", "").split(" ")
        elemParse = list(map(int, elemParse))
        MATRIKS.append(elemParse)

    # Parsing bobot
    for parent in range(jumlahNodes):
        for children in range(jumlahNodes):
            if (MATRIKS[parent][children] == 1):
                weightDict[parsedNodes[parent]][parsedNodes[children]] = euclideanDistance(parsedNodes[parent], parsedNodes[children])
    return weightDict, coordinateDict

def euclideanDistance(start, end):
    powerDifLat = (coordinateDict[start]["lat"] - coordinateDict[end]["lat"])**2
    powerDifLng = (coordinateDict[start]["lng"] - coordinateDict[end]["lng"])**2
    return round((powerDifLat + powerDifLng) ** (1/2), 3)

