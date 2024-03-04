// main.rs
use std::net::{TcpListener, TcpStream};
use std::io::{Read, Write};
use std::thread;

fn handle_client(mut stream: TcpStream) {
    let mut buffer = [0; 1024];
    loop {
        match stream.read(&mut buffer) {
            Ok(bytes_read) => {
                if bytes_read == 0 {
                    break;
                }
                let message = String::from_utf8_lossy(&buffer[..bytes_read]);
                println!("Received message: {}", message);
                // Process message (encryption, authentication, etc.)
                // Echo the message back to the client
                stream.write_all(&buffer[..bytes_read]).unwrap();
            }
            Err(_) => {
                println!("An error occurred while reading from the stream");
                break;
            }
        }
    }
}

fn main() {
    let listener = TcpListener::bind("127.0.0.1:8080").unwrap();
    println!("Server listening on port 8080...");

    for stream in listener.incoming() {
        match stream {
            Ok(stream) => {
                thread::spawn(|| {
                    handle_client(stream);
                });
            }
            Err(_) => {
                println!("Failed to establish connection with client");
            }
        }
    }
}
