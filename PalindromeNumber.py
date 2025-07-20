# 🚀 LeetCode Problem: Palindrome Number (#9)

## 🧠 Problem-Solving Note

**Problem:** Determine whether an integer is a palindrome.  
**Link:** (https://leetcode.com/problems/palindrome-number/)

---

## 💡 My Understanding

The goal is to check whether a given integer reads the same forward and backward (e.g., `121`, `1221` are palindromes).  
Some key constraints:
- Negative numbers are **not** palindromes (`-121` ≠ `121-`)
- Cannot convert the integer to a string (in the follow-up)

---

## ✅ My Approach

1. **Edge Case Check:**
   - Return `False` if the number is negative
   - Return `False` if it ends with `0` but is not `0` (e.g., `10`)

2. **Reverse Half of the Number:**
   - To avoid overflow and unnecessary work, only reverse half and compare

3. **Compare:**
   - If the reversed half equals the remaining half, it’s a palindrome

---

## 🧪 Code (Python)

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0 or(x%10==0 and x!=0):
            return False

        Half_reverse = 0     
        while x > Half_reverse:
          Half_reverse=Half_reverse*10+x%10
          x=x//10

        return  x==Half_reverse or x==Half_reverse//10
