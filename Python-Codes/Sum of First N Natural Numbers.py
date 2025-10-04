Sum of First N Natural Numbers

Given an integer n, your task is to compute the sum of all natural numbers from 1 to n (inclusive). If n is 0, the sum should be 0.

Examples:

Input: n = 6
Output: 21
Explanation: The sum of natural numbers up to 6 is: 1 + 2 + 3 + 4 + 5 + 6 = 21
Input: n = 4
Output: 10
Explanation: The sum of natural numbers up to 4 is: 1 + 2 + 3 + 4 = 10
Input: n = 0
Output: 0
Explanation: Since n is 0, the sum is 0.
Constraints:
0 ≤ n ≤ 104


SOLUTION:

#User function Template for python3

class Solution:
    def sumOfNaturals(self, n):
        sum=0
        for i in range(1,n+1):
            sum=sum+i
        return sum