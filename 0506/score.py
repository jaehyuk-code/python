marks = []

for i in range(5):
       scr = int(input("%d번 학생의 성적" %(i+1)))
       marks.append(scr)


print(marks)
sum = 0
number = 0
for mark in marks:
       number = number + 1
       sum = sum + mark
       if mark >= 60:
              print("%d번 학생의 성적은 %d이고 합격입니다." %(number,mark))
       else:
              print("%d번 학생의 성적은 %d이고 합격입니다." %(number,mark))
print("전체 학생의 총합은 %d이고 평균은 %f입니다." % (sum, (sum/number)))
