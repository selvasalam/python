def length(words):
    return max(len(word)for word in words)
word_list=input("enter list of words seperate  by space:").split()
print("length of longest word:",length(word_list))