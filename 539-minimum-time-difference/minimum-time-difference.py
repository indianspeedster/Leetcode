class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def convert(string):
            hour, minute = string.split(":")
            return (0 - (int(hour)*60 + int(minute))) 
        timepoints = [convert(string) for string in timePoints]

        timepoints.sort()
        print(timepoints)
        mini = float("inf")
        for i in range(1, len(timepoints)):
            mini = min(mini, timepoints[i]-timepoints[i-1])
        return min(mini, 1440 - timepoints[-1]+timepoints[0])
        
        