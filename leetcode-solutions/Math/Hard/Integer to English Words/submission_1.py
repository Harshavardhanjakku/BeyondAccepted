# Problem: Integer to English Words
# Difficulty: Hard
# Topic: Math
# Language: python
# Submission: 1

class Solution(object):
    def numberToWords(self, n):
        """
        :type num: int
        :rtype: str
        """

        ones = {
            0: "",
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine"
        }

        teens = {
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen"
        }

        tens = {
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety"
        }

        def convert(x):
            s = ""

            hundred = x // 100
            x %= 100

            if hundred:
                s += ones[hundred] + " Hundred "

            if x:
                if x < 10:
                    s += ones[x]
                elif x < 20:
                    s += teens[x]
                else:
                    s += tens[(x // 10) * 10]
                    if x % 10:
                        s += " " + ones[x % 10]

            return s.strip()

        if n == 0:
            return "Zero"

        ans = ""

        billion = n // 1000000000
        n %= 1000000000

        million = n // 1000000
        n %= 1000000

        thousand = n // 1000
        n %= 1000

        if billion:
            ans += convert(billion) + " Billion "

        if million:
            ans += convert(million) + " Million "

        if thousand:
            ans += convert(thousand) + " Thousand "

        if n:
            ans += convert(n)

        return ans.strip()
