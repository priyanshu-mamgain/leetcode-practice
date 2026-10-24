class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def get_day(date):
            month = int(date[:2])
            day = int(date[3:])

            total = day
            for i in range(month - 1):
                total += days_in_month[i]

            return total

        start = max(get_day(arriveAlice), get_day(arriveBob))
        end = min(get_day(leaveAlice), get_day(leaveBob))

        return max(0, end - start + 1)
