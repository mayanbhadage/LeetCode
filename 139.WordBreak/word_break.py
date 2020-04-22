class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        queue = deque([s])
        seen = set()
        while queue:
            curr_string = queue.pop()
            for word in wordDict:
                if curr_string.startswith(word):
                    new_str = curr_string[len(word):]
                    if new_str == "":
                        return True
                    
                    if new_str not in seen:
                        queue.append(new_str)
                        seen.add(new_str)
        return False