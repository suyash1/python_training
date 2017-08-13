# Examples of string, list and tuple

x = 'Hello, I am a string.'
y = 'This is a list:'
z = 'Tuple looks like:'

print x
print y, [1, 2, 'abc', [0]*2, {'name': 'John Doe'}]
print z, (1, 3, 5, 7, 'alpha', 'beta')

# extending a string
x = x + ' I am extended but I result in another object creation which is bad when for memory intensive operations... :('
print x
x = 'Hello, I am a string.'
x = ''.join([x, ' I am extended but the reference to the same object is maintained and no new object is created :)'])
print x

# extending list
y = [1, 2, 'abc', [0]*2, {'name': 'John Doe'}]
print 'adding new element in list y:', 22
y.append(22)
print y
print "Merging two lists [1,2,3] and ['a', 'b', 'c'] using extend() method"
temp = [1,2,3]
temp.extend(['a', 'b', 'c'])
print temp

