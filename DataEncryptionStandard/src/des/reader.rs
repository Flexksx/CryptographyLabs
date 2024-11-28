use std::io;

pub struct Reader;

impl Reader {
    pub fn read_input() -> String {
        let mut input = String::new();
        println!("Enter plaintext to encrypt:");
        io::stdin()
            .read_line(&mut input)
            .expect("Failed to read input");
        input.trim().to_string()
    }

    pub fn string_to_blocks(input: &str) -> Vec<[u8; 8]> {
        let bytes = input.as_bytes();
        let mut blocks = vec![];

        for chunk in bytes.chunks(8) {
            let mut block = [0u8; 8];
            for (i, &byte) in chunk.iter().enumerate() {
                block[i] = byte;
            }

            blocks.push(block);
        }
        if let Some(last) = blocks.last_mut() {
            if last.contains(&0) {
                return blocks;
            }
            let last_size = last.iter().position(|&x| x == 0).unwrap_or(8);
            if last_size < 8 {
                let padding_value = (8 - last_size) as u8;
                for i in last_size..8 {
                    last[i] = padding_value;
                }
            }
        }

        blocks
    }
}
