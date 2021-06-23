import java.util.*;

public class Solution {
    public int[][] kClosest(int[][] points, int k) {
        int[][] ans = new int[k][2];

        PriorityQueue<int[]> pq = new PriorityQueue<int[]>(k, new Comparator<int[]>() {
            public int compare(int[] a, int[] b) {
                return (b[0]*b[0] + b[1]*b[1]) - (a[0]*a[0] + a[1]*a[1]);
            }
        });

        for(int i = 0; i < points.length; i++) {
            pq.add(points[i]);
            if(pq.size() > k) pq.poll();
        }

        while(k > 0) {
            k--;
            ans[k] = pq.poll();
        }
        return ans;
    }
}
