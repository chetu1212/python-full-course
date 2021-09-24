#********************     arithmatic operator   *****************
# + , - , * , /
a=10
b=220
print("the sum of",a," and ",b," is = ",a+b)    #addtion
print("the subtraction of",b," and ",a," is = ",b-a) #subtraction
print("the subtraction of",a," and ",b," is = ",a-b) #subtraction
print("the multiplication of",b," and ",a," is = ",b*a)  #multiplication
print("the division of",b," and ",a," is = ",b/a)   #division
print("the division of",a," and ",b," is = ",a/b)

#***********   assignment operators ********************
# += , -= , *=  ,/=
k=34
k+=2
print(k)
k-=10
print(k)
k*=10
print(k)
k/=5
print(k)


#*********** comparison operator **********
#   == , >  ,  <  , <= , >= ,!=

t=(10==20)
print(t)
t=(10>20)
print(t)
t=(10<20)
print(t)
t=(10<=20)
print(t)
t=(10>=20)
print(t)
t=(10!=20)
print(t)

#********************* logical operstors *******************
#   and ,or ,not
bool1=1
bool2=0
print("and operator result ",(bool1 and bool2))
print("or operator result ",(bool1 or bool2))
print("not operator result ",(not bool2))