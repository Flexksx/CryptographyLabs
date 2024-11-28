use std::io;

fn main() {
    // Prompt user for input
    println!("Enter plaintext (max 8 characters):");

    // Read user input
    let mut input = String::new();
    io::stdin()
        .read_line(&mut input)
        .expect("Failed to read input");

    // Trim newline and limit to 8 characters
    input = input.trim().to_string();
    if input.len() > 8 {
        println!("Input too long! Truncating to 8 characters.");
        input = input.chars().take(8).collect();
    }

    println!("Input (plaintext): {}", input);

    let input_block = string_to_block(&input);
    println!("64-bit block: {:?}", input_block);
}
fn string_to_block(input: &str) -> [u8; 8] {
    let mut block = [0u8; 8];
    let bytes = input.as_bytes();

    for i in 0..bytes.len() {
        block[i] = bytes[i];
    }

    block
}
