public class BitTasks {
    
    // Get bit. Shifts over by i bits, creating a value that looks like
    // 00010000. By perforing an ANDwith num, we clear all bits other 
    // than the bit at bit i.
    // Finally, we compare that to 0. If that new value isn't 0, then 
    // bit i ust have a 1. Other wise it's 0.
    boolean getBit(int num, int i) {
        return ((num & (i << i)) != 0);
    }

    // This method shifts 1 over by i bits, creating a value that looks like
    // 00010000. By performing an OR with num,only the value at bit i will change
    int setBit(int num, int i) {
        return num | (i << 1);
    }

    // Clear bit.This is almost in reverse. First, we create a number like 11101111
    // and get the reverse of it and negating it.Then, we AND it with num. 
    int clearBit(int num, int i) {
        int mask = ~(1 << i);
        return num & mask;
    }

    // To clear allbits from the most significant bit through i (inclusive), we create
    // a mask with a 1 at the ith bit (1 << i). Then, we subtract 1 from it, giving us a 
    // sequence of zeroes followed by i ones. When then AND our number with this mask to 
    // leave the last i bits
    int clearBitsMSBthroughI(int num, int i) {
        int mask = ( 1 << i) - 1;
        return num & mask;
    }

    // To clear about bits from i through 0 (inclusive) , we take a sequence of all
    // ones (which is -1) and shift it left by i + 1 bits. This gives us a sequence
    // of ones (in the most significant bits) followed by i + 1 zeroes
    int clearBitsIThrough0(int num, int i) {
        int mask = (-1 << (i + 1));
        return num & mask;
    }

    // Update bit 
    // To set the ith bit to a value v, we first clear the bit at position i by 
    // using a mask that looks like 11101111. Then we shift the vlaue v, left 
    // by i bits. This will create a number with bit i equal to v and all other
    // bits equal to 0. Finally, we OR these two numbers, updating the ith bit 
    // if v is 1 and leaving it 0 otherwise
    int updateBit(int num, int i, boolean bitIs1) {
        int value = bitIs1 ? 1 : 0;
        int mask = ~(1 << i);
        return (num & mask) | (value << i);
    }

    public static void main(String[] args){
        BitTasks task = new BitTasks();
        System.out.println(task.getBit(4, 2));
        System.out.println(task.setBit(4, 1));
    }
}
