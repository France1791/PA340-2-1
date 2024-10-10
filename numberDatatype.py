#Program to add 2 integers
num1 = 5
num2 = 10
sum_integers = num1 + num2
print('Sum of 2 integers is:', sum_integers)

#Program to add 2 float variables
float1 = 5.5
float2 = 10.5
sum_float = float1 + float2
print('Sum of 2 float numbers is:', sum_float)

#Program to add 1 integer and 1 float number
sum_int_float = num1 + float2
print('Sum of 1 integer and 1 float number is:', sum_int_float)
#the sum of an integer and a float number is a float number


# Program that declares two integer variables, assigns an integer to each, and divides the larger number by the smaller number. 
int1 = 10
int2 = 4

result_division = max(int1, int2) / min(int1, int2)
print('Division of larger number by smaller number is:', result_division)


# Program that declares two float variables, assigns a float to each, and divides the larger number by the smaller number.
float1 = 10.5
float2 = 4.5
result_division_float = max(float1, float2) / min(float1, float2)
print('Division of larger float number by smaller float number is:', result_division_float)

#Program that calculates the subtotal and total sale for cafe products
cofee_price = 2.5
cappuccino_price = 3.5
expresso_price = 2.75

subtotal = (3 * cofee_price) + (4 * cappuccino_price) + (2 * expresso_price)
sales_tax = 0.07
total_sale = subtotal + (subtotal * sales_tax)
print('Subtotal is:', subtotal)
print('Total sale is:', total_sale)

#Program that calculates the area of a circle based on the radius
radius = 63
PI = 3.14
area = PI * (radius ** 2)
print('Area of the circle is:', area)