class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(curr, open_c, close_c):
            if open_c == close_c == n:
                res.append("".join(curr))
                return   # important to stop further recursion

            if open_c < n: 
                curr.append("(")
                backtrack(curr, open_c + 1, close_c)
                curr.pop()

            if close_c < open_c:
                curr.append(")")
                backtrack(curr, open_c, close_c + 1)
                curr.pop()

        backtrack([], 0, 0)
        return res

# we didnt need an out for loop here cause there is only one valid state in our solution that is we start with open bracket
# every other starting state is invalid so only the starting state is required which is backtrack([], 0, 0)
