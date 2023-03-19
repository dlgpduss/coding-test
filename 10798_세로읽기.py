word = []
for i in range(5):
    a = input()
    word.append(a)

words = []

for j in range(15):
    for i in range(5):
        if j < len(word[i]):
            print(word[i][j])

print("".join(words))