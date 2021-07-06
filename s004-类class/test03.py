
'''
Enter() should lock the resources and optionally return an object.
Exit() should release the resources.
Any exception that happens inside the with block is passed to the exit() method.
If it wishes to suppress the exception it must return a true value.
'''

class MyOpen:
    def __init__(self, filename):
        self.filename = filename
    def __enter__(self):
        self.file = open(self.filename)
        return self.file
    def __exit__(self, exc_type, exception, traceback):
        self.file.close()

with open('test.txt', 'w') as file:
    file.write('Hello World!')
with MyOpen('test.txt') as file:
    print(file.read())