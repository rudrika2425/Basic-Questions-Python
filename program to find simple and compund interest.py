principle=int(input("enter principle amount"))
rate_of_interest=int(input("enter rate of inters"))
time=int(input("enter time"))
n=int(input("enter Compounding Frequency Per Annum"))
simple_interest=(principle*rate_of_interest*time)/100
compound_interest=(principle*(1+(rate_of_interest/n)**(n*time))-principle)
print("total amount is:",compound_interest)
print("simple interest is:",simple_interest)
