import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import numpy as np
import math
from dezero import Variable
from dezero.utils import plot_dot_graph
from PIL import Image

# 테일러 급수를 이용한 sin(x) 근사
x = Variable(np.array(np.pi / 4))
y = x
for i in range(1, 6):
    c = (-1)**i / math.factorial(2 * i + 1)
    y = y + c * (x ** (2 * i + 1))

y.name = 'y'
plot_dot_graph(y, to_file='graph_taylor_sin.png')
print("sin(x) 테일러 급수 계산 그래프가 graph_taylor_sin.png 로 저장되었습니다.")
Image.open('graph_taylor_sin.png').show()