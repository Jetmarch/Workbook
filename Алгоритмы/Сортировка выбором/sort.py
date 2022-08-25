
def selection_sort(list: list, desc = True) -> list:
    sorted_list = []

    while(len(list) > 0):
        sorted_item = list[0]
        item_index = 0

        for i in range(len(list)):
            if desc:
                if list[i] > sorted_item:
                    sorted_item = list[i]
                    item_index = i
            else:
                if list[i] < sorted_item:
                    sorted_item = list[i]
                    item_index = i

        sorted_list.append(list.pop(item_index))
        #list.remove(sorted_item)
    
    return sorted_list


print(selection_sort([5, 3, 6, 1, 7, 3, 9], False))