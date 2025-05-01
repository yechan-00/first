def sum_to(x, shape):
    return x  # Placeholder for broadcasted sum

def get_item(x, slices):
    return x[slices]

def reshape(x, shape):
    return x.reshape(shape)

def transpose(x, axes=None):
    return x.transpose(axes) if axes is not None else x.T

def sum(x, axis=None, keepdims=False):
    return x.sum(axis=axis, keepdims=keepdims)

def matmul(x0, x1):
    return x0 @ x1

def max(x, axis=None, keepdims=False):
    return x.max(axis=axis, keepdims=keepdims)

def min(x, axis=None, keepdims=False):
    return x.min(axis=axis, keepdims=keepdims)

import numpy as np
import dezero.core as core

class Sin(core.Function):
    def forward(self, x):
        return np.sin(x)

    def backward(self, gy):
        x, = self.inputs
        from dezero.functions import cos
        return gy * cos(x)

def sin(x):
    x = core.as_variable(x)
    return Sin()(x)


class Cos(core.Function):
    def forward(self, x):
        return np.cos(x)

    def backward(self, gy):
        x, = self.inputs
        from dezero.functions import sin
        return gy * -sin(x)

def cos(x):
    x = core.as_variable(x)
    return Cos()(x)