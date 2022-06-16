def quick_sort(array):
    if len(array) == 1:
        return array
    pivot = array[0]
    left = 1
    right = len(array) - 1
    while left < right:
        if array[left] <= pivot:
            if array[right] >= pivot:
                array[left], array[right] = array[right], array[left]
            else:
                right -= 1
        else:
            left += 1
    if array[0] <= array[left]:
        array[0], array[left] = array[left], array[0]
    array = quick_sort(array[0:left]) + quick_sort(array[left:len(array)])
    return array

def read_input():
    people_number = int(input())
    data = []
    for ind in range(people_number):
        row = input().split()
        row[1:len(row)] = map(int, row[1:len(row)])
        row[0] = list(map(ord, row[0]))
        row = [row[1], -row[2], [sym*-1 for sym in row[0]]]
        data.append(row)
    return data

def print_results(array):
    for ind in array:
        name_char = [sym*-1 for sym in ind[2]]
        name = ''.join(list(map(chr, name_char)))
        print(name)


if __name__ == '__main__':
    data = read_input()
    data_sorted = quick_sort(data)
    print_results(data_sorted)
