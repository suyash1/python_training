# hello world

# with simple print statement
print 'hello_world, from simple print stamement!'

# with function
def hello():
    print 'procedural hello world!'

class Hello:
    def __init__(self):
        self.greeting = 'OO hello world!'
    
    def greet(self):
        print self.greeting

if __name__ == '__main__':
    hello()
    hello = Hello()
    hello.greet()
