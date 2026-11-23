from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        gruppi = defaultdict(list)
        
        for string in strs:
            chiave = "".join(sorted(string))
            gruppi[chiave].append(string)
            
        return list(gruppi.values())
