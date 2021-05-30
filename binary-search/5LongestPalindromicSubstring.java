class Solution {
    public String longestPalindrome(String s) {
        if(s == null || s.length() < 1) return "";
        int l = 0, r = 0;
        for(int i = 0; i < s.length(); i++) {
            int len1 = expandAroundCenter(i, i, s);
            int len2 = expandAroundCenter(i, i + 1, s);
            int len = Math.max(len1, len2);
            if(len > r - l) {
                l = i - (len - 1) / 2;
                r = i + len / 2;
            }
        }
    }

    public int expandAroundCenter(int l, int r, String s) {
        while(l >= 0 && r < s.length() && s.charAt(l) == s.charAt(r)) {
            l++;
            r--;
        }
        return r - l - 1;
    }
}