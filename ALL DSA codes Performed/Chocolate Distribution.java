package q3180;
import java.util.*;
import java.util.stream.*;

public class CTJ3180 {

	public static int findMinDiff(List<Integer> arr, int m) {
		if (arr == null || arr.size() == 0 || m == 0) {
            return 0;
        }
        
        Collections.sort(arr);
        
        if (m > arr.size()) {
            return -1; 
        }
        
        int minDiff = Integer.MAX_VALUE;
        
        for (int i = 0; i + m - 1 < arr.size(); i++) {
            int currentDiff = arr.get(i + m - 1) - arr.get(i);
            if (currentDiff < minDiff) {
                minDiff = currentDiff;
            }
        }
        
        return minDiff;

	}

	public static void main(String[] args) {
		List<Integer> arr = Arrays.stream(args[0].split(",")).map(s -> Integer.parseInt(s)).collect(Collectors.toList());
		int m = Integer.parseInt(args[1]);
		System.out.println(findMinDiff(arr, m));
	}
}