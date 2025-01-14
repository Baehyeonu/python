"""
animals라는 패키지를 만들고, 이 패키지 내에 mammals, birds라는 두 개의 서브 모듈을 생성하세요. 

- 각 모듈에는 최소한 한 개 이상의 동물에 관한 클래스를 정의하세요<br>
  (예: mammals에는 Dog, birds에는 Eagle)
- 이 패키지와 모듈을 사용하여 동물들의 정보를 출력하는 프로그램을 작성"""

class mammals:
    def __init__(self,name,age,crying):
        self.name = name
        self.age = age
        self.crying = crying

    def infor(self): 
        print("강아지를 소개합니다")
        print(f"이름 :, {self.name}")
        print(f"나이 : {self.age}살")
        print(f"울음소리 : {self.crying}")