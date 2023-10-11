class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = []

        def dfs(index,current_list):
            if sum(current_list) == target:
                result.append(current_list)
                return
            if sum(current_list) >= target:
                return 

            
            
            list_copy = current_list.copy()
            current_list.append(candidates[index])
            dfs(index,current_list)

            if index+1 < len(candidates):
                dfs(index+1,list_copy)

        dfs(0,[])

        return result

