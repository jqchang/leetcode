from queue import Queue

class Solution(object):
    def measureHelper(self,cx,mx,cy,my,z,visited,Q):
        visited.add((cx,cy))
        if(cx == z or cy == z or cx+cy == z):
            return True
        else:
            Q.put((mx,cy))
            Q.put((cx,my))
            Q.put((0,cy))
            Q.put((cx,0))
            t = cx+cy
            y2x = min(mx,t)
            x2y = min(my,t)
            Q.put((y2x,t-y2x))
            Q.put((t-x2y,x2y))
        return False

    def canMeasureWater(self, x, y, z):
        visited = set()
        Q = Queue()
        Q.put((0,0))
        while(not Q.empty()):
            cx,cy = Q.get()
            if (cx,cy) not in visited:
                r = self.measureHelper(cx,x,cy,y,z,visited,Q)
                if r:
                    return True
        return False
