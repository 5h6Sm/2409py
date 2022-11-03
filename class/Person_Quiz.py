class Person_Quiz:
    def print_info(self):
        print('-'*30)
        print('이름 : ' + self.name)
        print('나이 :', self.age)
        print('-'*30)

    def __init__(self, name, age):
        # 생성자
        self.name = name
        self.age = age


p1 = Person_Quiz('홍길동', 20)
p1.print_info()

p2 = Person_Quiz('강감찬', 40)
p2.print_info()

p3 = Person_Quiz('을지문덕', 30)
p3.print_info()
