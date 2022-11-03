# 클래스의 인스턴스 객체가 생성될 때마다 카운트를 1식 증가시키는 클래스 구현
# 이 때 카운트 증가 함수는 클래스 내 메서드를 통해서 구현

# 클래스 생성
class Person:
    # 클래스 변수
    count_class_var = 0

    # 생성자
    def __init__(self, name, age, power):
        self.name = name
        self.age = age
        self.power = power
        # increase_obj 메서드 호출
        self.increase_obj()  # Person.increase_obj()가 아님을 주의

    def increase_obj(self):  # 클래스 변수 값 1 증가
        Person.count_class_var += 1
        print(Person.count_class_var)


print('현재까지 생성된 인스턴스 객체의 갯수 : ', Person.count_class_var)

p1 = Person("홍길동", 20, 50)
print('현재까지 생성된 인스턴스 객체의 갯수 : ', Person.count_class_var)
p2 = Person("강감찬", 40, 60)
print('현재까지 생성된 인스턴스 객체의 갯수 : ', Person.count_class_var)
p2 = Person("을지문덕", 30, 70)
print('현재까지 생성된 인스턴스 객체의 갯수 : ', Person.count_class_var)
