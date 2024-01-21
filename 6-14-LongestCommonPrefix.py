

def longestCommonPrefix(strs):
        
        res = strs[0]
        for string in strs:
            newRes = ""
            base = strs[0]
            compare = string
            if len(string) > len(base):
                compare, base = base, compare

            for i in range(0, len(compare)):
                if compare[i] != base[i]:
                    break
                if compare[i] == base[i]:  
                    newRes += compare[i]
                
            if len(newRes) <= len(res):
                res = newRes
            
        return res
            

strs = ["flower","flow","flight"]
# Output: "fl"

print(longestCommonPrefix(strs))

