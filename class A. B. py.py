class A:
    def __init__(self):
        self.message = "Hello"

class B(A):
    def __init__(self):
        super().__init__()
