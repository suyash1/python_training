# This is an example for usage of various operators
#
#
# Arithematic
# Arithematic operations on numbers is same as expected
# while multiplication on python objects other than numbers creates multiple copies of them
# e.g., '#' * 8 will result in ######## 
a = 8
print a, ' * 10 =', a*10

s = '@'
print s, ' * 10 =', s*10

l = [0]
print l, ' * 10 =', l*10

# Comparison operator
print '1 < 2', 'is', 1 < 2 
print '5 > 9', 'is', 5 > 9 
print 'Ramesh != Suresh', 'is', 'Ramesh' != 'Suresh'
print 'Is difference of 5 - 4 and 2 - 1 are same? ',(5 - 4) == (2 - 1)

# Logical opertors
a = None
b = 22
if a and b:
    print 'Hello there! a and b are holding some non-None value'
else:
    print 'either a or b is None'
