class Coffee:
    # 클래스 변수
    _type = 'Ice Americano'

    # 클래스 변수 초기화
    def __init__(self, bean):
        self._bean = bean

    def information(self):
        return f'This {self._type} is made of {self._bean} beans.'

    def drink(self):
        return f"I am drinking {self._type}."


coffee = Coffee("Ethiopia")
print(coffee.information())
print(coffee.drink())

