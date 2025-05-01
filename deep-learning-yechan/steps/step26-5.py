import numpy as np

# 함수 정의
def f(x):
    return x**4 - x**2

def f_prime(x):
    return 4 * x**3 - 2 * x

def f_double_prime(x):
    return 12 * x**2 - 2

# 뉴튼 방법 구현
x = 2.0  # 초기값
max_iter = 100
tol = 1e-6  # 허용 오차
history = []

for i in range(max_iter):
    x_new = x - f_prime(x) / f_double_prime(x)
    history.append(x_new)
    
    if abs(x_new - x) < tol:
        print(f"수렴 완료: {i+1}회 반복 후 x = {x_new}")
        break
    x = x_new
else:
    print("수렴하지 않았습니다.")

# 결과 출력
print("최솟값 근사 지점:", x)
print("최솟값 f(x):", f(x))