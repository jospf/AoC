use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() -> io::Result<()> {
    // File path
    let file_path = "day1input.txt";

    // Vectors to store columns
    let mut col1: Vec<f64> = Vec::new();
    let mut col2: Vec<f64> = Vec::new();

    // Read the file line by line
    if let Ok(lines) = read_lines(file_path) {
        for line in lines {
            if let Ok(content) = line {
                // Split line into columns
                let values: Vec<&str> = content.split_whitespace().collect();
                if values.len() == 2 {
                    // Parse values into floats and push to vectors
                    if let (Ok(val1), Ok(val2)) = (values[0].parse::<f64>(), values[1].parse::<f64>()) {
                        col1.push(val1);
                        col2.push(val2);
                    }
                }
            }
        }
    }

    // Sort the vectors
    col1.sort_by(|a, b| a.partial_cmp(b).unwrap());
    col2.sort_by(|a, b| a.partial_cmp(b).unwrap());

    // Calculate the cumulative sum
    let mut cumulative_sum = 0.0;
    for &element in &col1 {
        let count = col2.iter().filter(|&&x| x == element).count();
        cumulative_sum += element * count as f64;
    }

    // Output the result
    println!(
        "Cumulative Sum of Elements in Column 1 Multiplied by Their Counts in Column 2: {}",
        cumulative_sum
    );

    Ok(())
}

// Helper function to read lines from a file
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where
    P: AsRef<Path>,
{
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
