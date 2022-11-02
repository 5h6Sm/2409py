# 얕은 복사
l = []
print(l)
player = ["Messi", 10, True]
print(player)
print(list("Happy"))
print(list((1125, 2436)))
print(list({"menu": "pizza", "price": 10000}))
print(list({"사과", "배"}))
nums = list(range(3))
print(nums)

print(nums + [10, 11])
nums += [10, 11]
print(nums)

nums.append(20)
print(nums)
nums.append([30, 31])
print(nums)
nums.insert(2, 40)
print(nums)
nums.extend([50, 51])
print(nums)

a = [1, 2, 3]
a.append(4)
print(len(a))

# 리스트 요소 수정, 제거

print(nums[7])
nums[7] = 60
print(nums)

del nums[2]
print(nums)
nums.remove(20)
print(nums)
nums.pop()
nums.pop(5)
nums.append(20)
print(nums)
nums.remove(10)
print(nums)
nums.clear()
print(nums)

nums = list(range(3))
print(nums)
nums += [100, 10]
print(nums)
print(nums[3])

print(3 in nums)
print(10 in nums)

print(len(nums))
nums.sort()
print(nums)
nums.reverse()
print(nums)
