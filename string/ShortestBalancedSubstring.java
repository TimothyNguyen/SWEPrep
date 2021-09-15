import java.util.HashSet;
import java.util.Set;

public class ShortestBalancedSubstring {

  public static void main(String[] args) {
    test("ABcabbCa", "ABcabbC");
    test("azABaabza", "ABaab");
    test("CATattac", "ATat");
    test("TacoCat", "-1");
    test("Madam", "-1");
    test("AcZCbaBz", "AcZCbaBz");
    test("aZABcabbCa", "ABcabbC");
  }

  private static void test(String s, String e) {
    ShortestBalancedSubstring shortestBalancedSubstring = new ShortestBalancedSubstring();
    String result = shortestBalancedSubstring.find(s);
    System.out.println(result);
    assert result.equals(e);
  }

  public String find(String str) {
    int len = str.length();
    Set<Character> set1, set2;

    for (int j = 1; j <= len; j++) {
      for (int i = 0; i < j; i++) {
        set1 = new HashSet<>();
        set2 = new HashSet<>();

        String tempStr = str.substring(i, j);

        for (char ch : tempStr.toCharArray()) {
          if (Character.isLowerCase(ch)) {
            set1.add(ch);
          } else {
            set2.add(Character.toLowerCase(ch));
          }
        }

        if (equals(set1, set2)) {
          return tempStr;
        }
      }
    }

    return "-1";
  }

  private boolean equals(Set<Character> set1, Set<Character> set2) {
    if (set1.size() != set2.size()) {
      return false;
    }

    for (Character c : set1) {
      if (!set2.contains(c)) {
        return false;
      }
    }

    return true;
  }
}