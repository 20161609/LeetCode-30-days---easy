# Notes  

## Link  
https://leetcode.com/problems/find-numbers-with-even-number-of-digits/description/  

## Code
``` python
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum((len(str(num))+1)%2 for num in nums)    
```

## Idea  
- **Key pattern(s):** Count numbers that have an **even number of digits**.  
- **Core steps:**  
  - Convert each number to a string to measure its digit count.  
  - Check whether the count is even.  
  - Sum up the counts to get the total.  

## Complexity  
- **Time:** O(n) — each number is processed once.  
- **Space:** O(1) — no extra space except for temporary string conversion.  

## Gotcha  
- String conversion slightly increases runtime but remains linear overall.  
- Only works correctly for non-negative integers (as per problem constraints).