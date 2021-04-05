import os
from collections import defaultdict
from os.path import dirname, abspath
    
def read_input():
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
    pathDict = defaultdict(dict)
    heuristicDict = dict()
    toParse = f.readlines()

    #Parsing nilai heurisitik
    toParseHeuristik = toParse[toParse.index("HEURISTIK\n") + 1:]
    for word in toParseHeuristik:
        heuristicParse = word.replace("\n", "").split(" ")
        heuristicDict[heuristicParse[0]] = int(heuristicParse[1])
    #Parsing nilai jalur 
    toParseJalur = toParse[:toParse.index("HEURISTIK\n")]
    for word in toParseJalur:
        wordParse = word.replace("\n", "").split(" ")
        # Jalur dianggap bisa 2 arah
        pathDict[wordParse[0]][wordParse[1]] = int(wordParse[2])
        pathDict[wordParse[1]][wordParse[0]] = int(wordParse[2])
    
    return pathDict, heuristicDict