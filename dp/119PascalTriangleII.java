public class 119PascalTriangleII {
    
}
class Solution {
    public List<Integer> getRow(int rowIndex) {
        List<Integer> solution = new ArrayList<>();
        if(rowIndex < 0) return solution;
        for(int i = 0; i < rowIndex + 1; i++) {
            solution.add(0, 1);
            for(int j = 1; j < solution.size() - 1; j++) {
                solution.set(j, solution.get(j) + solution.get(j + 1));
            }
        }
        return solution;
    }
}