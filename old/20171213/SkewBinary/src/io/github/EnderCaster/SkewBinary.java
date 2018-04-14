/*
 * @author EnderCaster
 * @intorduction 在skewbinary 表示中，第K位的值x[k]表示x[k]*(2^(k+1)-1)。每个位上的可能数字可能是0或1，最后面一个非零位可以是2
 * @Input 输入包含一行或多行，美行包含一个整数n，若n=0则输入结束，否则其为skew数
 * @output skew数的十进制表示*/
package io.github.EnderCaster;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;

public class SkewBinary {
	private static int power(int base, int power) {
		int result=1;
		for(int i=0;i<power;i++){
			result*=base;
		}
		return result;
	}
	private static int skewConverter(int bit,int count){
		return bit*(power(2, count)-1);
	}

	public static void main(String[] args) {
		String skewbinaryStoregeFile="skewbinaryStoregeFile.txt";
		File inputFile=new File(skewbinaryStoregeFile);
		InputStreamReader isr;
		BufferedReader br = null;
		try {
			isr=new InputStreamReader(new FileInputStream(inputFile));
			br=new BufferedReader(isr);
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		String skewBinaryS="";
		try {
			while((skewBinaryS=br.readLine()) != null && !skewBinaryS.equals("0")){
				int result=0;
				for(int count=1;count<=skewBinaryS.length();count++){
					try {
						String skewBinaryC="";
						skewBinaryC+=skewBinaryS.charAt(count-1);
						result+=skewConverter(Integer.parseInt(skewBinaryC), count);
					} catch (NumberFormatException e) {
						System.out.println("not number");
						e.printStackTrace();
						break;
					}
				}
				System.out.println(result);
			}
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

}
