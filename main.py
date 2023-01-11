year = int(input("Which year do you want to check? "))

#first we check if the year is divisible by 4
if year % 4 == 0:
    #if the year is divisible by 4, we check if it is divisible by 100
    if year % 100 == 0:
        #if it is divisible by 100, we check if it is divisible by 400
        if year % 400 == 0:
            #if it is divisible by 400 then is a leap year
            print("Leap year.")
        else:
            #if is not divisible by 400 then it is not a leap year
            print("Not leap year.")
    else:
        #if it is not divisible by 100 then it is a leap year
        print("Leap year.")
else:
    #if it is not divisible by 4 then it is not a leap year
    print("Not leap year.")
    