import pickle

def loadQuranTextFile(filePath):
    with open(filePath, "r", encoding="utf-8") as file:
        lines = file.readlines()

    verses = []
    currentSurah = None

    for line in lines:
        parts = line.strip().split("|")
        if len(parts) >= 2:
            surahNumber = parts[0]
            verseText = "|".join(parts[1:]).strip().replace("|", "")
            verses.append((surahNumber, verseText))

    return verses


def createNestedList(verses):
    nestedList = []
    currentSurah = None
    surahVerses = []

    for verse in verses:
        surahNumber, verseText = verse

        if currentSurah is None:
            currentSurah = surahNumber

        if surahNumber != currentSurah:
            nestedList.append(surahVerses)
            surahVerses = []
            currentSurah = surahNumber

        surahVerses.append(verseText)

    if surahVerses:
        nestedList.append(surahVerses)

    return nestedList

def main():
    quranTextFile = "fullQuran.txt"
    quranVerses = loadQuranTextFile(quranTextFile)
    nestedList = createNestedList(quranVerses)

    with open("nestedListSave.pkl", "wb") as file:
        pickle.dump(nestedList, file)


if __name__ == "__main__":
    main()
