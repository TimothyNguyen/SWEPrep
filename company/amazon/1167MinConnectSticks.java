class Solution {
    public int connectSticks(int[] sticks) {
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        int minCost = 0;
        for(int stick : sticks){
            minHeap.add(stick);
        }
        while(minHeap.size() > 1){
            int s1 = minHeap.poll();
            int s2 = minHeap.poll();
            int cost = s1 + s2;
            minHeap.add(cost);
            minCost = minCost + cost;
        }
        return minCost;
    }
}