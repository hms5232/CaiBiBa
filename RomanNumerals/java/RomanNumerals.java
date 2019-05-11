/** ANSI */
/**
 * I（1）
 * V（5）
 * X（10）
 * L（50）
 * C（100）
 * D（500）
 * M（1000）
 */

import java.util.Scanner;

public class RomanNumerals{
	public static void main(String[] args){
		Scanner input = new Scanner(System.in);
		System.out.print("Please input the Roman numberals: ");
		String ronum = input.next();
		
		// 強型態/型別麻煩在這邊哀
		char[] inputNum = ronum.toUpperCase().toCharArray();  // 將使用者輸入的東西先通通轉成大寫並逐一丟進陣列中存成char
		int[] numerals = new int[inputNum.length];  // 存放轉換後變成的數字
		
		for(int i=0; i<=inputNum.length-1; i++){
			int checkRomanNum = transformRomanNum(inputNum[i]);
			if(checkRomanNum == -1){
				System.out.println("\""+inputNum[i]+"\"不是正確的羅馬數字，請重新輸入正確的羅馬數字");
				return ;
			}else{
				// 我準備好了，放進來吧
				numerals[i] = checkRomanNum;
			}
		}
		
		// 檢查有無四個連續一樣的數碼
		if(checkRestriction(numerals)){
			System.out.println("不能連續四個一樣的數碼");  // 願大家都可以像小孩一樣 => 「我全都要」是不行的喔
			return;
		}
		
		// 『μ's music start~』
		int result = 0;  // ※羅馬數字中是沒有0的喔
		for(int l=0; l<=numerals.length-1; l++){
			if(l == 0){
				result += numerals[l];
				continue;
			}
			if(numerals[l] > numerals[l-1]){  // 左邊的數字比較小就減掉
				// 左減的數字有限制，僅限於I、X、C
				if(numerals[l-1]==1 || numerals[l-1]==10 || numerals[l-1]==100){
					numerals[l-1] *= -2;  // 加倍奉還（把原本加上去的扣回來）
					result += (numerals[l] + numerals[l-1]);
				}else{
					System.out.println("左減的數字有限制，僅限於I、X、C");
					return;
				}
			}else{  // 右邊的數字比較小就相加
				result += numerals[l];
			}
		}
		
		System.out.println(result);
	}
	
	
	// 檢查使用者輸入的羅馬數字和轉換成阿拉伯數字
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
				// 『好像有奇怪的東西混進來了』
				return -1;
		}
	}
	
	
	// 不能連續四個一樣的數碼
	public static boolean checkRestriction(int[] numerals){
		for(int j=2; j<=numerals.length-2; j++){
			/*
				XXXX
				  ↑
				檢查前面兩個和後面一個數碼是否和現在指向的數碼相同
			 */
			if(numerals[j-2]==numerals[j] && numerals[j-1]==numerals[j] && numerals[j+1]==numerals[j]){
				if(numerals[j] == 1){  // 唯一的例外IIII
					// 『人家才...才有沒給你特殊待遇呢！哼！』(別過頭
					continue;
				}
				return true;
			}
		}
		return false;
	}
}