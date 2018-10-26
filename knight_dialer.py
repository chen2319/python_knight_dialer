# 问题：
# 把一个骑士放在Iphone电话拨号盘上。骑士按照大写“L”的形状移动：水平两步，然后是垂直一步，或者水平一步，然后垂直两步，
# 如果你只能按照骑士的步法来按键盘上的按键。每当骑士落在一个按键上，我们就按那个按键，然后继续下一跳。起始位置被标记为已按过。
# 从某个特定的位置开始，在 N 跳内可以拨打多少个不同的号码？
#
# [原文链接](https://medium.com/@alexgolec/google-interview-questions-deconstructed-the-knights-dialer-f780d516f029)


# 首先定义每个拨号数字能够跳到的下一个数字
NEXT_NUMBER_MAP = {
     1: (6, 8),
     2: (7, 9),
     3: (4, 8),
     4: (3, 9, 0),
     5: tuple(),
     6: (1, 7, 0),
     7: (2, 6),
     8: (1, 3),
     9: (2, 4),
     0: (4, 6),
}


# 获得下一跳的号码
def get_next_dial_number(current_num):
    return NEXT_NUMBER_MAP[current_num]


# 算法1：便利枚举出所有可拨打号码，然后计算个数: 需要计算所有号码（题目只要求数量），性能差
def count_available_number_1(start_number, num_hops):

    def get_number_list(start_number, num_hops, seq=None):
        if seq is None:
            seq = [start_number]

        if num_hops == 0:
            yield seq
            return

        for next_number in get_next_dial_number(start_number):
            yield from get_number_list(next_number, num_hops - 1, seq + [next_number])

    count = 0
    for available_num in get_number_list(start_number, num_hops, None):
        # print(available_num)
        count += 1
    return count


# 算法2：递归遍历只求数量 F(X,N) = Sum(F(next(X), N-1)), and F(X, 0) = 1, 性能还是差
def count_available_number_2(start_number, num_hops):
    if num_hops == 0:
        return 1
    count = 0
    for next_number in get_next_dial_number(start_number):
        count += count_available_number_2(next_number, num_hops-1)
    return count


# 算法3：带cache的递归遍历只求数量 F(X,N) = Sum(F(next(X), N-1)), and F(X, 0) = 1, 性能较好
def count_available_number_3(start_number, num_hops):
    cache = {}

    def get_count_with_cache(start_number, num_hops):
        if (start_number, num_hops) in cache:
            return cache[(start_number, num_hops)]
        if num_hops == 0:
            return 1
        count = 0
        for next_number in get_next_dial_number(start_number):
            count += get_count_with_cache(next_number, num_hops-1)
        cache[(start_number, num_hops)] = count
        return count
    res = get_count_with_cache(start_number, num_hops)
    return res

if __name__ == '__main__':
    res1 = count_available_number_1(1, 11)
    res2 = count_available_number_2(1, 11)
    res3 = count_available_number_3(1, 100)
    print(res1)
    print(res2)
    print(res3)

