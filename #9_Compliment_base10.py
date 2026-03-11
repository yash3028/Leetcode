class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        # convert number into binary from
        b = bin(n)[2:]     
        comp = ""
        # compliment of binary value
        for bit in b:
            if bit == '0':
                comp += '1'
            else:
                comp += '0'
        # convert compliment binary into number
        return int(comp, 2)  
    
ans = Solution().bitwiseComplement(5)
print(ans)