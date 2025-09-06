package q3640;
import java.util.*;
import java.util.stream.*;

public class CTJ3640 {

	public static int calPoints(List<String> ops) {
		Stack<Integer> stack = new Stack<>();
        
        for (String op : ops) {
            switch (op) {
                case "C":
                    stack.pop();
                    break;
                case "D":
                    stack.push(2 * stack.peek());
                    break;
                case "+":
                    int top = stack.pop();
                    int newTop = top + stack.peek();
                    stack.push(top);
                    stack.push(newTop);
                    break;
                default:
                    stack.push(Integer.parseInt(op));
                    break;
            }
        }
        
        int sum = 0;
        for (int score : stack) {
            sum += score;
        }
        
        return sum;

	}

	public static void main(String[] args) {
		List<String> ops = Arrays.stream(args[0].split(",")).map(s -> s).collect(Collectors.toList());
		System.out.println(calPoints(ops));
	}
}