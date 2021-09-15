/*
As pointed out in other solutions, without loss of generality because of the symmetry of the board, we can assume the target is in the upper right quadrant. So take absolute values of x and y for the target.

Compute the possible moves from the target at (|x|, |y|) to (0, 0). There are 2 possible moves towards (0, 0): (x-1, y-2) or (x-2, y-1).

If target and destination are both (0, 0) then x+y == 0 and we need 0 moves.
If either x or y == 2, then target and origin are on the same vertical or horizontal line, and we can get there in 2 moves (notice by observation of the board).

Code is as follows.
*/
class Solution {
    private Map<String, Integer> cache = new HashMap<>();
    
    public int minKnightMoves(int x, int y) {
        x = Math.abs(x);
        y = Math.abs(y);
        
        // Could use a StringBuilder here for better performance
        String key = x + "," + y;
        
        if(cache.containsKey(key)) {
            return cache.get(key);
        }
       
        if(x+y == 0 || x+y == 2) {
            cache.put(key, x+y);
            return x+y;
        }
        
        int answer = Math.min(minKnightMoves(x-2, y-1), minKnightMoves(x-1, y-2)) + 1;
        cache.putIfAbsent(key, answer);
        
        return answer;
    }
}

/*
class Solution {
    public int minKnightMoves(int x, int y) {
        Queue<int[]> queue = new LinkedList<>();
        HashMap<Integer, Set<Integer>> visited = new HashMap<>();
        if(x == 0 && y == 0) return 0;
        int[] initial = {0, 0};
        queue.add(initial);
        int levels = -1;
        while(queue.size() > 0) {
            int l = queue.size();
            levels++;
            for(int i = 0; i < l; i++) {
                int[] arr = queue.poll();
                if(x == arr[0] && y == arr[1]) return levels;
                int newX = arr[0], newY = arr[1];
                if(Math.abs(newX) + Math.abs(newY) > 300) continue;
                int[][] newDir = {{newX-2, newY - 1},
                                  {newX-2, newY + 1},
                                  {newX-1, newY - 2},
                                  {newX-1, newY + 2},
                                  {newX+1, newY - 2},
                                  {newX+1, newY + 2},
                                  {newX+2, newY - 1},
                                  {newX+2, newY + 1}};
                for(int j = 0; j < newDir.length; j++) {
                    if(!visited.containsKey(newDir[j][0])) {
                        HashSet<Integer> set = new HashSet<>();
                        visited.put(newDir[j][0], set);
                    } 
                    if(!visited.get(newDir[j][0]).contains(newDir[j][1])) {
                        visited.get(newDir[j][0]).add(newDir[j][1]);
                        queue.add(newDir[j]);
                    } 
                }
            }
        }
        return -1;
    } 
}
*/