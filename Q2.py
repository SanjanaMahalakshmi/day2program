def romanToInt(s: str) -> int:
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0

    for char in s:
        value = roman_values[char]
        if value > prev_value:
            total += value - 2 * prev_value
        else:
            total += value
        prev_value = value

    return total

# Example 1:
s = "III"
print(romanToInt(s))

# Example 2:
s1 = "LVIII"
print(romanToInt(s1))

# Example 3:
s2 = "MCMXCIV"
print(romanToInt(s2))
