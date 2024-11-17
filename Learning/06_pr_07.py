text = input("Enter the text\n")

if("piyu" in text):
    spam = True
elif("Piyu" in text):
    spam = True
elif("PIyu" in text):
    spam = True
elif("PIYu" in text):
    spam = True
elif("PIYU" in text):
    spam = True
elif("PiYU" in text):
    spam = True  
elif("PiyU" in text):
    spam = True 
elif("PiYu" in text):
    spam = True     
elif("pIyu" in text):
    spam = True
elif("pIYu" in text):
    spam = True    
elif("pIYU" in text):
    spam = True
elif("piYu" in text):
    spam = True
elif("piYU" in text):
    spam = True
elif("piyU" in text):
    spam = True      
else:
    spam = False

if(spam):
    print("This text is talking about Piyu")
else:
    print("This text is not talking about Piyu")
