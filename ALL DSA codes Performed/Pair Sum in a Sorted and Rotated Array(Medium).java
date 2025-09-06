package q3195;
import java.util.*;
import java.util.stream.*;

public class CTJ3195 {

	public static boolean pairInSortedRotated(List<Integer> arr, int target) {
		int n = arr.size();
        int pivot = findPivot(arr);
        int left = pivot; // Smallest element
        int right = (pivot - 1 + n) % n; // Largest element
        
        while (left != right) {
            int sum = arr.get(left) + arr.get(right);
            if (sum == target) {
                return true;
            }
            if (sum < target) {
                left = (left + 1) % n; // Move left pointer right
            } else {
                right = (right - 1 + n) % n; // Move right pointer left
            }
        }
        return false;
    }
    
    private static int findPivot(List<Integer> arr) {
        int low = 0, high = arr.size() - 1;
        while (low < high) {
            int mid = low + (high - low) / 2;
            if (arr.get(mid) > arr.get(high)) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }
        return low;

	}

	public static void main(String[] args) {
		List<Integer> arr = Arrays.stream(args[0].split(",")).map(s -> Integer.parseInt(s)).collect(Collectors.toList());
		int target = Integer.parseInt(args[1]);
		System.out.println(pairInSortedRotated(arr, target));
	}
}