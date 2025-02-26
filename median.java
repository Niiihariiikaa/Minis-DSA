
class median {
    public ArrayList<Double> getMedian(int[] arr) {
        
        PriorityQueue<Integer> leftmax= new PriorityQueue<>(
            (a,b)-> b-a);
        PriorityQueue<Integer> rightmin= new PriorityQueue<>();
        ArrayList<Double> res= new ArrayList<>();
        
        for (int i=0; i<arr.length; i++){
            leftmax.add(arr[i]);
            
            int temp=leftmax.poll();
            rightmin.add(temp);
            
            if(rightmin.size()> leftmax.size()){
               temp= rightmin.poll();
                leftmax.add(temp);
                
            }
            
            double median;
            if(leftmax.size()!=rightmin.size()){
                median= leftmax.peek();
            }else {
                median= (leftmax.peek()+ rightmin.peek())/2.0;
            }
            res.add(median);
            
        }
        
        return res;
        
        
            
            
        // code here
    }
}