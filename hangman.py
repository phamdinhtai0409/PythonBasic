import random

class HangMan(object):
    words = "ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion".split()
    def randomWord(self):
        return self.words[random.randint(0, len(self.words)-1)]

    def inputWord(self, word, result):
        char = input()
        if char == None or len(char) != 1:
            return None, False
        i, count = 0, 0
        check = char in word
        for c in word:
            if c == char:
                result[i] = c
                count += 1
            i += 1
        return char, check, count

    def start(self):
        print("Hangman Game !!!")
        word = list(self.randomWord())
        result = list('*' * len(word))
        print(word)
        print("Tu khoa gom co {0} chu cai: {1}".format(len(word), " ".join(result)))
        winner, i, missed = False, 0, []
        while i < 5:
            print("Moi ban doan 1 chu cai: ", end='')
            char, check, count = self.inputWord(word, result)
            if char == None:
                print("Chi duoc nhap 1 ky tu duy nhat")
                continue
            if result == word:
                print("Chuc mung ban da doan dung tu khoa", ''.join(word))
                winner = True
                break
            if not check:
                print("Khong co ky tu {} nao trong tu khoa".format(char))
                missed.append(char)
                i += 1
                print("Cac tu sai:", missed)
            else:
                print("Chung ta co {0} chu {1} trong tu khoa".format(count, char))
                print(' '.join(result))
        if not winner:
            print("Tu khoa cua game la: " + ''.join(word))


HangMan().start()
