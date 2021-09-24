# chapter02_2
# 파이썬 완전 기초
# 파이썬 변수


# 기본 선언
n = 700


# 출력
print(n)
print(type(n))


#동시선언
x = y = z = 700
print(x, y, z)
print()


#선언
var = 75

# 재선언
var = 'Change Value'

# 출력
print(var)
print(type(var))
print()

# Object Refrences
# 변수 값 할당 상태
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔 출력

# 예1)
print(300)
print(int(300))


# 예2)
n = 777

print(n, type(n))
print()

m = n
# m -> 777 <- n
print(m, n)
print(type(m), type(n))
print()

m = 400
print(m, n)
print(type(m), type(n))
print()


# ★id(identity)확인 : 객체의 고유값 확인

m = 800
n = 655

print(id(m))
print(id(n))
print(id(m) == id(n))
print()


# 같은 오브젝트 참조
m = 800
n = 800

print(id(m))
print(id(n))
print(id(m) == id(n))
print()


# 다양한 변수 선언
# Camel Case : numberOfCollegeGraduates - Method
# Pascal Case : NumberOfCollegeGraduates - Class
# Snake Case : number_of_college_graduates - 추천

# 허용하는 변수 선언 법
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 8
# 1AGE = 10 [Error] 변수 제일 앞에 특수문자나 숫자가 오면 에러 발생
# _, $ 허용 특수 문자 


# 예약어 변수명 불가능
# python reserved words
# class = 3 [X]

