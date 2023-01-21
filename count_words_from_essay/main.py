

def count_words():
    with open("essay", "r") as file:
        data = file.read()
        words = data.split()
        print("The essay has", len(words), "words.")


if __name__ == '__main__':
    count_words()
