import java.util.*;

public class FindRelatedProducts {
    List<String> res = new ArrayList<>();

    public List<String> findLargestGroup(List<List<String>> items) {
        Map<String, Set<String>> map = new HashMap<>();
        Set<String> keys = new HashSet<>();
        for (List<String> lst : items) {
            keys.addAll(lst);
            for (int i = 1; i < lst.size(); i++) {
                map.putIfAbsent(lst.get(i), new HashSet<>());
                map.putIfAbsent(lst.get(i - 1), new HashSet<>());
                map.get(lst.get(i - 1)).add(lst.get(i));
                map.get(lst.get(i)).add(lst.get(i - 1));
            }
        }
        Set<String> visited = new HashSet<>();

        for (String k : keys) {
            if (!visited.contains(k)) {
                List<String> lst = new ArrayList<>();
                dfs(map, visited, k, lst);
                if (lst.size() > res.size()) {
                    res = lst;
                }
            }
        }
        return res;
    }

    void dfs(Map<String, Set<String>> map, Set<String> visited, String k, List<String> lst) {
        if (!visited.add(k))
            return;
        lst.add(k);
        for (String nei : map.getOrDefault(k, new HashSet<>())) {
            dfs(map, visited, nei, lst);
        }
    }
}
