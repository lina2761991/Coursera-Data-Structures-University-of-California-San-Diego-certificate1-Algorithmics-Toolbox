
n, W = [int(i) for i in input().split()] # the number n of compounds and W is the weight of backpack
lst = []

if W == 0:
    print(0)
    quit()

for _ in range(n):
    v, w = [int(i) for i in input().split()] # we r gonna input the weight of each element and its price 
    if v == 0:      
        continue
    lst.append((v, w)) # we fill the price and quantity of elements in the empty list ,we append them to each other 

lst.sort(key = lambda x: x[0]/x[1], reverse = True)  # we used list comprehension cuz we created a list out of another list 
#we r gonna sort the elements so f lst and divide the first /last in a reversed order ( from max to min)
# for example 100 50 , each kilo costs 100/50 = 2
# we sort the prices of kilos per element in descendding order


total_value = 0

for v,w in lst:
    if W == 0:
        print(total_value)
        quit()

    subsw = min(W,w) # the amount we got substract shouldnt exceed W neither w
    unitprice = v/w #  price per kg 
    W  = W - subsw # the remaining weight in each loop
    total_value = total_value + (unitprice*subsw)

print(total_value)