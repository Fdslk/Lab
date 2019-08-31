#coding=utf-8
class match():
    def __init__(self):
        pass
    def match(self, *params):
        str1 = params[0]
        str2 = params[1]
        for i in range(len(str1)):
            if str1[i] == str2[0]:
                if(len(str1) - i + 1 > len(str2)):
                    for j in range(len(str2)):
                        if str1[i + j] != str2[j]:
                            j -= 1
                            break
                    if j + 1 == len(str2):
                        return i
                else:
                    return  -1
    def KMP_match(self, *params):
        str1 = params[0]
        str2 = params[1]

    def get_next(self, *params):
        matchedStr = params[0]
        Tlen = 0
        n = len(matchedStr) - 1
        for i in range(len(matchedStr)):
            if(i != len(matchedStr) - 1):
                if(matchedStr[:i + 1] == matchedStr[n - i:]):
                    if(len(matchedStr[:i+1])) > Tlen:
                        Tlen = len(matchedStr[:i+1])
        return Tlen


if __name__ == "__main__":
    m = match()
    # str1 = raw_input()
    # str2 = raw_input()
    # print(m.match(str1, str2))
    str1 = raw_input()
    print(m.get_next(str1))