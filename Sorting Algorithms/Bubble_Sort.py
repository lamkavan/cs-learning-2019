### The following implements bubble sort ###

def bubble_sort(input_list):
    return_list = input_list.copy()

    for x in range(0, len(input_list)):
        for y in range(0, len(input_list) - 1):
            if (return_list[y] > return_list[y + 1]):
                temp = return_list[y]
                return_list[y] = return_list[y + 1]
                return_list[y + 1] = temp

    return return_list


def bubble_sort_with_steps(input_list):
    return_list = input_list.copy()

    print("Initial state: " + str(return_list))
    for x in range(0, len(input_list)):
        for y in range(0, len(input_list) - 1):
            if (return_list[y] > return_list[y + 1]):
                temp = return_list[y]
                return_list[y] = return_list[y + 1]
                return_list[y + 1] = temp
        print("State after " + str(x + 1) + "iterations: " + str(return_list))

    return return_list
