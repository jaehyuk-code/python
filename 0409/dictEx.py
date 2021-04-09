# dictionarty는 key:value 쌍으로 자료를 저장합니다.
# dictionarty는 숫자로 인덱싱 할 수 업고
# 키 값으로  벨류에 접근할 수 있습니다.
a= dict()
a['name'] = 'python'     #키 값으로 문자열 가능 
a[('a',)] = 'python'      #키 값으로 튜플 가능 (변경되지 않아서)    
#a[[1]] = 'python'       # error 키 값으로 리스트 불가능
a[250] ='python'         # 키 값으로 정수 가능

print(a) 
