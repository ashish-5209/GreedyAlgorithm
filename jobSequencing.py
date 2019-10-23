{
#Initial Template for Python 3
import atexit
import io
import sys
class Job:
    '''
    Job class which stores profit and deadline.
    '''
    def __init__(self,profit=0,deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        info = list(map(int,input().strip().split()))
        Jobs = [Job() for i in range(n)]
        for i in range(n):
            Jobs[i].id = info[3*i]
            Jobs[i].deadline = info[3 * i + 1]
            Jobs[i].profit=info[3*i+2]
        maxProfit(Jobs,n)
}
def maxProfit(Jobs,n):
    '''
    :param Jobs: list of "Job" class defined in driver code, with "profit" and "deadline".
    :param n: total number of jobs
    :return: None, print the count of jobs done and maximum profit
    '''
    '''
    {
        class Job:.
        def __init__(self,profit=0,deadline=0):
            self.profit = profit
            self.deadline = deadline
            self.id = 0
    }
    '''
    # code here
    
    # Sorting the Jobs w.r.t Profit in decreasing Order
    
    Jobs.sort(key = lambda item: item.profit, reverse = True)
    
    m = 0
    for i in range(n):
        m = max(m, Jobs[i].deadline)
        
    result = [0]*m
    s = 0
    
    for i in range(n):
        r = Jobs[i].deadline-1
        while r >= 0:
            if result[r] == 0:
                s += 1
                result[r] = Jobs[i].profit
                break
            r -= 1
                    
    print(s, sum(result))
