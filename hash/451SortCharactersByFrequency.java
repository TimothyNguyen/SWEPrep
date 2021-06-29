import java.util.Map;
import java.util.PriorityQueue;

public class SortCharactersByFrequency {
    public String frequencySort(String s) {
        PriorityQueue<Map.Entry<Character, Integer>> maxHeap = 
            new PriorityQueue<>((a, b) -> b.getValue() - a.getValue());
        Map<Character, Integer> map = new HashMap<>();
        for(int i = 0; i < s.length(); i++) map.put(s.charAt(i), map.getOrDefault(s.charAt(i), 0) + 1);
        maxHeap.addAll(map.entrySet());
        StringBuilder sb = new StringBuilder();
        while(maxHeap.size() > 0) {
            Map.Entry<Character, Integer> e = maxHeap.remove();
            for(int i = 0; i < e.getValue(); i++) sb.append(e.getKey());
        }
        return sb.toString();
    }
}
