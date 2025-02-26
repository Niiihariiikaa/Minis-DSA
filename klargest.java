package heap;

import java.util.ArrayList;
import java.util.Collections;
import java.util.PriorityQueue;

public class klargest {
     public ArrayList<Integer> kLargest(int[] arr, int k) {
        
        PriorityQueue<Integer> minheap= new PriorityQueue<>(k);
        ArrayList<Integer> res= new ArrayList<>();
        
        for (int i=0; i<k; i++){
            minheap.add(arr[i]);
            
        }
        for (int i=k; i<arr.length; i++){
            if(arr[i]> minheap.peek()){
                minheap.poll();
                minheap.add(arr[i]);
                
            }
            
        }
        
        while(!minheap.isEmpty()){
            res.add(minheap.poll());
        }
        Collections.reverse(res);
        return res;
        // Your code here
    }
}
    

