# if statement
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# multiple conditions
age_0 = 22
age_1 = 18
age_0 >= 21 or age_1 >= 21

# simple if statement structure
#   if conditional_test:
#       do something
#   else:
age = 19
if age <= 18:
    print("To young, Mate!")
else:
    print("Go Hard!")


