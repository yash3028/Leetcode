class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)
        word = ["0"] * (n+m-1)
        print(word)
        for i in range(n):
            if str1[i]=="T":
                for j in range(m):
                    if word[i+j]=="0" or word[i+j]==str2[j]:
                        word[i+j]=str2[j]
                    else:
                        return ""
        
        for i in range(len(word)):
            if word[i]=="0":
                word[i]="a"

        for i in range(n):
            if str1[i]=="F":
                if ''.join(word[i:i+m])==str2:
                    for j in range(m-1,-1,-1):
                        if word[i+j]!="z":
                            word[i+j]=chr(ord(word[i+j])+1)
                            break
                        else: 
                            return ""
        return "".join(word)
                        

ans = Solution().generateString("TTFFT","fff")
print(ans)