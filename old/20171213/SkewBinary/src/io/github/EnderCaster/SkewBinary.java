/*
 * @author EnderCaster
 * @intorduction ��skewbinary ��ʾ�У���Kλ��ֵx[k]��ʾx[k]*(2^(k+1)-1)��ÿ��λ�ϵĿ������ֿ�����0��1�������һ������λ������2
 * @Input �������һ�л���У����а���һ������n����n=0�����������������Ϊskew��
 * @output skew����ʮ���Ʊ�ʾ*/
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
