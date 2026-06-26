# Redis From Scratch

A small Redis clone built from scratch in Python.

This project is an educational implementation of a Redis-like in-memory data store. The goal is not to replace Redis or match every feature, but to build the core pieces by hand and understand how they fit together.

## What It Will Do

This server will eventually include:

- A TCP server that accepts client connections
- RESP protocol parsing for Redis-compatible messages
- Basic Redis commands such as `PING`, `SET`, and `GET`
- An in-memory key-value store
- Key expiry support for time-limited values

## Why Build This?

Redis is fast, simple, and deeply useful, which makes it a great system to study. Building a small clone from scratch is a practical way to learn:

- How TCP servers accept and handle client connections
- How application protocols are parsed and serialized
- How in-memory databases store and retrieve values
- How expiry and cleanup logic works inside a data store
- How systems programming ideas show up in everyday infrastructure

This project is mainly for learning systems programming and understanding how in-memory databases work under the hood.

## Project Structure

```text
redis-from-scratch/
├── main.py
├── requirements.txt
├── README.md
└── src/
    ├── __init__.py
    ├── parser.py
    ├── server.py
    └── store.py
```

## Status

Initial project structure only. Server logic will be added incrementally.
