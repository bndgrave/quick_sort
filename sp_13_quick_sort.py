# Номер посылки - 69069447

def quick_sort(array, begin, end):
    if begin >= end:
        return
    pivot = array[begin]
    left = begin + 1
    right = end
    while left < right:
        if array[left] >= pivot:
            if array[right] <= pivot:
                array[left], array[right] = array[right], array[left]
            else:
                right -= 1
        else:
            left += 1
    if array[begin] >= array[left]:
        array[begin], array[left] = array[left], array[begin]
    quick_sort(array, begin, left-1)
    quick_sort(array, left, end)


def read_input():
    people_number = int(input())
    data = []
    for ind in range(people_number):
        row = input().split()
        row[1], row[2] = int(row[1]), int(row[2])
        row = [-row[1], row[2], row[0]]
        data.append(row)
    return data


def print_results(array):
    for record in array:
        print(record[2])


if __name__ == '__main__':
    data = read_input()
    quick_sort(data, 0, len(data)-1)
    print_results(data)
