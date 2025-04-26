def is_palindrome_permutation(word):
    hash_table = {}
    for char in word:
        if char not in hash_table:
            hash_table[char] = 1
        else:
            hash_table[char] += 1
            
    
    print(hash_table)   
    counter = 0
    for char in word:
        if hash_table[char] % 2 != 0:
            counter += 1
    if counter == 1 or counter == 0:
        return True 
    return False



    print(hash_table)
print(is_palindrome_permutation("loole"))