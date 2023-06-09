class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l,h = 0, len(letters)-1
        smallest = 200
        arr=letters
        while l<=h:
            mid = (l+h)//2
            if arr[mid]>target:
                smallest = min(smallest,ord(arr[mid]))
                h = mid-1
            else:
                l = mid+1
        return chr(smallest) if smallest != 200 else arr[0]
                
            
        