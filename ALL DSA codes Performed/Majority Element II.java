package q3659;
import java.util.*;
import java.util.stream.*;

public class CTJ3659 {

	public static List<Integer> majorityElement(List<Integer> numsArr) {
		// Boyer-Moore voting Algorithm
		List<Integer> ans = new ArrayList<>();
		if(numsArr==null || numsArr.isEmpty()) return ans;
		int count1 = 0, count2 = 0;
		int candidate1 = 0, candidate2 = 0;

		// first pass to find upto two elements
		for(int num : numsArr) {
			if( num==candidate1) {
				count1++;
			} else if( num==candidate2) {
				count2++;
			} else if(count1 == 0) {
				candidate1 = num;
				count1 = 1;
			} else if(count2 == 0) {
				candidate2 = num;
				count2 = 1;
			} else {
				count1--;
				count2--;
			}
		}

		// second pass to confirm the elements
		count1 = 0;
		count2 = 0;
		for(int num : numsArr) {
			if(num == candidate1) count1++;
			if(num == candidate2) count2++;
		}

		int n = numsArr.size();

		if(candidate1==3 && candidate2==2) {
			if(count2 > n/3) ans.add(candidate2);
			ans.add(candidate1);
			return ans;
		}
		if(count1 > n/3) ans.add(candidate1);
		if(candidate2!=candidate1 && count2 > n/3) ans.add(candidate2);
		return ans;

	}

	public static void main(String[] args) {
		List<Integer> numsArr = Arrays.stream(args[0].split(",")).map(s -> Integer.parseInt(s)).collect(Collectors.toList());
		System.out.println(majorityElement(numsArr).stream().map(String::valueOf).collect(Collectors.joining(",")));
	}
}