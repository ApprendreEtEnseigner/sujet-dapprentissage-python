
def solution(s):
    if len(s) % 2 != 0:
        s += '_' 
    split = []
    
    for i  in range(0, len(s), 2):
            split.append(s[i:i+2])
    return split
            
    