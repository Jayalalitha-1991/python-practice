def remove(s):
    seen = set()
    result = ""
    for char in s:
        if char not in seen:
            seen.add(char)
            result += char
    return result

s = "aaabbbbcccdef"
print(remove(s))  # Output: "abcdef"
