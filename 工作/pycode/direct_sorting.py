#coding=utf-8
def direct_sorting():
    arr = [0, 48, 62, 35, 77, 55, 14, 98]
    for i in range(2, len(arr)):
        temp = arr[i]
        j = i - 1;
        while(temp < arr[j]):
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = temp
    print(arr[1:])

direct_sorting()