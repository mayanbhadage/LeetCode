class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        # Finding already satisfied customers
        already_satisfied = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                already_satisfied += customers[i]
                customers[i] = 0
        
        # now we have to find max with the super power
        
        max_satisfied = 0
        curr_satisfied = 0
        for i, curr_customer in enumerate(customers):
            curr_satisfied += curr_customer
            
            if i >= X:
                curr_satisfied -= customers[i-X]
            
            max_satisfied = max(max_satisfied,curr_satisfied)
        return already_satisfied + max_satisfied
                

                