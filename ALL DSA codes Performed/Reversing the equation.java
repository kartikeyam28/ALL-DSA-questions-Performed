package q3583;

public class CTJ3583 {

	public static String reverseEqn(String s) {
		StringBuilder result = new StringBuilder();
        StringBuilder number = new StringBuilder();

        for (int i = s.length() - 1; i >= 0; i--) {
            char ch = s.charAt(i);

            if (Character.isDigit(ch)) {
                number.insert(0, ch);
            } else {
                result.append(number).append(ch);
                number.setLength(0);
            }
        }

        result.append(number); // append the last number
        return result.toString();

	}

	public static void main(String[] args) {
		String s = args[0];
		System.out.println(reverseEqn(s));
	}
}