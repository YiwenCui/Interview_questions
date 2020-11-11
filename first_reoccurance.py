def find_first_reoccurance(string):
    n=[ ]
    for char in string:
        if n==[ ] or char not in n:
            n.append(char)
        
        else:
            return char

print(find_first_reoccurance("DBCABA"))
    