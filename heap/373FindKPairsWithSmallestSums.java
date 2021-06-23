import java.util.*;

class Solution {
    public List<List<Integer>> kSmallestPairs(int[] nums1, int[] nums2, int k) {
        //max heap
        PriorityQueue<List<Integer>> maxHeap = new PriorityQueue<List<Integer>>(
            (b, a) -> ((a.get(0) + a.get(1)) - (b.get(0) + b.get(1))));
        for(int i = 0; i < nums1.length; i++) {
            for(int j = 0; j < nums2.length; j++) {
                maxHeap.add(Arrays.asList(nums1[i], nums2[j]));
                if(maxHeap.size() > k) maxHeap.poll();
            }
        }
        return new ArrayList<>(maxHeap);
    }   

    public List<List<Integer>> kSmallestPairs2(int[] nums1, int[] nums2, int k) {
        int n = nums1.length;
        int m = nums2.length;
        List<List<Integer>> ans = new ArrayList();
        
        if (n == 0 || m == 0) {
            return ans;
        }
        
        PriorityQueue<int[]> pq = new PriorityQueue(new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return (nums1[o1[0]] + nums2[o1[1]]) - (nums1[o2[0]] + nums2[o2[1]]);
            }
        });
        
        for (int i = 0; i < Math.min(k, n); i++) {
            pq.add(new int[]{i, 0});
        }
        
        for (int i = 0; i < Math.min(k, n*m); i++) {
            int[] pair = pq.remove();
            
            if (pair[1] < m - 1) {
                pq.add(new int[]{pair[0], pair[1]+1});
            }
            
            List<Integer> subsolution = new ArrayList();
            subsolution.add(nums1[pair[0]]);
            subsolution.add(nums2[pair[1]]);
            ans.add(subsolution);
        }
        
        return ans;
    }
}