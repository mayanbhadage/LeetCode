class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        arr = list(S)
        
        left= 0
        right = len(arr) -1
        while(left <= right):
            if arr[left] .isalpha() and arr[right].isalpha():
                #Swap these
                temp = arr[left]
                arr[left] = arr[right]
                arr[right] = temp
                left += 1
                right -= 1
            elif not arr[left] .isalpha() and  arr[right].isalpha():
                left += 1
            elif  arr[left] .isalpha() and  not arr[right].isalpha():
                right -= 1
            else:
                left += 1
                right -= 1
        return "".join(x for x in arr)
        