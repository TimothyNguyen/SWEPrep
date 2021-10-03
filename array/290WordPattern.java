public class 290WordPattern {

    /**
     * Given a pattern and a string s, find if s follows the same pattern.
     * 
     * Input: pattern = "abba", s = "dog cat cat dog"
     * Output: true
     */
    public boolean wordPattern(String pattern, String s) {
        HashMap<String, Character> m1 = new HashMap<>();
        HashMap<Character, String> m2 = new HashMap<>();

        String[] words = s.split(" ");
        if(words.length != pattern.length()) return false;
        for(int i = 0; i < pattern.length(); i++) {
            if(!m1.containsKey(words[i])) {
                if(!m2.containsKey(pattern.charAt(i))) {
                    m1.put(words[i], pattern.charAt(i));
                    m2.put(pattern.charAt(i), words[i]);
                } else return false;
            } else {
                if(!m2.containsKey(pattern.charAt(i))) return false;
                if(m1.get(words[i]) != pattern.charAt(i)) return false;
            }
        }
        return true;
    }
}
