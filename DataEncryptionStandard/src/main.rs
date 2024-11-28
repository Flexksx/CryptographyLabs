mod des;

use des::key;
use des::permutation;
use des::reader;
fn main() {
    // Step 1: Use Reader to read input from the user
    let plaintext = reader::Reader::read_input();

    println!("Transforming your text: '{plaintext}' input into 64-bit blocks");
    let blocks = reader::Reader::string_to_blocks(&plaintext);
    println!("64-bit blocks: {:?}", blocks);

    // Step 3: Generate a key for encryption (dummy for now)
    let key = key::generate_key();
    println!("Generated key: {:?}", key);
    let initial_permutation = permutation::Permutation::get_initial();
    println!("Initial permutation: {:?}", initial_permutation);
}
