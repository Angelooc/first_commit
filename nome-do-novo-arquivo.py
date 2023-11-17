def remove_duplicate(lst):
    seen = set()
    result = []
    
    for item in reversed(lst):
        if item not in seen:
            seen.add(item)
            result.insert(0, item)
            
    return result
