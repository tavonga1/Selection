#tavonga Mudzana
#06/10/14
#selection rev ex 4

first_number=int(input("please enter a new number: "))
second_number=int(input("please enter the second number: "))
third_number=int(input("inputplease enter a third number: "))

if first_number > second_number and first_number > third_number:
    print("the first number is bigger")
elif second_number > first_number and second_number > third_number:
    print("the second number is bigger")
elif third_number > first_number and third_number > second_number:
    print("the third number is bigger")

