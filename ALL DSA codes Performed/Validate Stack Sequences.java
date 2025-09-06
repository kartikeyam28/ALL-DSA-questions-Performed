package q3651;
import java.util.*;
import java.util.stream.*;

public class CTJ3651 {

	public static boolean validateStackSequences(List<Integer> pushed, List<Integer> popped) {
		Stack<Integer> stack = new Stack<>();
		int popIndex = 0;
		for (int num : pushed){
			stack.push(num);
			while(!stack.isEmpty() && stack.peek() == popped.get(popIndex)){
				stack.pop();
				popIndex++;
			}
		}
		return stack.isEmpty();
	}

	public static void main(String[] args) {
		List<Integer> pushed = Arrays.stream(args[0].split(",")).map(s -> Integer.parseInt(s)).collect(Collectors.toList());
		List<Integer> popped = Arrays.stream(args[1].split(",")).map(s -> Integer.parseInt(s)).collect(Collectors.toList());
		System.out.println(validateStackSequences(pushed, popped));
	}
}