class Smartphone:
    # 클래스 변수
    thanks = "Thank You for buying!"

    # 클래스 변수 초기화
    def __init__(self, brand, information):
        self._brand = brand
        self._information = information
        print(Smartphone.thanks)

    def information(self):
        return f'Smartphone Detail Info : {self._information.get("color")} {self._brand} ${self._information.get("price")}'


smartphone1 = Smartphone('Iphone', {'color': 'Navy', 'price': 1200})
print(smartphone1.information())

smartphone2 = Smartphone('Galaxy', {'color': 'Black', 'price': 1000})
print(smartphone2.information())

# print(Smartphone.__dict__)

print(smartphone1.__dict__)
print(smartphone2.__dict__)
