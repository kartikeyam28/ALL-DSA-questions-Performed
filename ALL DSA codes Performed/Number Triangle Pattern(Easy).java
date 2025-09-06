package q3627;
import java.util.*;
public class CTJ3627{
	public static void main(String [] args){
		int n;
		Scanner sc=new Scanner(System.in);
		n = sc.nextInt();
		int num =1;
		int i,j;
		for (i=1;i<=n;i++){
			for (j=1;j<=i;j++){
				if(j<i){
					System.out.print(num+" ");
				}
				else{
					System.out.print(num);
				}
				num++;
			}
			System.out.println();
			
		}
	}
}