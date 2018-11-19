# 算法问题描述： 给定一个整数，要求抽取其中k个数字后，留下来的整数是最小。例如： 43672， 抽取其中2个数字k=2，剩下最小的是362， 抽取的是4，7

# 算法： 很显然，并不是直接抽取最大的k个数，如上例，并不是直接抽取6和7。所以，应该是从高位开始，按顺序，抽取比右边数字大的数 4>3, 7>2


def number_remove_k_1(num, k):
    n_list = list(map(int,num))

    n_length = len(n_list)
    after_list = [] #可以看成是栈结构，最后一个是栈顶元素
    new_length = n_length - k
    if new_length <= 0:
        return "0"

    top_index = 0
    for i in n_list:
        while top_index > 0 and k > 0 and after_list[top_index-1] > i:
            k = k-1
            after_list.pop(top_index-1)
            top_index = top_index -1
        after_list.append(i)
        top_index = top_index + 1

    index_zero = 0
    while index_zero < new_length and after_list[index_zero] == 0:
        index_zero = index_zero + 1

    if index_zero == new_length:
        return "0"

    return ''.join(list(map(str, after_list[index_zero:new_length])))



if __name__ == '__main__':
    # res = number_remove_k_1("78912", 2)
    res = number_remove_k_1("112", 1)
    print(res)