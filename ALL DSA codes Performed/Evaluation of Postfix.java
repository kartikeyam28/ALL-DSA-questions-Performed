package q3649;
import java.util.*;
import java.util.stream.*;

public class CTJ3649 {

	public static int evalRPN(List<String> tokens) {
		Stack<Integer> stack = new Stack<>();

        for (String token : tokens) {
            switch (token) {
                case "+":
                    stack.push(stack.pop() + stack.pop());
                    break;
                case "-":
                    int b = stack.pop(), a = stack.pop();
                    stack.push(a - b);
                    break;
                case "*":
                    stack.push(stack.pop() * stack.pop());
                    break;
                case "/":
                    int divisor = stack.pop(), dividend = stack.pop();
                    stack.push(dividend / divisor);
                    break;
                default:
                    stack.push(Integer.parseInt(token));
            }
        }

        return stack.pop();

	}

	public static void main(String[] args) {
		List<String> tokens = Arrays.stream(args[0].split(",")).map(s -> s).collect(Collectors.toList());
		System.out.println(evalRPN(tokens));
	}
}