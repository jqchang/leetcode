from solution import Solution
import time

# Unit testing

def test(myFunc,args,exp):
    t = myFunc(*args)
    match = t==exp
    if not match:
        print("Mismatch for test case",args,"- encountered",t,"expected",exp)
    return match

sol = Solution()
testCases = [
    (3,4,5),
    (2,6,5),
]
expected = [
    True,
    False,
]
result = list()
for i in range(len(testCases)):
    result.append(test(sol.canMeasureWater,testCases[i],expected[i]))

print("Completed in ", time.clock()*1000, " ms");
