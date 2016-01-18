

def load():
    f = open("prob18.txt", "rt")
    nums = []
    i = 0
    for line in f.readlines():
        nums.append([])
        for num in line.split(' '):
            nums[i].append(int(num))
        i+= 1
    return nums

def run(nums):
