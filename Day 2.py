## string formatting
price1=45000
price2=5000
price3=85000

## Method1
report='one shirt {}, shoe price is {}, jeans priceis {}'
print(report.format(price1,price2,price3))

## Method2
print(f'one shirt [price1], shoe price is {price2}, jeans is {price3}')

## string methods
World5= "python is easy"
World6=" hello, word "
print (World5. title())
print (World5.capitalize())
print (World5.lower())
print (World6.strip())
print (World5.split())


## detatype conversion
num1="23"
num2="45"
add=int(num1)+int(num2)
print(add)
f=print(int(num1))
print(float(num1))

## Input function
name=input (" what is your name:")
print (name)
age= int(input("what is your age:"))
print(age)

##arithemetic operator
num3= int (input ("what is the first number:"))
num4=int (input ("what is the second :"))
print(f'{num3}+ {num4}={num3 + num4} ' )
print(f'{num3}- {num4}={num3 - num4} ' )
print(f'{num3}* {num4}={num3 * num4} ' )
print(f'{num3}/ {num4}={num3 / num4} ' )
print(f'{num3}//{num4}={num3 // num4} ')
print(f'{num3}**{num4}={num3 ** num4} ')

## question
### A person bought a computer for $1,200
##and sold it for $1,800
## calculate the profit made
purchase_price= 1200
selling_price= 1800
profit= selling_price - purchase_price
print(" the profit made $", profit)


