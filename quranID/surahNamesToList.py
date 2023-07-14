import pickle

inputFile = "surahNames.txt"

outputFile = "surahs.pkl"

with open(inputFile, "r") as file:
    surahs = [line.strip() for line in file]

with open(outputFile, "wb") as file:
    pickle.dump(surahs, file)
