// { Driver Code Starts
import java.util.*;

class MaxLenZeroSumSub
{

    // Returns length of the maximum length subarray with 0 sum

    // Drive method
    public static void main(String arg[])
    {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        while (T > 0)
        {
            int n = sc.nextInt();
            int arr[] = new int[n];
            for (int i = 0; i < n; i++)
                arr[i] = sc.nextInt();

            GfG g = new GfG();
            System.out.println(g.maxLen(arr, n));
            T--;
        }
    }
}// } Driver Code Ends


class GfG {
	int maxLen(int arr[], int n) {
		int preSum = 0;

		int max = 0;

		HashMap<Integer, Integer> myMap = new HashMap<>();

		for (int i = 0; i < n; i++) {

			preSum = preSum + arr[i];

			if (preSum == 0) {
				max = i + 1;
			} else {

				if (myMap.containsKey(preSum)) {
					int start = myMap.get(preSum);
					max = Math.max(i - start, max);
				} else {
					myMap.put(preSum, i);
				}

			}

		}

		return max;

	}
}