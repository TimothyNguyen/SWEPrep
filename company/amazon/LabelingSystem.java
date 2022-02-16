/*
Labeling System
Amazon is looking to develop a new labeling system in the fulfilment 
centers. New labels will be devised from the original string labels.
Given the original string label, construct a new string by rearranging 
the original string and deleting characters as needed. Return the 
alphabetically-largest string that can be constructed respecting the 
limit as to how many consecutive characters can be the same (represented by k).

"Alphabetically-largest" is defined in reverse alphabetical order (e.g., 
b is "larger" than a, c is "larger" than b, etc.) from left to right (e.g., 
"ba" is larger than "ab").

Write an algorithm to return the alphabetically-largest string that can 
be constructed respecting the above limits.

Input
The input to the function/method consists of two arguments:
originalLabel, a string representing the original string label;
charLimit, an integer representing the maximum number of identical consecutive 
characters the new string can have (k).

Output
Return a string representing the alphabetically largest string that can be 
constructed that has no more than k identical consecutive characters.
*/

public class LabelingSystem {
    public static String getLargestString(String origin, int k) {
        int[] board = new int[26];
        for(char c : origin.toCharArray()) {
            board[c-'a']++;
        }    
        StringBuilder sb = new StringBuilder();
        int index = 25;
        int lastCount = 0;
        while(index >= 0) {
            if(board[index] == 0) {
                index--;
                lastCount = 0;
                continue;
            }
            if(lastCount < k) {
                sb.append((char)('a'+index));
                lastCount++;
                board[index]--;
            } else {
                for(int i = index - 1; i >= 0; i--) {
                    if(board[i] > 0) {
                        sb.append((char)('a'+i));
                        board[i]--;
                        lastCount = 0;
                        break;
                    }
                }
                if(lastCount != 0) break;
            }
        }
        return sb.toString();
    }
}

/*
import collections
def largestAlphabeticalString(label, k):
    flippedLabel = sorted(label, reverse=True)
    counter = collections.Counter(flippedLabel)
    out = []
    for c,v in counter.items():
        out.append(c*min(k, v))
    
    return "".join(out)
*/