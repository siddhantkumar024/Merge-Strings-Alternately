class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        j1=len(word1)
        j2=len(word2)
        d=min(j1,j2)
        i,j=0,0
        m=[]
        while i<d and j<d:
            m.append(word1[i])
            m.append(word2[j])
            i+=1
            j+=1
        if j1==d:
            for n in word2[d:]:
                m.append(n)
        if j2==d:
            for n in word1[d:]:
                m.append(n)
        return ''.join(m)
        


        
