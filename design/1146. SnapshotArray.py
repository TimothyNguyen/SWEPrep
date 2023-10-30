'''
Implement a SnapshotArray that supports the following interface:

SnapshotArray(int length) initializes an array-like data structure with the given length. Initially, each element equals 0.
void set(index, val) sets the element at the given index to be equal to val.
int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id
 
'''
class SnapshotArray:

    def __init__(self, length: int):
        self.id = 0
        self.arr = dict()
        self.snap_dict = dict()
        self.length = length

    def set(self, index: int, val: int) -> None:
        self.arr[index] = val

    def snap(self) -> int:
        self.snap_dict[self.id] = dict(self.arr)
        self.id += 1
        return self.id - 1

    def get(self, index: int, snap_id: int) -> int:
        return self.snap_dict[snap_id].get(index, 0)
    
class SnapshotArray:

    def __init__(self, length: int):
        self.cache = collections.defaultdict(lambda : collections.OrderedDict())
        self.i = 0

    def set(self, index: int, val: int) -> None:
        self.cache[index][self.i] = val
        

    def snap(self) -> int:
        self.i += 1
        return self.i - 1

    def get(self, index: int, snap_id: int) -> int:
        if index not in self.cache: return 0
        else:
            idx_cache = self.cache[index]
            if snap_id in idx_cache: 
                return idx_cache[snap_id]
            else:
                keys = list(idx_cache.keys())
                i = bisect.bisect(keys, snap_id)
                if snap_id > keys[-1]:
                    return idx_cache[keys[-1]]
                elif i == 0:
                    return 0
                else:
                    return idx_cache[keys[i-1]]



# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)