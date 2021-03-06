function switchNum(){
	let getInput = document.getElementById("inputNum").value.toUpperCase();  // 取值時順便通通轉換成大寫；小寫是Lower
	let numerals = [];
	var result = 0;  // answer
	// 開始逐一處理使用者輸入的數碼
	for(let i=0; i<=getInput.length-1; i++){
		let tmp = checkInput(getInput.substr(i, 1));  // 先看使用者有沒有輸入非羅馬數字的東西
		if(tmp == -1){  // 『ブッブーですわ!』
			alert("「"+getInput.substr(i, 1)+"」不是正確的羅馬數字");
			return;
		}
		numerals[i] = tmp;  // 要放進去囉>///<
	}
	// 再來確定有沒有連續四個數碼都長一樣
	if(checkRestriction(numerals)){
		alert("不可連續四個數碼");
		return;  // あのねあのね~通行止め！╮>,<
	}
	// 開始計算
	for(let j=0; j<=getInput.length-1; j++){
		if(j == 0){ // 「排頭伍為準──~~~」
			result += numerals[j];
			continue;
		}
		if(numerals[j] > numerals[j-1]){  // 左邊的數字比較小要相減
			// 左減的數字有限制，僅限於I、X、C
			if(numerals[j-1]==1 || numerals[j-1]==10 || numerals[j-1]==100){
				numerals[j-1] *= -2;  // 把原本加上去的也扣掉（加倍奉還）
				result += (numerals[j] + numerals[j-1]);
			}else{
				alert("左減的數字有限制，僅限於I、X、C");
				return;
			}
		} else {
			result += numerals[j];
		}
	}
	alert(result);  // 跳出結果
}

// 檢查輸入的羅馬數字順便轉換成對應的阿拉伯數字
function checkInput(word){
	switch(word){
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
			return 500
		case 'M':
			return 1000;
		default:
			// 『好像有奇怪的東西混進來了』
			return -1;
	}
}

// 不能連續四個數碼在一起
function checkRestriction(numerals){
	for(let j=2; j<=numerals.length; j++){
		/*
			XXXX
			  ↑
			檢查前面兩個和後面一個數碼是否和現在指向的數碼相同
		*/
		if(numerals[j] == numerals[j-2] && numerals[j] == numerals[j-1] && numerals[j] == numerals[j+1]){
			if(numerals[j] == 1){  // 唯一的例外IIII
				continue;
			}
			return 1;
		}
	}
	return 0;
}