from queue import Queue

class Solution(object):
    def measureHelper(self,cx,mx,cy,my,z,visited,Q):
        visited[cy][cx] = True
        if(cx == z or cy == z or cx+cy == z):
            print("measureHelper return True")
            return True
        else:
            Q.put((mx,mx,cy,my,z,visited,Q))
            Q.put((cx,mx,my,my,z,visited,Q))
            Q.put((0,mx,cy,my,z,visited,Q))
            Q.put((cx,mx,0,my,z,visited,Q))
            t = cx+cy
            y2x = min(mx,t)
            x2y = min(my,t)
            Q.put((y2x,mx,t-y2x,my,z,visited,Q))
            Q.put((t-x2y,mx,x2y,my,z,visited,Q))
        print("measureHelper return False")
        return False

    def canMeasureWater(self, x, y, z):
        visited = [[False for i in range(x+1)] for j in range(y+1)]
        Q = Queue()
        Q.put((0,x,0,y,z,visited,Q))
        while(not Q.empty()):
            args = Q.get()
            print(args[:-2])
            cx,cy = args[0],args[2]
            if not visited[cy][cx]:
                r = self.measureHelper(*args)
                if r:
                    print("canMeasureWater return True")
                    return True
        print("canMeasureWater return False")
        return False
