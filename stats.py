def count_words(text: str):
    list_of_words = text.split()
    return len(list_of_words)

def count_characters(text:str) -> dict:
    lowered_text = text.lower()
    letter_count = {}
    words = lowered_text.split()
    for word in words:
        for letter in word:
            if letter in letter_count.keys():
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
    return letter_count

def sort_characters(dict: dict) -> list:
    def sort_on(value):
        return value["count"]

    character_counts = []
    for key, value in dict.items():
        if not key.isalpha():
            continue
        char_obj = {}
        char_obj["char"] = key
        char_obj["count"] = value
        character_counts.append(char_obj)

    character_counts.sort(key=sort_on, reverse=True)
    return character_counts


