from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_scores = sorted(score, reverse=True)
        answer = [""] * len(score)

        for i, s in enumerate(sorted_scores):
            original_index = score.index(s)

            if i == 0:
                answer[original_index] = "Gold Medal"
            elif i == 1:
                answer[original_index] = "Silver Medal"
            elif i == 2:
                answer[original_index] = "Bronze Medal"
            else:
                answer[original_index] = str(i + 1)

        return answer
