package heap;

import java.util.PriorityQueue;

public class korigin {

    
    public int sqdis(int[] point){
        return point[0]*point[0] + point[1]*point[1];
    }
    public int[][] kClosest(int[][] points, int k) {
        PriorityQueue<int[]> maxheap= new PriorityQueue<>(
            (a,b)-> sqdis(b)-sqdis(a));
            
            for(int[] point: points ){
                if(maxheap.size()<k){
                    maxheap.offer(point);
                }
                else{
                    if(sqdis(point)<sqdis(maxheap.peek())){
                        maxheap.poll();
                        maxheap.offer(point);
                    }
                }
            }
            
            int[][] res= new int[k][2];
            int index=0;
            while(!maxheap.isEmpty()){
                int[] point= maxheap.poll();
                res[index][0]= point[0];
                res[index][1]= point[1];
                index++;
            }
            
            return res;
            
            
        
        
        // Your code here
    }
}
    
}
