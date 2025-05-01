import numpy as np
import math
from dezero import Variable
from dezero.utils import plot_dot_graph
from PIL import Image

# sin(x)의 테일러 급수 근사
x = Variable(np.array(3 * np.pi / 4))
y = x
for i in range(1, 6):
    c = (-1)**i / math.factorial(2 * i + 1)
    y = y + c * x ** (2 * i + 1)

y.name = 'y'

# 계산 그래프 시각화
plot_dot_graph(y, to_file='graph_sin_taylor_6.png')
Image.open('graph_sin_taylor_6.png').show()