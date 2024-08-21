
#1st problem
class first:
    def firstzeroindex(arr,n):
        i=0
        while (i<n):
            if(arr[i]==0):
                return i
            i+=1
        return -1
    def main(args):
        arr=[1,1,1,1,1,0,0,0,0,0,0]
        n=len(arr)
        x=first.firstzeroindex(arr,n)
        if(x==-1):
            print("Count of zero is 0.")
        else:
            print("Count of zero is: ",end=' ')
            print(n-x)
            
if __name__=="__main__":
    first.main([])

