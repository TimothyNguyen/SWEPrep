public class 118PascalTriangle {
    
}
class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> solution = new ArrayList<>();
         if(numRows <= 0) return solution;
        List<Integer> row1 = new ArrayList<>();
        row1.add(1);
        solution.add(row1);
        for(int i = 2; i <= numRows; i++) {
            List<Integer> row = new ArrayList<>();
            row.add(1);
            List<Integer> prevRow = solution.get(i-2);
            for(int j = 1; j < i - 1; j++) {
                row.add(prevRow.get(j - 1) + prevRow.get(j));
            }
            row.add(1);
            solution.add(row);
        }
        return solution;
    }
}