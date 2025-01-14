p = 3.14

def extent_samgaghyeong(x):
    x,y = map(int,input("밑변과 높이를 입력해 주세요").split(" "))
    return x * y / 2

def extent_one(x):
    x = int(input("반지름을 입력하세요: "))
    return x * x * p

def extent_sagaghyeong(x):
    x,y = map(int,input("밑변과 높이를 입력해 주세요").split(" "))
    return x * y