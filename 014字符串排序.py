count = int(input())
word_list = []
for _ in range(count):
    word_list.append(input())

word_sorted = sorted(word_list)
for word in word_sorted:
    print(word)
