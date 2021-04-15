
year = int(input("연도를 입력하시오:"))
if(year%4 ==0 and year%100 != 0 or year%400 == 0):
 print(year,"년은 윤년(leap year)입니다.")
else:
   print(year,"년은 평년(common year)입니다.")
