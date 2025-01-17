
class Solution {
    public int maxWater(int arr[]) {
        
        int l=1;
        int r=arr.length-2;
        int res=0;
        int lmax=arr[l-1];
        int rmax= arr[r+1];
        
        while (l<=r) {
            if (rmax<=lmax) {
                
                res+=Math.max(0, rmax- arr[r]);
                rmax=Math.max(rmax, arr[r]);
                r--;
                
            }
            
            else {
                res+=Math.max(0, lmax- arr[l]);
                lmax=Math.max(lmax, arr[l]);
                l++;
            }
        // code here
    }
    
    return res;
    }
}