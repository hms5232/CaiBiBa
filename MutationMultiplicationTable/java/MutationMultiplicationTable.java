/**
 * �ܺؤE�E���k��
 *
 * ��X��1,m,2,m-1......
 *
 * �Ҧp19*9��X����7
 *      7*1=1
 *      7*9=63
 *      7*2=14
 *
 *      ...
 *      �̦�����
 */

import java.util.Scanner;

public class MutationMultiplicationTable{

	// �ϦV���ƨ��o
	public static int reverseWay(int multiplicand, int round){
		int reverse = 9 - round + 1;
		System.out.println(multiplicand+" * "+reverse+" = "+multiplicand*reverse);
		return 0;
	}

	public static void main(String[] args){
		Scanner input = new Scanner(System.in);
		System.out.print("�п�J�Ʀr�G");
		int go = input.nextInt();  //��J�n���h��*9����
		for(int i=1; i<=go; i++){
			for(int j=1; j<=5; j++){
				System.out.println(i+" * "+j+" = "+i*j);
				if(j != 5){
					reverseWay(i, j);
				}
			}
			System.out.println();  // �Q����+1�e���������n��
		}
	}
}