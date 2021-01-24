def half_is_copy(str):
    if len(str) % 2 != 0:
        return False

    if str[::-1] == str:
        return True

print(half_is_copy("ABCDDCBA")) #True
print(half_is_copy("ABCDCBA")) #False
