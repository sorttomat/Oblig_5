infile = open("a_study_in_scarlet.txt","r")

lines = infile.readlines()
infile.close()

class Word:
    def __init__(self, word):
        self.word = word
        self.count = 0

    def increaseCount(self):
        self.count += 1
    
    def getWord(self):
        return self.word

    def getCount(self):
        return self.count



words = []

for line in lines:
    word = line.strip("\n")
    for obj in words:
        if obj.getWord() == word:
            obj.increaseCount()
            print(obj.getCount())
    else:
        print(word)
        words.append(Word(word))
    




print(words)
