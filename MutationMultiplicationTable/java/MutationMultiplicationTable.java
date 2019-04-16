/**
 * 變種九九乘法表
 *
 * 輸出為1,m,2,m-1......
 *
 * 例如19*9輸出中的7
 *      7*1=1
 *      7*9=63
 *      7*2=14
 *
 *      ...
 *      依此類推
 */

import java.util.Scanner;

public class MutationMultiplicationTable{

	// 反向乘數來囉
	public static int reverseWay(int multiplicand, int round){
		int reverse = 9 - round + 1;
		System.out.println(multiplicand+" * "+reverse+" = "+multiplicand*reverse);
		return 0;
	}

	public static void main(String[] args){
		Scanner input = new Scanner(System.in);
		System.out.print("請輸入數字：");
		int go = input.nextInt();  //輸入要做多少*9的表
		for(int i=1; i<=go; i++){
			for(int j=1; j<=5; j++){
				System.out.println(i+" * "+j+" = "+i*j);
				if(j != 5){
					reverseWay(i, j);
				}
			}
			System.out.println();  // 被乘數+1前先換行比較好看
		}
	}
}