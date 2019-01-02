from solution import Solution
import time

# Unit testing

def test(myFunc,args,exp):
    t = myFunc(*args)
    print("Test case: {}, answer:{}, expected:{}".format(args,t,exp))
    return t

sol = Solution()
testCases = [
    (3,5,4),
    (2,6,5),
    (0,0,1),
    (1,2,3),
    (22003,31237,1)
]
expected = [
    True,
    False,
    False,
    False,
    True
]
result = list()
for i in range(len(testCases)):
    t = test(sol.canMeasureWater,testCases[i],expected[i])

print("Completed in ", time.clock()*1000, " ms");
