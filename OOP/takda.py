class Solution:
  def letterCasePermutation(self, S):
    ans = []
    def dfs(S, i, n):
      if i == n:
        ans.append(''.join(S))
        return
      
      dfs(S, i + 1, n)      
      if not S[i].isalpha(): return      
      S[i] = chr(ord(S[i]) ^ (1<<5))
      dfs(S, i + 1, n)
      S[i] = chr(ord(S[i]) ^ (1<<5))
    
    dfs(list(S), 0, len(S))
    return(ans)


a=Solution()
	
print(a.letterCasePermutation("da2da2ja8"))

print("=====================")

#824
class Solution2:
    def toGoatLatin(self, S):
        def convert(S):
            for i, word in enumerate(S.split(), 1):
                if word[0] not in 'aeiouAEIOU':
                    word = word[1:] + word[:1]
                yield word + 'ma' + 'a'*i
        return " ".join(convert(S))


b=Solution2()
print(b.toGoatLatin("Hello every one my name is pukich"))
