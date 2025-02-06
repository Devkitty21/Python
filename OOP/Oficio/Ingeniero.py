class First:
    def __init__(self):
        print('First')

class Second(First):
    def __init__(self):
        print('Second')

class Third:
    def __init__(self):
        print('Third')

class fourth(Second,Third, First):
    def __init__(self):
        super(Second, self).__init__()
        print('That\'s it')

f = fourth()
