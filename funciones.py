def duplicados(nums):
    set_nums = set(nums)
    if len(nums) != len(set_nums):
        return True
    else:
        return False