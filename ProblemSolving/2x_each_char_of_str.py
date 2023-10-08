def dbl_each_char_of_str(str1):
    s = ""
    new_str = map(lambda a: a+a, str1)
    for char in new_str:
        s = s + char
    print(s)

dbl_each_char_of_str("Hi-There")
