# write a program to where a shop give discount 30% above buying 3000 ruppess and 
# give 20% discount above 2000 ruppess and give 10% discount above 1000 ruppess 
# and give no discount by less than 1000 ruppess

amount = int(input("Enter your amount : "))

if amount > 999 :
    if(amount < 2000) :
        dis = (amount * 10) / 100
        finally_price = amount - dis
        print("After discount 10% your final_amount is : ", finally_price)
    elif(amount < 3000):
        dis = (amount * 20) / 100
        finally_price = amount - dis
        print("After discount 20% your final_amount is : ", finally_price)
    else : 
        dis = (amount * 30) / 100
        finally_price = amount - dis
        print("After discount 30% your final_amount is : ", finally_price)
else :
    print("you have no any discount.")