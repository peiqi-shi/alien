
class A():
    def __init__(self) -> None:
        self.a=10
    pass

class AA( A ):
    def __init__(self) -> None:
        A.__init__(self)
        self.b=20
        pass