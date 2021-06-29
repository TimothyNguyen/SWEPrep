/* The knows API is defined in the parent class Relation.
      boolean knows(int a, int b); */

public class Solution extends Relation {
    
    private int numberOfPeople;
    
    public int findCelebrity(int n) {
        numberOfPeople = n;
        int cand = 0;
        for(int i = 0; i < n; i++) 
            if(knows(cand, i)) 
                cand = i;
        if(isCelebrity(cand)) return cand;
        return -1;
    }

    private boolean isCelebrity(int i) {
        for(int j = 0; j < numberOfPeople; j++) {
            if(i == j) continue;
            if(knows(i, j) || !knows(j, i)) return false;
        }
        return true;
    }
}

/*
Input: graph = [[1,1,0],[0,1,0],[1,1,1]]
Output: 1
Explanation: There are three persons labeled with 0, 1 and 2. graph[i][j] = 1 
means person i knows person j, otherwise graph[i][j] = 0 means person i does 
not know person j. The celebrity is the person labeled as 1 because both 
0 and 2 know him but 1 does not know anybody.
*/