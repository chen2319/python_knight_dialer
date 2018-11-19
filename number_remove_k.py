# 算法问题描述： 给定一个整数，要求抽取其中k个数字后，留下来的整数是最小。例如： 43672， 抽取其中2个数字k=2，剩下最小的是362， 抽取的是4，7

# 算法： 很显然，并不是直接抽取最大的k个数，如上例，并不是直接抽取6和7。所以，应该是从高位开始，按顺序，抽取比右边数字大的数 4>3, 7>2


def number_remove_k_1(num, k):
    n_list = list(map(int,num))

    n_length = len(n_list)
    after_list = [] #可以看成是栈结构，最后一个是栈顶元素
    after_n = n_length - k
    if after_n <= 0:
        return "0"

    for i in range(n_length):
        if k == 0:
            m = after_n - len(after_list)
            after_list.extend(n_list[i:i+m+1])
            break

        if len(after_list) == 0:
            after_list.append(n_list[i])
        else:
            # 和栈after_list的顶元素比较，如果比它小，则栈顶元素出栈，接续比下一个栈顶元素，直到k为0或者不满足条件，入栈。
            compare_n = after_list[len(after_list)-1]
            while n_list[i] < compare_n:
                after_list.pop(len(after_list)-1)
                k = k-1
                if len(after_list) == 0 or k == 0:
                    break
                compare_n = after_list[len(after_list)-1]
            after_list.append(n_list[i])

    res = after_list[:after_n]
    y = 0
    l = len(res)
    for j in range(l):
        if res[j] == 0:
            if y == l-1:
                y=j
                break
            else:
                y=j+1

        else:
            break
    return ''.join(list(map(str, res[y:])))



if __name__ == '__main__':
    # res = number_remove_k_1("78912", 2)
    res = number_remove_k_1("100", 1)
    print(res)