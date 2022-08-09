def balancestr(string: str) -> bool:
    if string is None or len(string) < 2:
        return False
    if len(string) == 2 and string[0] != string[1]:
        return False
    head = 0
    tail = len(string) - 1
    while head != tail and head < len(string):
        if string[head] != string[tail]:
            return False
        head += 1
        tail -= 1
    return True


print("a是否回文字符串：%s" % balancestr("a"))
print("aa是否回文字符串：%s" % balancestr("aa"))
print("level是否回文字符串：%s" % balancestr("level"))
print("madam是否回文字符串：%s" % balancestr("madam"))
