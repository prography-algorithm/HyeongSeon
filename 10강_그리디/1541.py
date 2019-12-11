question = input()
result = 0
tokens = question.split('-')
result += sum([int(x) for x in tokens[0].split('+')])
for token in tokens[1:]:
    result -= sum([int(x) for x in token.split('+')])

print(result)