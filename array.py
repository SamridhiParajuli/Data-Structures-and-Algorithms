"""
Let us say your expense for every month are listed below,
January - 2200
February - 2350
March - 2600
April - 2130
May - 2190

1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this



"""
#1. In Feb, how many dollars you spent extra compare to January?
Month = [2200,2350,2600,2130,2190]
Extra = Month[1] - Month [0]
print(Extra)

#2. Find out your total expense in first quarter (first three months) of the year.

sum = Month[0]+Month[1]+Month[2]
print(sum)

#3. Find out if you spent exactly 2000 dollars in any month
for i in range (len(Month)):
    if Month[i] ==2000:
        print("yes")
        
    else:
        print("no")
        break

#June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list

Month.append(1980)
print(Month)

#5. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this

Month[3] = Month[3] - 200
print(Month)