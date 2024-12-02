
def is_safe(arr):
    return all(1 <= arr[i] - arr[i + 1] <= 3 for i in range(len(arr) - 1)) or \
    all(1 <= arr[i + 1] - arr[i] <= 3 for i in range(len(arr) - 1))

def answer():
    count = 0
    with open("aoc_2.txt", "r") as file:
        for line in file:
            nums = list(map(int, line.strip().split()))
            if is_safe(nums):
                count += 1
    print(count)
    
answer();