a = {}
print 'This is an empty dictionary-', a

# adding some key and value in dictionary a

a['first_name'] = 'Shinchan'
a['last_name'] = 'Nohara'

print 'Added some data in dictionary', a

b = {'Company': 'Tesla'}
# extending or updating another dictionary 'b' with some other dictionary
print 'updating another dictionary', b, 'with some other dictionary'
b.update({'first_name': 'Elon', 'last_name':'Musk'})
print b
