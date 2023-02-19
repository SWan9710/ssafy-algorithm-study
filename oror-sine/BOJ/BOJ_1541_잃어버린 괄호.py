import sys

nums = [0]
tmp = ""
idx = 0

for char in sys.stdin.readline():
    if char.isdigit(): 
        tmp += char
    else:
        nums[idx] += int(tmp)
        tmp = ""
        if char == "-":
            idx += 1
            nums.append(0)

result = 0
for i in range(len(nums)):
    result += nums[i] if i==0 else -nums[i]

print(result)
