class Solution:
    def romanToInt(self, s: str) -> int:
        numerals = {
            "I":     1,
            "II":    2,
            "III":   3,
            "IV":    4,
            "V":     5,
            "VI":    6,
            "VII":   7,
            "VIII":  8,
            "IX":    9,
            "X":     10,
            "L":     50,
            "C":     100,
            "D":     500,
            "M":     1000,
        }

        total = 0
        temp = 0  

        for i, num in enumerate(s):
            # If this is the last character
            if i + 1 >= len(s):
                total += numerals[num]
                break

            next_int = s[i + 1]

            # Subtractive case
            if numerals[num] < numerals[next_int]:
                total -= numerals[num]
            else:
                total += numerals[num]

        return total
