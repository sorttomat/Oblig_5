infile = open("a_study_in_scarlet.txt","r")

lines = infile.readlines()
infile.close()

words = {}

for line in lines:
    word = line.strip("\n")
    if word not in words:
        words[word] = 1
    else:
        words[word] += 1

for key in sorted(words):
    print(key, words[key])