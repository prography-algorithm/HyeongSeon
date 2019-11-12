import sys
read = lambda: sys.stdin.readline()
N = int(read())
words = set()
for _ in range(N):
    word = input()
    words.add(word)

words = sorted(words)
words = sorted(words, key=lambda word:len(word))

for word in words:
    print(word)

