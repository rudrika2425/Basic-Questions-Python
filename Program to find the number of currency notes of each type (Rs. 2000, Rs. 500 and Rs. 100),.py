a=eval(input())
notes = (2000,500,200,100,50,20,10,5,2,1)

amount = int(input("Enter Amount to be paid : "))

for a in notes:
    count = amount//a
    print("Note Value : ", a,'\tnumber of notes ',count)
    amount = amount%a  
