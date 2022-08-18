

from array import array


def binary_search(list, value):
    '''
        Принимает в себя отсортированный массив и значение, которое требуется найти в массиве
        Возвращает индекс массива
        Работает только с числовыми значениями
    '''
    
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = int((low + high) / 2)
        val = list[mid]

        if val == value:
            return mid
        
        if val < value:
            low = mid + 1
        else:
            high = mid - 1
    
    return None

list = [1, 3, 5, 7]


print(f'Позиция 5 в списке {list}: {binary_search(list, 5)}')

print(f'Позиция 7 в списке {list}: {binary_search(list, 7)}')

print(f'Позиция 1 в списке {list}: {binary_search(list, 1)}')

print(f'Позиция 10 в списке {list}: {binary_search(list, 10)}')