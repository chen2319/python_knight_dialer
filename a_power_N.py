# 算法问题描述： 计算a的N次方， N为整数


# 算法1：直接暴力计算，不解释
# O(n)
def a_power_n_1(a,n):
    res = 1
    i = 0
    while i < n:
        res *= a
        i = i + 1
    return res


# 算法2：分治法，考虑N是奇数还是偶数。偶数 f(n) = f(n/2)*f(n/2)， 奇数 f(n) = f(n-1/2)*f(n-1/2)
# O(logN)
def a_power_n_2(a,n):
    if n == 0:
        return 1
    if n == 1:
        return a

    if n%2 == 0:
        return a_power_n_2(a,n/2) * a_power_n_2(a,n/2)
    else:
        return a_power_n_2(a,(n-1)/2) * a_power_n_2(a,(n-1)/2) * a


if __name__ == '__main__':
    print(a_power_n_1(3,200000))
    print(a_power_n_2(3,200000))