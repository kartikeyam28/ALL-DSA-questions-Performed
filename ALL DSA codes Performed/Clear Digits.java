package q3600;

public class CTJ3600 {

	public static String clearDigits(String s) {
		StringBuilder stack = new StringBuilder();
        for (char ch : s.toCharArray()) {
            if (Character.isDigit(ch)) {
                if (stack.length() > 0) {
                    stack.deleteCharAt(stack.length() - 1); // remove the closest non-digit to the left
                }
            } else {
                stack.append(ch); // push non-digit to stack
            }
        }
        return stack.toString();

	}

	public static void main(String[] args) {
		String s = args[0];
		System.out.println(clearDigits(s));
	}
}