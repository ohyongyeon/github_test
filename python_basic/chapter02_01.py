# Chapter02-1
# 파이썬 완전 기초
# Print 사용법


# 기본 출력
print('Python Start!')
print("python Start!")
print('''Python Start!''')
print("""Python Start!""")

print()


# Separator 옵션
print('P', 'Y', 'T', 'H', 'O', 'N', sep='')
print('P', 'Y', 'T', 'H', 'O', 'N', sep=',')
print('P', 'Y', 'T', 'H', 'O', 'N', sep='|')
print('P', 'Y', 'T', 'H', 'O', 'N', sep='    ')

print('010', '7777', '1234', sep="-")
print('python', 'google.com', sep="@")
print()


# end 옵션
print('Welcome to', end=" ")
print('IT News', end=" ")
print('Web site')
print()


# file 옵션
# 파일 쓰기
import sys
print('Learn Python', file=sys.stdout)
print()


# ★중요 format 사용(d(정수), s(문자), f(실수))
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', 'two'))
print('{1} {0}'.format('one', 'two'))
print()


# %s 문자 // s 생략 가능
print('%10s' % ('nice'))
print('{:>10}'.format('nice'))

print('%-10s' % ('nice'))
print('{:10}'.format('nice'))

print('{:_>10}'.format('nice')) #공백 _ 표시
print('{:^10}'.format('nice')) #중앙 정렬

print('%5s' % ('pythonstudy')) 
print('%.5s' % ('pythonstudy')) # 절삭
print('{:10.5}'.format('pythonstudy')) # 10공간 5글자 표기
print()


# %d 정수
print('%d %d' % (1,2))
print('{} {}'.format(1,2))

print('%4d' % (42))
print('{:4d}'.format(42))
print('test')
print('{:d}'.format(42))
print('test')

# %f 실수
print('%f' % (3.1424242424242424))
print('%1.18f' % (3.1424242424244242)) # %1 정수부 // 18f 실수부 지정가능
print('{:f}'.format(3.1424242424242))

print('%06.2f' % (3.14242424242)) # '06'은 6자리를 의미 // 2f 소수 2자리 // 나머지는 00
print('{:06.2f}'.format(3.14242424242))