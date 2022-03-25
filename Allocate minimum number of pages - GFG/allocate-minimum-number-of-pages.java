// { Driver Code Starts
//Initial Template for Java

/*package whatever //do not write package name here */

import java.io.*;
import java.util.*;
class GFG {
	public static void main (String[] args) {
		Scanner sc=new Scanner(System.in);
		
		int t=sc.nextInt();
		
		while(t-->0)
		{
		    int n=sc.nextInt();
		    int a[]=new int[n];
		    
		    for(int i=0;i<n;i++)
		    {
		        a[i]=sc.nextInt();
		    }
		    int m=sc.nextInt();
		    Solution ob = new Solution();
		    System.out.println(ob.findPages(a,n,m));
		}
	}
}// } Driver Code Ends


//User function Template for Java

class Solution 
{
    //Function to find minimum number of pages.
    public static int findPages(int[]weights,int N,int days)
    {
        if (days > weights.length)
			return -1;

		int low = weights[0];
		int high = 0;

		for (int i : weights) {
			high += i;
			low = Math.min(i, low);
		}

		int result = -1;

		while (low <= high) {

			int mid = (low + high) >> 1;

			if (isPossible(weights, mid, days)) {
				result = mid;
				high = mid - 1;
			} else {
				low = mid + 1;
			}

		}

		return low;
    }
    
    private static boolean isPossible(int[] weights, int weight, int days) {

		int count = 0;

		int sumAllocated = 0;

		for (int i = 0; i < weights.length; i++) {

			if (sumAllocated + weights[i] > weight) {

				count++;
				sumAllocated = weights[i];
				if (sumAllocated > weight) return false;

			} else {
				sumAllocated += weights[i];
			}

		}

		if (count < days)
			return true;

		return false;
	}

};