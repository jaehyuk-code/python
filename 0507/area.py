#면적을 구하는 프로그램 using function
def cirArea(r):
       return 3.14159 * r * r
def rectArea(b, h):
    return b * h
def triArea(b, h):
     return 0.5 * b * h

while True:
       print("0. 끝내기")
       print("1. 원의 면적")
       print("2. 삼각형의 면적 구하기")
       print("3. 사각형의 면적 구하기")
       choice = int(input("원하는 작업을 선택하세요: "))

       if choice == 0:
              break
       if choice == 1:
         rad = int(input("원의 반지름 입력 : "))
         print("반지름", rad, "인 원의 면적은", cirArea(rad))
       elif choice == 2:      
        base = int(input("삼각형의 밑변 : "))
        hgt = int(input("삼각형의 높이 : "))
        print("밑변 높이", base, hgt, "삼각형의 면적은", triArea(base, hgt))
       elif choice ==3:
        base = int(input("사각형의 밑변 : "))
        hgt = int(input("사각형의 높이 : "))
        print("밑변 높이", base, hgt, "사각형의 면적은", triArea(base, hgt))
       else:
        print("잘못된 선택입니다.")
print("좋은하루 보내세요")
