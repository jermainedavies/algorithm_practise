def is_substring(s,target):
    
    pos1 = 0
    pos2 = len(s)

    for i in range(len(target)-len(s)):
        if target[pos1:pos2] == s:
            return f"There was a matching substring at {pos1}, {pos2}"
        else:
            pos1 += 1
            pos2 += 1

    return "NOT A SUBSTRING"


print(is_substring("toast", "rrrrrrtoastyyyyy"))

# returns "There was a matching substring at 6, 11"
