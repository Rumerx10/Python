def is_end_same(str1, str2):
    x = slice(len(str1) - 3, len(str1))
    y = slice(len(str2) - 3, len(str2))

    if str1[x].lower() == str2[y].lower():
        print("True")
    else:
        print("False")


is_end_same("Hiabc", "abc")
is_end_same("AbC", "HiaBz")
is_end_same('abc', 'abXabc')
