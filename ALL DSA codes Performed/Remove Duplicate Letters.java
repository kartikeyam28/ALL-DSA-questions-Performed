package q3602;

public class CTJ3602 {

	public static String removeDuplicateLetters(String s) {
		int[] lastIndex = new int[26]; // Last index of each character
        boolean[] seen = new boolean[26]; // To check if character is in result
        char[] stack = new char[26]; // Stack to store result characters
        int top = -1; // Stack pointer

        // Store the last index of each character
        for (int i = 0; i < s.length(); i++) {
            lastIndex[s.charAt(i) - 'a'] = i;
        }

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            int idx = c - 'a';

            if (seen[idx]) continue;

            while (top >= 0 && c < stack[top] && lastIndex[stack[top] - 'a'] > i) {
                seen[stack[top] - 'a'] = false;
                top--;
            }

            stack[++top] = c;
            seen[idx] = true;
        }

        // Build result string
        StringBuilder result = new StringBuilder();
        for (int i = 0; i <= top; i++) {
            result.append(stack[i]);
        }

        return result.toString();

	}

	public static void main(String[] args) {
		String s = args[0];
		System.out.println(removeDuplicateLetters(s));
	}
}