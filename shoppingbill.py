n=int(input('enter number of product:'))
list={}
total=0
total_of_each=0
for i in range(n):
    name=input('enter name of product:')
    quantity=int(input('enter quantity:'))
    price=int(input('enter price of prouct:'))
    list[name]={
        "quantity":quantity,
        "price":price
    }
    total=total+price*quantity




print("Total amount is ",total)
if total>=5000:
    after=total-(total/10)
print("10% discoun")
print("Final amount is ",after)