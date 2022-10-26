name = 'John'
lastname= 'Wick'
age =40
print('My name is {} {}'.format(name,lastname))
print('My name is {1} {0}'.format(name,lastname))
print('My name is {l} {n}'.format(n=name,l=lastname))
print("My name is {} {}. I 'm {} years old".format(name,lastname,age))
print('My name is {} {}'.format(name,name))
print('My name is {0} {1}. I am {2} {2} years old'.format(name,lastname,age))

number = 200 /700
print('Result is {n:1.2}'.format(n=number))

print(f"My name is {name} and my last name is {lastname} I am {age} years old")