class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        distances = []
        
        for worker_id, worker_pos in enumerate(workers):
            temp = []
            for bike_id, bike_pos in enumerate(bikes):
                #Calculate distance:
                dist = abs(worker_pos[0]- bike_pos[0]) + abs(worker_pos[1] - bike_pos[1])
                temp.append((dist, worker_id, bike_id))
            temp.sort(reverse = True)
            distances.append(temp)
        
        # Now we have a list with worker bike and distances
        
        # Add smallest distance bike in heap
        
        heap = []
        for i in range(len(workers)):
            heapq.heappush(heap,distances[i].pop())
        
        #add bikes to the result
        used = set()
        result = [0] * len(workers)
        
        while(len(used) < len(workers)):
            curr_dist, w_id, b_id = heapq.heappop(heap)
            
            if b_id not in used:
                result[w_id] = b_id
                used.add(b_id)
            else:
                heapq.heappush(heap, distances[w_id].pop())
        return result        
        