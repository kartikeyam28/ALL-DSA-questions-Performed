package q3656;
import java.util.*;
import java.util.stream.*;

public class CTJ3656 {

	public static List<Integer> twoSum(List<Integer> nums, int target) {
		Map<Integer, Integer> numMap = new HashMap<>();
        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums.get(i);
            if (numMap.containsKey(complement)) {
                return Arrays.asList(numMap.get(complement), i);
            }
            numMap.put(nums.get(i), i);
        }
        // As per problem statement, this line should never be reached
        return Collections.emptyList();

	}

	public static void main(String[] args) {
		List<Integer> nums = Arrays.stream(args[0].split(",")).map(s -> Integer.parseInt(s)).collect(Collectors.toList());
		int target = Integer.parseInt(args[1]);
		System.out.println(twoSum(nums, target).stream().map(String::valueOf).collect(Collectors.joining(",")));
	}
}