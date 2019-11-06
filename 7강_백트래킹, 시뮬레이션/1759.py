L, C = [int(x) for x in input().split()]
chars = sorted([x for x in input().split()])
vowels = ['a', 'e', 'i', 'o', 'u']

is_vowel_map = dict()
for char in chars:
    if char in vowels:
        is_vowel_map[char] = True
    else:
        is_vowel_map[char] = False
def check_is_vowel(char):
    return is_vowel_map[char]

MIN_VOWEL_COUNT = 1
MIN_CONSONANT_COUNT = 2
"""
a c i s t w
가지고 있는 모음의 개수 - 최소 모음 = required_vowels 
가지고 있는 자음의 개수 - 최소 자음 = required_consonants
빈 자리 개수 >= required_vowels + required_consonants 
"""
class Temp:
    def __init__(self):
        self._payload = ['' for _ in range(L)]
        self.vowel_count = 0
        self.consonant_count = 0
    def __repr__(self):
        return repr(self._payload)

    def __getitem__(self, key):
        return self._payload[key]
    
    def __delitem__(self, key):
        del self._payload[key]

    def __contains__(self, key):
        return key in self._payload

    def __setitem__(self, key, value):
        before = self._payload[key]
        if before != '':
            if check_is_vowel(before):
                self.vowel_count -= 1
            else:
                self.consonant_count -= 1
        self._payload[key] = value
        if check_is_vowel(value):
            self.vowel_count += 1
        else:
            self.consonant_count += 1
    def __str__(self):
        return ''.join(self._payload)
temp = Temp()


def solution(chars,l, c, start=0, depth=0):
    if depth == l:
        if temp.vowel_count >= MIN_VOWEL_COUNT and temp.consonant_count >= MIN_CONSONANT_COUNT:
            print(temp)
        return
    if start == c:
        return
    for x in range(start, c):
        temp[depth] = chars[x]
        solution(chars, l, c, x + 1, depth + 1)
solution(chars, L, C)
