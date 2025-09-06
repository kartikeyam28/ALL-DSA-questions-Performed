package q3606;

public class CTJ3606 {

	public static int scoreOfParentheses(String s) {
		int score = 0;
        int depth = 0;

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                depth++;
            } else {
                depth--;
                if (s.charAt(i - 1) == '(') {
                    score += 1 << depth; // Same as score += Math.pow(2, depth)
                }
            }
        }
        return score;

	}

	public static void main(String[] args) {
		String s = args[0];
		System.out.println(scoreOfParentheses(s));
	}
}