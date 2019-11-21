class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        
        people = [0 for _ in range(0,num_people)]
        
        currCandies = 0
        while(candies > 0):
            for i in range(0,num_people):
                currCandies += 1
                if(candies < currCandies):
                    people[i] += candies;
                    candies = 0
                    break
                people[i] +=currCandies
                candies -= currCandies
            
        return people