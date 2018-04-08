class Solution:
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        ans=0
        for i in range(0,min(len(A),len(B))):
            l1 = []
            for j in range(0,len(B)):
                if i+j >= len(A):
                    break
                l1.append(A[i+j]-B[j])
            #print(l1)
            c1=0
            max1=0
            flag1=False
            for j in range(0,len(l1)):
                if (l1[j]==0 and j+1==len(l1)) or (l1[j]==0 and l1[j+1]==0):
                    c1+=1
                elif l1[j]==0 and j+1<len(l1) and l1[j+1]!=0:
                    c1+=1
                    if max1<c1:
                        max1=c1
                else:
                    c1=0
            if max1<c1:
                max1=c1
            l2 = []
            for j in range(0,len(A)):
                if i+j >= len(B):
                    break
                l2.append(B[i+j]-A[j])
            #print(l2)
            c2=0
            max2=0
            flag2=False
            for j in range(0,len(l2)):
                if (l2[j]==0 and j+1==len(l2)) or (l2[j]==0 and l2[j+1]==0):
                    c2+=1
                elif l2[j]==0 and j+1<len(l2) and l2[j+1]!=0:
                    c2+=1
                    if max2<c2:
                        max2=c2
                else:
                    c2=0
            if max2<c2:
                max2=c2
            if max2>max1:
                if ans<max2:
                    ans=max2
            else:
                if ans<max1:
                    ans=max1
            #print(max1)
            #print(max2)
            #print()
        return ans
