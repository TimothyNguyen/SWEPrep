import java.util.*;
public class FillTheTruck { 
	ArrayList<Integer> IDsOfPackages(int truckSpace, 
	                                 ArrayList<Integer> packagesSpace)
	{
		Map<Integer, Integer> map = new HashMap<>();
		int max = Integer.MIN_VALUE;
		truckSpace -= 30;
		ArrayList<Integer> list = new ArrayList<>();
		for(int i = 0; i < packagesSpace.size();i++) {
		    int val = packagesSpace.get(i);
		    if(map.containsKey(truckSpace-val)) {
		        int cMax = val > truckSpace-val ? val : truckSpace-val;
		        if(cMax > max) {
		            max = cMax;
		            list = new ArrayList<>();
		            list.add(map.get(truckSpace-val));
		            list.add(i);
		        }
		    }
		    map.putIfAbsent(val,i);
		}
		return list;
	}
	
}