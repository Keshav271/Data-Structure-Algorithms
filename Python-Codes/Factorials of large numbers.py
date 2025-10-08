Factorials of large numbers

Given an integer n, find its factorial. Return a list of integers denoting the digits that make up the factorial of n.

Examples:

Input: n = 5
Output: [1, 2, 0]
Explanation: 5! = 1*2*3*4*5 = 120
Input: n = 10
Output: [3, 6, 2, 8, 8, 0, 0]
Explanation: 10! = 1*2*3*4*5*6*7*8*9*10 = 3628800
Input: n = 1
Output: [1]
Explanation: 1! = 1 
Constraints:
1 ≤ n ≤ 103

SOLUTION:

#User function Template for python3

class Solution:
    def factorial(self, n):
        fact=1
        for i in range(1, n+1):
            fact*=i
        digits=[int(d) for d in str(fact)]
        return digits