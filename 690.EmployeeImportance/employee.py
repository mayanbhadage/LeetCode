class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        importance_val = 0
        subordinates = [id]
        for x in subordinates:
            for emp_details in employees:
                if emp_details.id == x:
                    importance_val += emp_details.importance
                    subordinates += emp_details.subordinates
        
        return importance_val