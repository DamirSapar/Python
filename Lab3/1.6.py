def reverse_words(sent):
    words = sent.split() 
    rev_words = words[::-1] 
    return "" .join(rev_words)  


St = input()
print(reverse_words(St))