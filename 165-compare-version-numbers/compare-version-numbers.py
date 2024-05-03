class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1 = version1.split(".")
        ver2 = version2.split(".")
        start = 0
        while start < len(ver1) and start < len(ver2):
            if int(ver1[start]) < int(ver2[start]):
                return -1
            elif int(ver1[start]) > int(ver2[start]):
                return 1
            start += 1
        while start < len(ver1):
            if int(ver1[start]) > 0 :
                return 1
            start += 1
        while start < len(ver2):
            if int(ver2[start]) > 0 :
                return -1
            start += 1
        return 0


        