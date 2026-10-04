class Solution:
    def readBinaryWatch(self, turnedOn: int) -> list[str]:
        result = []

        for hour in range(12):
            for minute in range(60):
                # Count how many LEDs are ON
                if hour.bit_count() + minute.bit_count() == turnedOn:
                    result.append(f"{hour}:{minute:02d}")

        return result