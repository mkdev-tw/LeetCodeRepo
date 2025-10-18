class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        sum_divisors = 0

        for num in nums:
            i = 1
            divisors = []
            while i * i <= num:
                if num % i == 0:
                    j = num // i
                    if j != i:
                        divisors.append(i)
                        divisors.append(j)
                    else: divisors.append(i)
                i += 1
            if len(divisors) == 4:
                for i in divisors:
                    sum_divisors += i

        return sum_divisors 