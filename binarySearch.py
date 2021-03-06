def bin(a):
    n = len(a)
    if n <= 1:
        return a
    for i in range(1, n):
        if a[i] < a[i - 1]:
            temp = a[i]
            start = 0
            end = i - 1
            while start <= end:
                mid = int((start + end) / 2)
                if a[mid] > temp:
                    end = mid - 1
                else:
                    start = mid + 1
            for j in range(i - 1, start - 1, -1):
                a[j + 1] = a[j]
            a[start] = temp
    return a


if __name__ == '__main__':
    a = list()
    b = int(input("输入列表的数量:"))
    for i in range(0, b):
        a.append(int(input()))
    print(bin(a))
