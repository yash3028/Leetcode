class Solution:
    def reverseParentheses(self, s: str) -> str:
        # to store characters without parentheses
        ans = []
        # to stores start indices of start paranthesis
        st = []

        for ch in s:
            if ch == "(":
                # find wheere bracket starts 
                st.append(len(ans))
            elif ch == ")":
                left = st.pop()
                # end of current substring
                right = len(ans) - 1

                while left < right:
                    # reverse the substring
                    ans[left], ans[right] = (
                        ans[right],
                        ans[left],
                    )
                    left += 1
                    right -= 1
            else:
                ans.append(ch)

        return "".join(ans)

ans = Solution().reverseParentheses("(abcd)")
print(ans)