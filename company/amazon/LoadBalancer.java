/*
Given an array containing only positive integers, return if you can pick 
two integers from the array which cuts the array into three pieces such 
that the sum of elements in all pieces is equal.

Example 1:

Input: array = [2, 4, 5, 3, 3, 9, 2, 2, 2]

Output: true

Explanation: choosing the number 5 and 9 results in three pieces [2, 4],
[3, 3] and [2, 2, 2]. Sum = 6.

Example 2:

Input: array =[1, 1, 1, 1],

Output: false
*/
import java.util.*;

 public class LoadBalancer {
	public boolean loadBalance(int[] arr) {
		int sum = 0;
		int len = arr.length;
		if(len < 5){
		    return false;
		}
		for(int i =0;i<len;i++) {
		    sum += arr[i];
		}
		int prefixSum = arr[0], suffixSum = arr[len-1];
		int left = 1, right = len - 2;
		boolean flag = false;
		while(left < right - 1) {
		    int midSum = sum - prefixSum - suffixSum - arr[left] - arr[right];
		    if(prefixSum == midSum && suffixSum == midSum) {
		        flag = true;
		        break;
		    } else {
		        if(prefixSum < suffixSum) {
		            prefixSum += arr[left];
		            left++;
		        } else if(prefixSum > suffixSum) {
		            suffixSum += arr[right];
		            right--;
		        } else {
		            prefixSum += arr[left];
		            suffixSum += arr[right];
		            left++;
		            right--;
		        }
		    }
		}
		return flag;
	}
}