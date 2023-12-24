class Solution(object):
    def isPalindrome(self, x):
        if 0>x : return False
        div =1
        while x >= div*10:
            div*=10
        while x:
            right= x%10
            left = x//div
            if right != left: return False
            x=(x%div)//10
            div=div//100
        return True
        