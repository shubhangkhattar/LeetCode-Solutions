class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.dfs(0,candidates,target,[],result)
        return result

    def dfs(self, index, candidates, target, current_list, result):
        if sum(current_list) == target:
            result.append(current_list)
            return
        if sum(current_list) > target:
            return

        increased_list = current_list.copy()
        increased_list.append(candidates[index])

        self.dfs(index, candidates, target, increased_list,result)

        if index+1 < len(candidates):
            self.dfs(index+1,candidates,target,current_list,result)