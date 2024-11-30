package substituion.substitutionbox;

import bytes.SubstitutionBlock;

public class SubstitutionBox {
    private final int[][] table;

    public SubstitutionBox(int[][] table) {
        this.table = table;
    }

    public int getAt(int row, int col) {
        return table[row][col];
    }

    public int[][] getTable() {
        return table;
    }

    public int substitute(SubstitutionBlock block) {
        int firstBit = block.getFirstBit();
        int lastBit = block.getLastBit();
        System.out.println("Selecting row of configuration " + firstBit + "xxxx" + lastBit);
        int row = (block.getFirstBit() << 1) + block.getLastBit();
        int col = block.getValue() & 0b011110;
        col >>= 1;
        System.out.println("Row: " + row + " Col: " + col);
        return table[row][col];
    }

    public int substitute(int value) {
        return substitute(new SubstitutionBlock(value));
    }
}
