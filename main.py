def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_char_dict(text)
    freq_report = get_freq_report(chars_dict)
    book_report = get_book_report(freq_report)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    print(book_report)
    print("--- End Report ---")

def get_book_report(freq_report):
    report = []
    for i in freq_report:
        report.append(f"The '{i['char']}' character was found {i['freq']} times")
    return "\n".join(report)

def get_num_words(text):
    words = text.split()
    return len(words)

def get_freq_report(chars_dict):
    dict_list = []
    for char in chars_dict:
        if char.isalpha():
            dict_list.append({"char": char, "freq": chars_dict[char]})
    dict_list.sort(reverse= True, key= lambda dict_list: dict_list["freq"])
    return dict_list

def get_char_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
main()