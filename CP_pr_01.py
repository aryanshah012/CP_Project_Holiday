def insertion_sort(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > current:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current

def find_mode(array):
    mode = array[0]
    max_count = 1

    current = array[0]
    current_count = 1

    for i in range(1, len(array)):
        if array[i] == current:
            current_count += 1
        else:
            if current_count > max_count:
                max_count = current_count
                mode = current

            current = array[i]
            current_count = 1

    # Check for the last element
    if current_count > max_count:
        mode = current

    return mode

if __name__ == "__main__":
    n = int(input())

    arr = []
    sum = 0
    for _ in range(n):
        num = int(input())
        arr.append(num)
        sum += num

        insertion_sort(arr)

        # after sorting, arr[0] will be min and the element at the current index will be max
        min_val = arr[0]
        max_val = arr[-1]

        avg = sum / len(arr)

        mode = find_mode(arr)

        print(f"min, max, sum, average, and mode after insertion of {arr[-1]} is : {min_val}, {max_val}, {sum}, {avg}, {mode}")
