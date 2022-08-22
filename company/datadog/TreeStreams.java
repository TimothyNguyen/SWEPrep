package company.datadog;
import java.util.*;


/*
Complexity analysis
Extracting the min element from a k-element heap, takes lgn => for n elements, O(nlgk)
*/
class StreamNumber implements Comparable<StreamNumber> {
    int value;
    int streamNo;

    public StreamNumber(int v, int n) {
        value = v;
        streamNo = n;
    }

    public int compareTo(StreamNumber other) {
        return this.value - other.value;
    }
    
    class TreeStreams {
        private PriorityQueue<StreamNumber> pq;
        private List<List<Integer>> streams;

        public TreeStreams(List<List<Integer>> s) {
            streams = s;

            pq = new PriorityQueue<>();

            for(int i = 0; i < streams.size(); i++) {
                pq.add(new StreamNumber(streams.get(i).get(0), i));
                streams.get(i).remove(0);
            }
        }

        public int read() {
            if(pq.isEmpty()) return -1;
        
            StreamNumber number = pq.poll();
        
            if(streams.get(number.streamNo).size() >= 1) {
                pq.add(new StreamNumber(streams.get(number.streamNo).get(0), number.streamNo));
                streams.get(number.streamNo).remove(0);
            }
            return number.value;
        }
    }
}