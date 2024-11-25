class Solution:
    def slidingPuzzle(self, b: List[List[int]]) -> int:
        v = {}
        @cache
        def f(s,i,j,k,r):
            if(s:=''.join(s[{i:j,j:i}.get(k,k)]for k in range(len(s))))=='123450':
                return k
            if k<r and k<v.get(s,inf):
                v[s] = k
                return min(f(s,j,z,k+1,r)for z in{0:(1,3),1:(0,2,4),2:(1,5),3:(0,4),4:(3,5,1),5:(4,2)}[j])
            return r            
        return(-1,t:=f(s:=''.join(map(str,sum(b,[]))),i:=s.find('0'),i,0,inf))[t<inf]


                
                    
        