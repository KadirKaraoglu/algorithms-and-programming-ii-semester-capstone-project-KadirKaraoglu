def bad_char_heuristic(pattern):
    bad_char = {}
    for i in range(len(pattern)):
        bad_char[pattern[i]] = i
    return bad_char


def good_suffix_heuristic(pattern):
    
    m = len(pattern)
    border_array = [0] * (m + 1)
    shift = [0] * (m + 1)


    i = m
    j = m + 1
    border_array[i] = j
    while i > 0:
        while j <= m and pattern[i - 1] != pattern[j - 1]:
            if shift[j] == 0:
                shift[j] = j - i  
            j = border_array[j]
        i -= 1
        j -= 1
        border_array[i] = j

    
    for i in range(m + 1):
        if shift[i] == 0:
            shift[i] = j - i 
    
   
    for i in range(m - 1):
        if shift[i+1] == 0:
            shift[i+1] = m - border_array[i+1]
    
    return shift, border_array

def boyer_moore_search(text, pattern):
    """
    Searches for all occurrences of a pattern within a text using the Boyer-Moore algorithm.
    Returns a list of starting indices where the pattern is found.
    """
    n = len(text)
    m = len(pattern)

    if m == 0:
        return [i for i in range(n + 1)] 

    if m > n:
        return [] 

    bad_char = bad_char_heuristic(pattern)
    good_suffix_shift, border_array = good_suffix_heuristic(pattern)

    
    s = 0  
    found_indices = []

    while s <= (n - m):
        j = m - 1 

       
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1

        
        if j < 0:
            found_indices.append(s)
            
            s += good_suffix_shift[0] 

        else:
          
            bad_char_shift = j - bad_char.get(text[s + j], -1)

            
            good_suffix_shift_val = good_suffix_shift[j + 1]

            
            s += max(bad_char_shift, good_suffix_shift_val)
            
    return found_indices

