{
#Initial Template for Python 3
import atexit
import io
import sys
class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,W = map(int,input().strip().split())
        info = list(map(int,input().strip().split()))
        Items = [Item(0,0) for i in range(n)]
        for i in range(n):
            Items[i].value = info[2*i]
            Items[i].weight = info[2*i+1]
        print("%.2f" %fractionalknapsack(W,Items,n))

}
def fractionalknapsack(W,Items,n):
    '''
    :param W: max weight which can be stored
    :param Items: List contianing Item class objects as defined in driver code, with value and weight
    :param n: size of Items
    :return: Float value of max possible value, two decimal place accuracy is expected by driver code
    
    {
        class Item:
        def __init__(self,val,w):
            self.value = val
            self.weight = w
    }
    '''
    # code here
    
    Items.sort(key = lambda item: item.value/item.weight, reverse = True)
    
    s = 0
    k = 0

    while k < n:
        if W >= Items[k].weight:
            s += Items[k].value
            W -= Items[k].weight
            k += 1
        else:
            s += (Items[k].value/Items[k].weight)*W
            break
    return s
    
    
