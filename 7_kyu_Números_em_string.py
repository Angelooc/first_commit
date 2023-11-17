def solve(s):
    max_num =0
    current_num = ""
    
    for character in s:
        if character.isdigit():
            
                        current_num += character
        else:
            if current_num:
                max_num = max(max_num, int(current_num))
                current_num = ""
                
    if current_num:
        max_num = max(max_num, int(current_num))
        
    return max_num    
            
result = solve("gh12cdy695m1")
print(result)                