def reverse_list(arr, start, end):
    if start >= end:
        return

    arr[start], arr[end] = arr[end], arr[start]
    reverse_list(arr, start + 1, end - 1)


n = int(input("Enter n: "))


print("Enter", n, "integers:", end=" ")
input_list = list(map(int, input().split()[:n]))


print("Original list:", ' '.join(map(str, input_list)))


print("Start reversing ...")
reverse_list(input_list, 0, n - 1)


print("Reversed list:", ' '.join(map(str, input_list)))