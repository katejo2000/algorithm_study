class TestClass:
    a = 10
    b = 0

    def __init__(self, first):
        self.a = first

    if __name__ == "__main__":
        print("This is main")


# test = TestClass(2)
# print(test.a, test.b)
#
# st = input().split()
#
# print(st)


def add(a, b=5):
    return a + b


print(add(3, 3))
