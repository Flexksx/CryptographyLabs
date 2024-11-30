import java.util.List;

import bytes.SubstitutionBlock;
import substituion.substitutionbox.SubstitutionBox;
import substituion.substitutionbox.SubstitutionBoxTable;

public class DataEncryptionStandard {
  public static void main(String[] args) {
    List<SubstitutionBlock> blocks = List.of(
        new SubstitutionBlock(0b110011),
        new SubstitutionBlock(0b101010),
        new SubstitutionBlock(0b111100),
        new SubstitutionBlock(0b000000));

    for (SubstitutionBlock block : blocks) {
      System.out.println("Block: " + block.getValue() + ". Bit representation: " + block.toString());
      for (int i = 0; i < 8; i++) {
        SubstitutionBox box = SubstitutionBoxTable.getAt(i);
        int value = box.substitute(block);
        System.out.println("Box " + i + ": " + value);
      }
    }
  }
}
