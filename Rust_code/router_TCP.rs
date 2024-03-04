use std::io::{self, Read, Write};
use std::net::TcpStream;

fn main() -> io::Result<()> {
    // Replace these values with the IP address and port of your router
    let router_address = "192.168.0.1";
    let router_port = 80;

    // Connect to the router
    let mut stream = TcpStream::connect((router_address, router_port))?;

    println!("Connected to router");

    // Example: Send a command to the router
    let command = "GET /wlbasic.htm HTTP/1.1\r\nHost: 192.168.0.1\r\n\r\n";
    stream.write_all(command.as_bytes())?;

    // Read the response from the router
    let mut buffer = [0; 1024];
    let bytes_read = stream.read(&mut buffer)?;

    // Convert the response to a string and print it
    let response = String::from_utf8_lossy(&buffer[..bytes_read]);
    println!("Response from router:\n{}", response);

    Ok(())
}
