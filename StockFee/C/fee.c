/*
 * Author: hms5232
 * Toolkit: Geany
 * URL: https://github.com/hms5232/CaiBiBa/tree/master/StockFee/C
 */

#include <stdio.h>

int main(){
	double price, fee;
	printf("請輸入股價：");
	scanf("%lf", &price);  // user input stock price
	fee = price * 1000 * 0.001425;
	printf("原始券商手續費：%f\n", fee);
	printf("電子下單手續費：%f\n", fee*0.6);
	printf("手續費CP最大化：%f張\n", 20/fee);
	printf("電子單CP最大化：%f張\n", 20/(fee*0.6));
	return 0;
}
