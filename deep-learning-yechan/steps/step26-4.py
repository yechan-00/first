import numpy as np
from dezero import Variable
from dezero.utils import plot_dot_graph
from PIL import Image

# square 함수 정의 (계산 그래프 추적 가능하게)
def square(x):
    return x * x

# 입력값
x = Variable(np.array(0.001))
y = square(square(x))
y.name = 'y'

# 계산 그래프 출력
plot_dot_graph(y, to_file='graph_square_composition.png')
Image.open('graph_square_composition.png').show()