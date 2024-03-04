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

fn chat_with_server() {
    let mut stream = TcpStream::connect("192.168.0.1:80/home.htm").unwrap();
    stream.write_all(b"Hello, server!").unwrap();
    for _ in 0..3 {
        let mut buffer = [0; 1024];
        stream.read(&mut buffer).unwrap();
        let message = String::from_utf8_lossy(&buffer);
        println!("Received message from server: {}", message);
    }
}

fn listener() {
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

fn main() {
    // thread::spawn(listener);
    chat_with_server();
}
