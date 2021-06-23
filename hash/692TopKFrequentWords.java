import java.util.*;

class Solution {
    public List<String> topKFrequent(String[] words, int k) {
        Map<String, Integer> map = new HashMap<>();
        for(int i = 0; i < words.length; i++) {
            map.put(words[i], map.getOrDefault(words[i], 0) + 1);
        }
        List<String> candidates = new ArrayList<>(map.keySet());
        Collections.sort(candidates, (w1, w2) -> map.get(w1).equals(map.get(w2)) ?
        w1.compareTo(w2) : map.get(w2) - map.get(w1));
        return candidates.subList(0, k);
    }
}