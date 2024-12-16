def main():
    word_count = 0
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        word_count += len(words)
        print(file_contents)
    print(word_count)

main()