sub1 = int(input("Enter first subject marks\n"))
sub2 = int(input("Enter second subject marks\n"))
sub3 = int(input("Enter third subject marks\n"))

if(sub1<33 or sub2<33 or sub3<33):
    print(" You are fail because you have scored less than 33% in atleast one of the subjects")
elif(sub1+sub2+sub3)/3 <40:
    print("You are fail due to total percentage being less than 40%")
else: 
    print("Congratulations! You have successfully passed the exam!")        