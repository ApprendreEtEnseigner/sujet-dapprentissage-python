
def are_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False
    freq1 = {}
    freq2 = {}
    
    for char in s1:
        if char in freq1:
            freq1[char] += 1
        else:
            freq1[char] = 1 
    
    for char in s2:
        if char in freq2:
            freq2[char] += 1
        else:
            freq2[char] = 1 
            
    
    for key in freq1:
        if key not in freq2 or freq1[key] != freq2[key]:
            return False
            
    return True

print(are_anagrams('nameless', 'salesmen'))
print(are_anagrams('chien', 'niche')) # doit afficher True
print(are_anagrams('python', 'typhon')) # doit afficher True
print(are_anagrams('bonjour', 'bonsoir')) # doit afficher False
