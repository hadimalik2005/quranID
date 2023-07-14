import pickle
import Levenshtein

def findBestMatchingVerse(transcribedVerse, nestedList):
    bestDistance = float('inf')
    bestMatchSurah = None
    bestMatchVerse = None
    bestMatchIndex = None

    for surahIndex, surah in enumerate(nestedList):
        for verseIndex, verseText in enumerate(surah):
            distance = Levenshtein.distance(transcribedVerse, verseText)

            if distance < bestDistance:
                bestDistance = distance
                bestMatchSurah = surah[0]
                bestMatchVerse = verseText
                bestMatchIndex = (surahIndex + 1, verseIndex + 1) 

    return bestMatchSurah, bestMatchVerse, bestMatchIndex

with open("nestedListSave.pkl", "rb") as file:
    nestedList = pickle.load(file)

with open("transcriptsSave.pkl", "rb") as file:
    transcribedVerse = pickle.load(file)[0]

with open("surahs.pkl", "rb") as file:
    surahs = pickle.load(file)

reversedTranscribedVerse = transcribedVerse[::-1]

def main():
    bestMatchSurah, bestMatchVerse, bestMatchIndex = findBestMatchingVerse(reversedTranscribedVerse, nestedList)
    print(f"Surah: {bestMatchSurah}, Verse: {bestMatchVerse}")
    print(f"Verse index: Surah {bestMatchIndex[0]} ({surahs[bestMatchIndex[0]-1]}) - Verse {bestMatchIndex[1]}")

if __name__ == "__main__":
    main()

