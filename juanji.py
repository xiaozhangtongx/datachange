import numpy as np
import pandas as pd

a = pd.read_csv("res/DM1.csv", header=None)
a = np.array(a)
print(len(a))


def zero_pad(x, pad_height, pad_width):  # 先在待处理矩阵周围填充0
    H, W = x.shape  # H为待处理矩阵的高（行），Wi为待处理矩阵的宽（列）
    out = None
    out = np.zeros((H + 2 * pad_height, W + 2 * pad_width))  # 知道尺寸后先全填入0
    out[pad_height:pad_height + H, pad_width:pad_width + W] = x  # 后在中间填入x，这样边缘填充0就完成了
    return out


# 卷积运算
def conv_fast(x, h):
    Hi, Wi = x.shape  # Hi为待处理矩阵的高（行），Wi为待处理矩阵的宽（列）
    Hh, Wh = h.shape  # Hh为卷积核的高（行），Wi为卷积的宽（列）
    out = np.zeros((Hi, Wi))  # 相当于占位

    pad_height = Hh // 2  # mode为same情况下，填充0的数量取决于卷积核h的尺寸
    pad_width = Wh // 2
    image_padding = zero_pad(x, pad_height, pad_width)
    h_flip = np.flip(np.flip(h, 0), 1)  # np.flip 是翻转函数,参数0为上下翻转也就是行翻转,而参数1为左右翻转也就是列翻转

    for i in range(Hi):
        for j in range(Wi):
            out[i][j] = np.sum(np.multiply(h_flip, image_padding[i:(i + Hh), j:(j + Wh)]))  # 加权求和后写入结果到out对应位置
    return out


h = np.array([[1, 1, 1],
              [1, 0, 1],
              [1, 1, 1]])

res = conv_fast(a, h)
print('卷积运算结果 :')
print(res)
np.savetxt(r'res/DM2.csv', res, fmt='%d', delimiter=',')
