class Solution {
    public int lengthOfLongestSubstring(String s) {
        char[] arr = new char[128];
        int l = 0, r = 0;
        int res = 0;
        while(r < s.length()) {
            char rChar = s.charAt(r);
            arr[rChar]++;
            
            while(arr[rChar] > 1) {
                char lChar = s.charAt(l);
                arr[lChar]--;
                l++;
            }
            
            res = Math.max(res, r - l + 1);
            r++;
        }
        return res;
    }

    public int lengthOfLongestSubstring2(String s) {
        int n = s.length(), ans = 0;
        Map<Character, Integer> map = new HashMap<>();
        for(int r = 0, l = 0; r < s.length(); r++) {
            if(map.containsKey(s.charAt(r))) {
                l = Math.max(map.get(s.charAt(r)), l);
            }
            ans = Math.max(ans, r - l + 1);
            map.put(s.charAt(r));
        }
        return ans;
    }
}