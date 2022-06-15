def quick_sort(array, key):
    if len(array) == 1:
        return array
    pivot = array[0][key]
    left = 1
    right = len(array) - 1
    while left < right:
        if array[left][key] < pivot:
            if array[right][key] > pivot:
                array[left], array[right] = array[right], array[left]
            else:
                right -= 1
        else:
            left += 1
    array[0], array[left-1] = array[left-1], array[0]
    array = quick_sort(array[0:left], key) + quick_sort(array[left:len(array)], key)
    return array

def read_input():
    people_number = int(input())
    data = []
    for ind in range(people_number):
        row = input().split()
        row[1:len(row)] = map(int, row[1:len(row)])
        data.append(row)
    return data

def print_results(array):
    for ind in range(len(array)):
        print(array[ind][0])


if __name__ == '__main__':
    data = read_input()
    print(data)
    print_results(quick_sort(data, 2))
