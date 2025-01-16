import java.util.PriorityQueue;
class Solution {
    public int[][] kClosest(int[][] points, int k) {
         PriorityQueue<int[]> p= new PriorityQueue<>( 
         (a,b) -> Integer.compare(distance(b),distance(a))
         );

         for (int[] point: points) {
            p.add(point);
            if(p.size()>k) {
                p.poll();
            }
         }

           int[][] result = new int[k][2];
        for (int i = 0; i < k; i++) {
            result[i] = p.poll();
        }

        return result;
    }

         private int distance (int[] point) {
            return point[0] *point[0] +point[1]*point[1];
         }
    }