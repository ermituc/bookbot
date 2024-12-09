
#meine Version
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    count = count_characters(text)
    print(f"{num_words} words found in the document")
    print(f"{count}")


def get_num_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    count={}
    text=[c for c in text if c.isapha()]
    joined_text="".join(text)
    lower_case=joined_text.lower()
    for i in lower_case :
        if i in count:
            count[i] +=1
        else:
            count[i] =1
    return(count)



def get_book_text(path):
    with open(path) as f:
        return f.read()

#bootdev version

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print(chars_dict)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
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



main()
