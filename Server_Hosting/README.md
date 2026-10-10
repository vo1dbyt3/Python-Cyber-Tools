# Python Localhost Server

## Overview

A small Python project that explores how a local server can communicate with clients over a network connection. It provides hands-on practice with sockets, IP addresses, ports, and basic HTTP communication.

## Features

* Creates a local server using Python sockets.
* Binds the server to a host address and port.
* Listens for incoming client connections.
* Explores HTTP requests and server responses.
* Provides a practical introduction to client-server communication.

## Technologies

* Python 3
* `socket` module
* HTTP fundamentals

## Usage

Run the server:

```bash
python3 server_hosting.py
```

Connect to the address and port configured in the script using a browser or an HTTP client, such as `curl`.

For example, if the server listens on port `8080`:

```bash
curl -v http://127.0.0.1:8080/file_name.html
```

`127.0.0.1` is the loopback address, which refers to the same machine running the client.

## What I Learned

* Client-server architecture.
* IP addresses, ports, and sockets.
* Listening for and accepting connections.
* HTTP request and response basics.
* The difference between a local server and a publicly accessible server.

## Limitations

This project is intended for learning and experimentation. Its supported HTTP methods, request handling, and concurrency depend on the current implementation.

## Disclaimer

This server is intended for educational use. Keep it restricted to trusted environments unless you have intentionally configured and secured it for broader access.
