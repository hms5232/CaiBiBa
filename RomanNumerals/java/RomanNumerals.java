/** ANSI */
/**
 * I�]1�^
 * V�]5�^
 * X�]10�^
 * L�]50�^
 * C�]100�^
 * D�]500�^
 * M�]1000�^
 */

import java.util.Scanner;

public class RomanNumerals{
	public static void main(String[] args){
		Scanner input = new Scanner(System.in);
		System.out.print("Please input the Roman numberals: ");
		String ronum = input.next();
		
		// �j���A/���O�·Цb�o��s
		char[] inputNum = ronum.toUpperCase().toCharArray();  // �N�ϥΪ̿�J���F����q�q�ন�j�g�óv�@��i�}�C���s��char
		int[] numerals = new int[inputNum.length];  // �s���ഫ���ܦ����Ʀr
		
		for(int i=0; i<=inputNum.length-1; i++){
			int checkRomanNum = transformRomanNum(inputNum[i]);
			if(checkRomanNum == -1){
				System.out.println("\""+inputNum[i]+"\"���O���T��ù���Ʀr�A�Э��s��J���T��ù���Ʀr");
				return ;
			}else{
				// �ڷǳƦn�F�A��i�ӧa
				numerals[i] = checkRomanNum;
			}
		}
		
		// �ˬd���L�|�ӳs��@�˪��ƽX
		if(checkRestriction(numerals)){
			System.out.println("����s��|�Ӥ@�˪��ƽX");  // �@�j�a���i�H���p�Ĥ@�� => �u�ڥ����n�v�O���檺��
			return;
		}
		
		// �y�g's music start~�z
		int result = 0;  // ��ù���Ʀr���O�S��0����
		for(int l=0; l<=numerals.length-1; l++){
			if(l == 0){
				result += numerals[l];
				continue;
			}
			if(numerals[l] > numerals[l-1]){  // ���䪺�Ʀr����p�N�
				// ����Ʀr������A�ȭ���I�BX�BC
				if(numerals[l-1]==1 || numerals[l-1]==10 || numerals[l-1]==100){
					numerals[l-1] *= -2;  // �[���^�١]��쥻�[�W�h�����^�ӡ^
					result += (numerals[l] + numerals[l-1]);
				}else{
					System.out.println("����Ʀr������A�ȭ���I�BX�BC");
					return;
				}
			}else{  // �k�䪺�Ʀr����p�N�ۥ[
				result += numerals[l];
			}
		}
		
		System.out.println(result);
	}
	
	
	// �ˬd�ϥΪ̿�J��ù���Ʀr�M�ഫ�����ԧB�Ʀr
	public static int transformRomanNum(char ronum){
		switch(ronum){
			case 'I':
				return 1;
			case 'V':
				return 5;
			case 'X':
				return 10;
			case 'L':
				return 50;
			case 'C':
				return 100;
			case 'D':
				return 500;
			case 'M':
				return 1000;
			default:
				// �y�n�����_�Ǫ��F��V�i�ӤF�z
				return -1;
		}
	}
	
	
	// ����s��|�Ӥ@�˪��ƽX
	public static boolean checkRestriction(int[] numerals){
		for(int j=2; j<=numerals.length-2; j++){
			/*
				XXXX
				  ��
				�ˬd�e����өM�᭱�@�ӼƽX�O�_�M�{�b���V���ƽX�ۦP
			 */
			if(numerals[j-2]==numerals[j] && numerals[j-1]==numerals[j] && numerals[j+1]==numerals[j]){
				if(numerals[j] == 1){  // �ߤ@���ҥ~IIII
					// �y�H�a�~...�~���S���A�S��ݹJ�O�I��I�z(�O�L�Y
					continue;
				}
				return true;
			}
		}
		return false;
	}
}