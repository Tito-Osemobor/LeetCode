class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        listOfLists = []
        dictionaryOfDictionaries = {} # maps index of listOfLists to character count dict
        for s in strs:
            found = False
            # Create character count for current string
            current_count = {}
            for char in s:
                current_count[char] = current_count.get(char, 0) + 1
            
            # Check against existing groups
            for i in range(len(listOfLists)):
                if current_count == dictionaryOfDictionaries[i]:
                    listOfLists[i].append(s)
                    found = True
                    break
            
            if not found:
                dictionaryOfDictionaries[len(listOfLists)] = current_count
                listOfLists.append([s])
        return listOfLists