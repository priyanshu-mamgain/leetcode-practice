class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        cleaned = s.replace("-", "").upper()

        groups = []
        i = len(cleaned)

        while i > 0:
            start = max(0, i - k)
            groups.append(cleaned[start:i])
            i -= k

        groups.reverse()
        return "-".join(groups)