
from traitlets import List


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        W = int(area ** 0.5)

        while area % W != 0:
            W -= 1

        L = area // W
        return [L, W]