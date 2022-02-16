public class CompareProduct {
    boolean compareProduct(int num) {
        if(num < 10) return false;
        int oddProdValue = 1;
        int evenProdValue = 1;

        while(num > 0) {
            int digit = num / 10;
            oddProdValue *= 10;
            num /= 10;
            if(num == 0) break;
            digit = num / 10;
            evenProdValue *= digit;
            num /= 10;
        }
        if(evenProdValue == oddProdValue) return true;
        return false;
    }
}
