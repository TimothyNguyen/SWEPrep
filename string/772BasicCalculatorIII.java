class Solution {
    // recursive Time and Space O(N)
    int i = 0;
    public int calculate(String s) {
        if (s == null || s.length() == 0) return 0;
        int result = 0, tmp = 0, num = 0;
        char op = '+';
        
        while (i < s.length()) {
            char c = s.charAt(i++);
            if (Character.isDigit(c)) {
                tmp = tmp * 10 + c - '0';
            } else if (c == '(') {
                tmp = calculate(s);     // string parse index is tracked by i
            } else if (c == ')') {
                break;
            } else if (c != ' ') {
                //process the numerical value of string so far; based on what 'op' we have before it
                num = cal(num, tmp, op);
                if (c == '+' || c == '-') {
                    result += num;
                    num = 0;
                }
                //reset 'tmp' and op for next character  processing
                tmp = 0;
                op = c;
            }
        }
        return result + cal(num, tmp, op);
    }
    private int cal(int num, int tmp, char op) {
        if (op == '+') return num + tmp;
        else if (op == '-') return num - tmp;
        else if (op == '*') return num * tmp;
        else return num / tmp;
    }
}