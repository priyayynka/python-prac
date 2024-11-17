def remove_and_split(string,word):
    newStr = string.replace(word, "")
    return newStr.strip()

this = "    Piyu is a good girl    "
n = remove_and_split(this, "Piyu")
print(n)    