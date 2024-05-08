def longest_common_prefix(strs):
    if not strs:
        return ""
    
    prefix = strs[0]
    for string in strs[1:]:
        while string[:len(prefix)] != prefix:
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

# Example 1:
strs = ["flower", "flow", "flight"]
print(longest_common_prefix(strs))

# Example 2:
strs1 = ["dog", "racecar", "car"]
print(longest_common_prefix(strs1)) 
