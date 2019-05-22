#보이어-무어 알고리즘
#패턴의 뒷부분에 대응되는 텍스트 문자를 이용해 텍스트를 보지 않고도 뛰어넘을 수 있게 한다. 
#이론적으로는 최악의 경우 O(mn)의 시간이 소요되지만, 평균적으로는 가장 좋은 성능을 보여 현장에서 애용됨.

def make_bad_match_table(pattern):

    length = len(pattern)
    table = {}
    for i, c in enumerate(pattern):
        if i == length-1 and not c in table:
            table[c] = length
        else:
            table[c] = length - i - 1

    return table


def boyer_moore(pattern, text):

    match_table = []
    pattern_length = len(pattern)
    text_length = len(text)
    if pattern_length > text_length:
        return match_table

    table = make_bad_match_table(pattern)
    index = pattern_length - 1
    pattern_index = pattern_length - 1

    while index < text_length:
        if pattern[pattern_index] == text[index]:
            if pattern_index == 0:
                match_table.append(index)
                pattern_index = pattern_length - 1
                index += (pattern_length * 2 - 1)
            else:
                pattern_index -= 1
                index -= 1
        else:
            index += table.get(text[index], pattern_length)
            pattern_index = pattern_length - 1

    return match_table

if __name__ == '__main__':
    A = "AABAACAADAABAAABAA"
    P = "AABA"
    bm = boyer_moore(P, A)
    print(A)
    for i in bm:
        print("{0}{1}".format(" "*i, P))