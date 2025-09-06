package q3193;
import java.util.*;
import java.util.stream.*;

public class CTJ3193 {

	public static int maxArea(List<Integer> height) {
		int maxWater = 0;
        int left = 0;
        int right = height.size() - 1;
        
        while (left < right) {
            int currentHeight = Math.min(height.get(left), height.get(right));
            int currentWidth = right - left;
            int currentArea = currentHeight * currentWidth;
            maxWater = Math.max(maxWater, currentArea);
            
            if (height.get(left) < height.get(right)) {
                left++;
            } else {
                right--;
            }
        }
        
        return maxWater;
		

	}

	public static void main(String[] args) {
		List<Integer> height = Arrays.stream(args[0].split(",")).map(s -> Integer.parseInt(s)).collect(Collectors.toList());
		System.out.println(maxArea(height));
	}
}