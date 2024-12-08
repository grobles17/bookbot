def number_words(book: str)->int:
    """Counts the number of words in a given str input. Returns an int"""
    return len(book.split())

def get_book_text(path: str) -> str:
    """Gets a file path, extracts the text of the file and returns it."""
    #Open the file with a with statement so it closes automatically
    with open(path) as f:
        file_content = f.read()
    return file_content

def count_characters(text: str) -> dict[str:int]:
    """Counts how many times each character appears, returning a dict str:int. Case insensitive"""
    letter_count: dict = {}
    for letter in text.lower():
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count

def sort_on_num(dict):
    """Returns the value of the key "num" in a dictionary"""
    return dict["num"] #Used on sort() method in sort_dict()

def sort_dict(dictionary: dict) ->list[dict]:
    """Gets a dict of letters:number of ocurrences and returns a sorted list of dictionaries form most common to least"""
    new_list: list = []
    for key, num in dictionary.items():
        if key.isalpha():
            temp_dict = {"char":key, "num":num}
            new_list.append(temp_dict)
    new_list.sort(reverse=True, key=sort_on_num)
    return new_list


def main():
    file_path: str = fr"books/frankenstein.txt"
    file_content: str = get_book_text(file_path)
    words: int = number_words(file_content)
    letter_count: dict = count_characters(file_content)
    sorted_letter_count: list[dict] = sort_dict(letter_count)
    print(sorted_letter_count)
    print(f"--- Begin report of {file_path} ---")
    print(f"{words} words where found in the document")
    print()
    for letter_dict in sorted_letter_count:
        print(fr"The {letter_dict['char']} character was found {letter_dict['num']} times")
    print(f"--- End of report ---")

main()
