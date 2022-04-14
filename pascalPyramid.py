# TCS CodeVita 2019 - Round 2

# We start with six numbers at the base of the pyramid and construct the 
# pyramid one layer at a time by adding the two adjacent numbers in the previous layer.

# For Example, starting with the numbers 1 2 3 4 5 6 in the base, we get the 
# following pyramid. The apex of the pyramid is filled with the product of the 
# numbers in the row below instead of the sum.

#             3072
#           48   64
#         20  28    36
#      8   12    16   20
#   3    5    7    9     11
# 1   2    3     4     5     6

# In the above pyramid, the apex is filled with the number 48 x 64 =3072. 
# The aim is to get| the largest number possible at the apex of the pyramid. The 

# Another Arrangement
#                 3953
#               67    59
#           34     33     26
#       15     19     14    12
#    5     10      9      5     7
# 1     4      6      3      2     5

# Input:
# input will be a set of N positive integers. 6 numbers need to be chosen from these and 
# arranged at the base to get the largest possible number at the top.

# N < 13
def getMaxApexValue(nums):
    a, b, c, d, e, f = nums[4], nums[2], nums[1], nums[0], nums[3], nums[5]

    return (a + 4*b + 6*c + 4*d + e)*(b + 4*c + 6*d + 4*e + f)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    # arr = [10, 4, 74, 61, 8, 37, 2, 35] -> O/P = 746415
    # arr = [1, 2, 3, 4, 5, 6] -> O/P = 5475

    arr.sort(reverse = True)
    nums = arr[ : 6]

    print(getMaxApexValue(nums))


