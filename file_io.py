# There are two ways to read a file
# With and without 'with' context manager
# Without 'with' context manager, you will explicitly need to close
# the file

fp = open('sample.txt', 'r')
# read() loads all the file content in memory as a single string
# this is preferably not the best way to read a file
all_content = fp.read()
print 'all file contents are loaded at once in memory using read(). The data is: ',
print all_content
fp.close()
print '~'*50

fp = open('sample.txt', 'r')
# reaadlines loads every line into memory line by line
print 'reading line by line below'
for line in fp.readlines(): # line is an iterator object
    print line
fp.close()
print '~'*50

# usinf with context manager. Most preferred way for file i/o
print 'Using with statement to perform file i/o'
with open('sample.txt', 'r') as fp:
    for line in fp.readlines():
        print line

print '~'*50
print 'You have been successfully demonstrated with file read operations.\
\nYour next task is perform file writes.\n'
