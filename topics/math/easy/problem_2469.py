"""
LeetCode 2469
Topic: math
Difficulty: easy
"""


class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:
        return [celsius + 273.15, celsius * 1.80 + 32.00]


if __name__ == "__main__":
    solution = Solution()
    print(solution.convertTemperature(30))  # Output: [303.15, 86.0]
