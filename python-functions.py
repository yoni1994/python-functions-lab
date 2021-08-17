def sum_to(n):
    count = 1
    sum = 0
    while count <= n:
        sum += count
        # print(f'{count}: {sum}')
        count += 1
    # print(sum)
    return sum
# sum_to(5)
# sum_to(10)

def largest(li):
    if len(li) == 0:
        print('list is empty')
        return
    max = li[0]
    for number in li:
        if number > max:
            max = number
    # print(max)
    return max

# largest([1, 2, 3, 4, 0])
# largest([10, 4, 2, 231, 91, 54])

def occurances(str1, str2):
    # print(str1.count(str2))
    return str1.count(str2)
# occurances('fleep floop', 'e')
# occurances('fleep floop', 'p')
# occurances('fleep floop', 'ee')
# occurances('fleep floop', 'fe')

def product(*nums):
    total = 1
    for num in nums:
        total *= num
    # print(total)
    return(total)
# product(-1, 4)
# product(2, 5, 5)
# product(4, 0.5, 5)