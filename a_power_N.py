# 算法问题描述： 计算a的N次方， N为整数
import time


# 算法1：直接暴力计算，不解释
# O(n)  (3的400000次方，6秒左右 （Mac Pro）)
def a_power_n_1(a, n):
    res = 1
    i = 0
    while i < n:
        res = res * a
        i = i + 1
    return res


# 算法2：分治法，考虑N是奇数还是偶数。偶数 f(n) = f(n/2)*f(n/2)， 奇数 f(n) = f(n-1/2)*f(n-1/2)
# O(logN)  (3的400000次方，0.3秒左右 （Mac Pro）)
def a_power_n_2(a, n):
    if n == 0:
        return 1
    if n == 1:
        return a

    if n%2 == 0:
        return a_power_n_2(a,n/2) * a_power_n_2(a,n/2)
    else:
        return a_power_n_2(a,(n-1)/2) * a_power_n_2(a,(n-1)/2) * a


# 算法3：a的二进制，遇1相乘。比如 3^9 = 3^1*3^8 (9 = 1001)
# O(logN) (3的400000次方，0.07秒左右 （Mac Pro）)
def a_power_n_3(a, n):
    res = 1
    square = a  # a 的1次方

    while n != 0:
        if n&1 == 1:
           res = square * res
        square = square * square
        n = n >> 1

    return res


if __name__ == '__main__':

    start1 = time.clock()
    res1 = a_power_n_1(3, 400000)
    end1 = time.clock()
    print('1: Running time: %s Seconds %d' % (end1-start1, res1))

    start2 = time.clock()
    res2 = a_power_n_2(3, 400000)
    end2 = time.clock()
    print('2: Running time: %s Seconds %d' % (end2-start2, res2))

    start3 = time.clock()
    res3 = a_power_n_3(3, 400000)
    end3 = time.clock()
    print('2: Running time: %s Seconds %d' % (end3-start3, res3))