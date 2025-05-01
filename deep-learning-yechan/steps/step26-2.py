import numpy as np
from dezero import Variable

def backward(self):
    if self.grad is None:
        self.grad = np.ones_like(self.data)

    funcs = [self.creator]
    while funcs:
        f = funcs.pop()
        if f is None:
            continue
        gys = [output.grad for output in f.outputs]
        gxs = f.backward(*gys)
        if not isinstance(gxs, tuple):
            gxs = (gxs,)
        for x, gx in zip(f.inputs, gxs):
            if x.grad is None:
                x.grad = gx
            else:
                x.grad = x.grad + gx
            if x.creator is not None:
                funcs.append(x.creator)

# 연결
Variable.backward = backward

# sin(x)의 테일러 급수 근사
x = Variable(np.array(3 * np.pi / 4))
y = x
for i in range(1, 6):
    c = (-1)**i / np.math.factorial(2 * i + 1)
    y = y + c * x ** (2 * i + 1)

y.backward()

print("근사한 sin(x):", y.data)
print("미분값 (cos(x) 근사):", x.grad)