
import java.util.HashSet;
class Happynumber {
    public boolean isHappy(int n) {

        HashSet<Integer> s= new HashSet<>();
        while (n!=1) {
            if (s.contains(n)) {
                return false;
            }
            s.add(n);
            n=getSquares(n);

        }
        return true;
        
    }
    private static int getSquares(int n) { 
        int sum=0;
        while (n>0) {
            int digit=n%10;
            sum += digit*digit;
            n/=10;


        }

        return sum;
    }
}
    

