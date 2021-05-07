#사각형의 밑변과 높이를 입력받아 면적을 리턴하는  함수를 정의하고
#테스트하는 프로그램을 작성하시오
#단 원의 반지름은 사용자로부터 입력 받으세요!!
def calcArea(b,h):
       area = b * h
       return area
base = int(input("사각형의 밑변 : "))
height = int(input("사각형의 높이 : "))
recArea = calcArea(base, height)
print("밑변의높이가", base, height,"인 사각형의 면적은", recArea, "입니다")
