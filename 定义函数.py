# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
# ax2 + bx + c = 0的两个解。
# 提示：计算平方根可以调用math.sqrt()函数：
import math


def quadratic(a, b, c):
    if b * b < 4 * a * c:
        return ('无实数解')
    else:
        return (-b + math.sqrt(b * b - 4 * a * c)) / 2 / a, (
            -b - math.sqrt(b * b - 4 * a * c)) / 2 / a


# 测试:
print(quadratic(2, 3, 1))  # => (-0.5, -1.0)
print(quadratic(1, 3, -4))  # => (1.0, -4.0)
