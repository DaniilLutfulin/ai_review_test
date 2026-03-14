def binary_search(arr,num):
    left = 0
    right = len(arr)
    mid = (left + right)//2
    while right > left:
        mid = (left + right)//2
        if abs(arr[mid]) < abs(num):
            right = mid
        else:
            left = mid+1
    return left


def insertion_sort(arr, ascending = False, ordered_end = 0):
    if ascending == True:
        arr = arr[:ordered_end+1][::-1] + arr[ordered_end+1:]
    for i in range(ordered_end+1,len(arr)):
        arr.insert(binary_search(arr[:i],arr[i]),arr.pop(i))
    return arr


def calculate_minrun(n, min_n = 16):
    flag = 0
    while n >= min_n:
        flag |= n&1
        n >>= 1
    return n + flag


def get_blocks(arr):
    if len(arr) <= 1:
        return [arr]
    min_run = calculate_minrun(len(arr))
    block_start = 0
    blocks = []
    while block_start < len(arr) - 1:
        end_index = block_start
        ascending_flag = abs(arr[block_start + 1]) > abs(arr[block_start])
        if ascending_flag:
            while end_index < len(arr) - 1 and abs(arr[end_index + 1]) > abs(arr[end_index]):
                end_index += 1
        else:
            while end_index < len(arr) - 1 and abs(arr[end_index + 1]) <= abs(arr[end_index]):
                end_index += 1

        if (end_index - block_start + 1) < min_run:
            ordered_index = end_index
            end_index = min(block_start + min_run - 1,len(arr) - 1)
            cur_block = arr[block_start:end_index+1]
            cur_block = insertion_sort(cur_block, ascending_flag, ordered_end=ordered_index - block_start)
        else:
            cur_block = arr[block_start:end_index + 1]
            if ascending_flag:
                cur_block = cur_block[::-1]
        blocks.append(cur_block)
        block_start += len(cur_block)

    return blocks


def merge_arrs(left_arr,right_arr, gallop_start = 3, merge_counter = -1, debug = False):
    gallops = 0
    left = 1
    right = 2
    new_arr = []
    gallop_counter = 0
    gallop_arr = left
    while len(left_arr) > 0 and len(right_arr) > 0:
        merge_idx = 1
        if abs(left_arr[0]) >= abs(right_arr[0]):
            if gallop_arr == left:
                gallop_counter += 1
                if gallop_counter == gallop_start:
                    merge_idx = binary_search(left_arr, right_arr[0])
                    gallop_counter = 0
                    gallops+=1
            else:
                gallop_arr = left
                gallop_counter = 1
            new_arr.extend(left_arr[:merge_idx])
            left_arr = left_arr[merge_idx:]
        else:
            if gallop_arr == right:
                gallop_counter += 1
                if gallop_counter == gallop_start:
                    merge_idx = binary_search(right_arr, left_arr[0])
                    gallop_counter = 0
                    gallops += 1
            else:
                gallop_arr = right
                gallop_counter = 1
            new_arr.extend(right_arr[:merge_idx])
            right_arr = right_arr[merge_idx:]
    if debug and merge_counter >= 0:
        print(f"Gallops {merge_counter}: {gallops}")
    return new_arr + left_arr + right_arr


def merge_blocks(blocks, debug = False):
    stack = []
    merge_counter = 0

    def merge_yx():
        stack[-2] = merge_arrs(stack[-2], stack[-1], merge_counter=merge_counter, debug=debug)
        if debug:
            print(f"Merge {merge_counter}:", *stack[-2])
        stack.pop(-1)

    def merge_zy():
        stack[-2] = merge_arrs(stack[-3], stack[-2], merge_counter=merge_counter, debug=debug)
        if debug:
            print(f"Merge {merge_counter}:", *stack[-3])
        stack.pop(-2)
    if debug:
        for i in range(len(blocks)):
            print(f"Part {i}:", *blocks[i])

    for i in range(len(blocks)):
        stack.append(blocks[i])
        while len(stack) >= 2:
            x = len(stack[-1])
            y = len(stack[-2])
            if len(stack) > 2:
                z = len(stack[-3])
                if z > x + y or y > x:
                    break
                if x < z:
                    merge_yx()
                    merge_counter += 1
                else:
                    merge_zy()
                    merge_counter += 1
            if x < y:
                break
            merge_yx()
            merge_counter += 1

    if len(stack) >= 2:
        x = len(stack[-1])
        z = None
        if len(stack) > 2:
            z = len(stack[-3])
        if z and x > z:
            merge_zy()
            merge_counter += 1
        else:
            merge_yx()
            merge_counter += 1

    return stack[0]


def timsort(arr, debug = False):
    blocks = get_blocks(arr)
    return merge_blocks(blocks,debug=debug)
