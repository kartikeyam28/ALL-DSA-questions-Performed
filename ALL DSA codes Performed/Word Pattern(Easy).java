package q3784;

public class CTJ3784 {

	public static boolean WordPattern(String pattern, String s) {
		String[] words = split(s, " ");
        if (pattern.length() != words.length) {
            return false;
        }

        String[] map = new String[26];       // for pattern char -> word
        String[] reverseMap = new String[words.length]; // to check if word already used

        for (int i = 0; i < pattern.length(); i++) {
            int idx = pattern.charAt(i) - 'a';
            String word = words[i];

            if (map[idx] == null) {
                // Check if word already assigned to another pattern character
                for (int j = 0; j < 26; j++) {
                    if (word.equals(map[j])) {
                        return false;
                    }
                }
                map[idx] = word;
            } else if (!map[idx].equals(word)) {
                return false;
            }
        }

        return true;
    }

    // Minimal string split helper (no import)
    private static String[] split(String s, String delimiter) {
        int count = 1;
        for (int i = 0; i < s.length(); i++) {
            if (s.substring(i, i + 1).equals(delimiter)) {
                count++;
            }
        }

        String[] result = new String[count];
        int index = 0;
        int start = 0;
        for (int i = 0; i <= s.length(); i++) {
            if (i == s.length() || s.charAt(i) == ' ') {
                result[index++] = s.substring(start, i);
                start = i + 1;
            }
        }

        return result;

	}

	public static void main(String[] args) {
		String pattern = args[0];
		String s = args[1];
		System.out.println(WordPattern(pattern, s));
	}
}