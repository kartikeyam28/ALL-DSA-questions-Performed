package q3634;
import java.util.*;
import java.util.stream.*;

public class CTJ3634 {

	public static List<Integer> nextGreaterElement(List<Integer> nums1, List<Integer> nums2) {
		Map<Integer, Integer> map = new HashMap<>();
        Stack<Integer> stack = new Stack<>();

        for (int num : nums2) {
            while (!stack.isEmpty() && stack.peek() < num) {
                map.put(stack.pop(), num);
            }
            stack.push(num);
        }

        List<Integer> result = new ArrayList<>();
        for (int num : nums1) {
            result.add(map.getOrDefault(num, -1));
        }
        return result;

	}

	public static void main(String[] args) {
		List<Integer> nums1 = Arrays.stream(args[0].split(",")).map(s -> Integer.parseInt(s)).collect(Collectors.toList());
		List<Integer> nums2 = Arrays.stream(args[1].split(",")).map(s -> Integer.parseInt(s)).collect(Collectors.toList());
		System.out.println(nextGreaterElement(nums1, nums2).stream().map(String::valueOf).collect(Collectors.joining(",")));
	}
}