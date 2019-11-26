class Solution:
    def numberOfDays(self, Y: int, M: int) -> int:
        days_31=[1,3,5,7,8,10,12]
        if M == 2:
            if(self.isLeap(Y)):
                return 29
            else:
                return 28
        elif(M in days_31):
            return 31
        else:
            return 30
        
    
    def isLeap(self,year):
        if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0 ):
            return True

            