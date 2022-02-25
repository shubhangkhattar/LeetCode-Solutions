// { Driver Code Starts
import java.io.*;
import java.lang.*;
import java.util.*;

class Item {
    int value, weight;
    Item(int x, int y){
        this.value = x;
        this.weight = y;
    }
}

class GfG {
    
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine().trim());
		while(t-->0){
            String inputLine[] = br.readLine().trim().split(" ");
            int n = Integer.parseInt(inputLine[0]);
            int w = Integer.parseInt(inputLine[1]);
            Item[] arr = new Item[n];
            inputLine = br.readLine().trim().split(" ");
            for(int i=0, k=0; i<n; i++){
                arr[i] = new Item(Integer.parseInt(inputLine[k++]), Integer.parseInt(inputLine[k++]));
            }
            System.out.println(String.format("%.2f", new Solution().fractionalKnapsack(w, arr, n)));
        }
    }
}// } Driver Code Ends


/*
class Item {
    int value, weight;
    Item(int x, int y){
        this.value = x;
        this.weight = y;
    }
}
*/

class itemComparator implements Comparator<Item> {

	@Override
	public int compare(Item o1, Item o2) {

		double r1 = (double) o1.value / (double) o1.weight;
		double r2 = (double) o2.value / (double) o2.weight;

		if (r2 > r1) {
			return 1;
		} else if (r2 < r1) {
			return -1;
		}

		return 0;
	}

}

class Solution {

	double fractionalKnapsack(int W, Item arr[], int n) {

		itemComparator myComparator = new itemComparator();

		Arrays.sort(arr, myComparator);

		int curWeight = 0;
		double finalValue = 0.0;

		for (int i = 0; i < arr.length; i++) {

			if (arr[i].weight + curWeight <= W) {

                curWeight += arr[i].weight;
                finalValue += arr[i].value;

			} else {

				int remain = W - curWeight;

				finalValue += (double) remain * ((double) arr[i].value / (double) arr[i].weight);
				break;
			}

		}

		return finalValue;

	}
}