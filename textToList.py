def load_quran_text_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    verses = []
    current_surah = None

    for line in lines:
        parts = line.strip().split("|")
        if len(parts) >= 2:
            surah_number = parts[0]
            verse_text = "|".join(parts[1:]).strip().replace("|", "")
            verses.append((surah_number, verse_text))
            current_surah = surah_number

    return verses


def create_nested_list(verses):
    nested_list = []
    current_surah = None
    surah_verses = []

    for verse in verses:
        surah_number, verse_text = verse

        if surah_number != current_surah:
            if surah_verses:
                nested_list.append(surah_verses)
            surah_verses = []
            current_surah = surah_number

        surah_verses.append(verse_text)

    if surah_verses:
        nested_list.append(surah_verses)

    return nested_list


def main():
    quran_text_file = "fullQuran.txt"
    quran_verses = load_quran_text_file(quran_text_file)
    nested_list = create_nested_list(quran_verses)

    # Print the nested list
    for surah in nested_list:
        print(surah)

if __name__ == "__main__":
    main()
