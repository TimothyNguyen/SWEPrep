import java.util.ArrayList;

class Solution {
    public String convert(String s, int numRows) {
        if(numRows <= 1) return s;
        int rowIndex = 0, stringIndex = 0;
        boolean goingDown = false;
        ArrayList<StringBuilder> rows = new ArrayList<>();
        for(int i = 0; i < numRows; i++) rows.add(new StringBuilder());
        while(stringIndex < s.length()) {
            rows.get(rowIndex).append(s.charAt(stringIndex));
            stringIndex++;
            if(rowIndex == 0 || rowIndex == numRows - 1) goingDown = !goingDown;
            rowIndex += goingDown ? 1 : -1;
        }
        StringBuilder ans = new StringBuilder();
        for(StringBuilder row : rows) ans.append(row);
        return ans.toString();
    }
}