#tavonga mudzana
#22/09/14
#spot check q2

weight=int(input("please enter your weight: "))

hundred=weight//100
remainder=weight%100

fifty=remainder//50
ramainder=remainder%50

ten=remainder//10
remainder=remainder%10

two=remainder//2
remainder=remainder%2

one=remainder
print("{0} 100 gram weights".format(hundred))
print("{0} 50  gram weights".format(fifty))
print("{0} 10  gram weights".format(ten))
print("{0} 2   gram weightd".format(two))
print("{0} 1   gram weights".format(one))
