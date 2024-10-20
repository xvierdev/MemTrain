class gamefunc ():
    def __init__(self) -> None:
        pass

    def open_word_list(self):
        with open('words.txt', 'r') as wordlist:
            db_words = wordlist
            print(db_words)
