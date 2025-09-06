package q3179;
import java.util.*;
import java.util.stream.*;

public class CTJ3179 {

	public static boolean containDuplicates(List<Integer> nums) {
		Set<Integer> seen = new HashSet<>();
		for (int num : nums) {
			if (seen.contains(num)) {
				return true;
			
			}
			seen.add(num);
		}
		return false;

	}

	public static void main(String[] args) {
		List<Integer> nums = Arrays.stream(args[0].split(",")).map(s -> Integer.parseInt(s)).collect(Collectors.toList());
		System.out.println(containDuplicates(nums));
	}
}