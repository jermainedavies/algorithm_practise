def is_palindrome(str):
    if str[::-1] == str:
        return True
    return False

palindromes = ["redivider", "deified", "civic", "radar", "level", "rotor", "kayak", "reviver", "racecar", "madam", "refer"]
random = ["Boletus", "adversative", "chemotaxis", "prier", "thrust", "antistriker", "porirua", "dodecahedron"]

for i in palindromes:
    print(is_palindrome(i)) #All return True

for i in random:
    print(is_palindrome(i)) #All return False
