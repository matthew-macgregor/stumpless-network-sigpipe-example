# Overview

This is a minimal example to reproduce the behavior of the 
[Stumpless](https://github.com/goatshriek/stumpless) logging framework network
target. This example relates to discussion about the behavior of the new
`STUMPLESS_OPTION_CONS` option.

- Target platform: Linux/Unix (Tested on Ubuntu 22.04)
- Stumpless version: v2.0.0

## Description

When logging to a network target on \*nix, if the server disconnects a 
`SIGPIPE` signal will be raised. The default behavior of this signal is to 
terminate the process. The current recommendation is to ignore the signal.

```c
if ( signal( SIGPIPE, SIG_IGN ) == SIG_ERR ) {
  fprintf( stderr, "Cannot handle SIGPIPE\n" );
  exit( EXIT_FAILURE );
}
```

If the signal is neither handled or ignored, the process will be terminated.

## Discussion

- https://github.com/goatshriek/stumpless/issues/78#issuecomment-1229197064
- Issue TBD

## TCP Server

This project provides `server.py`, which is a simple TCP server which will
kill the connection after 5 log messages are transmitted.

## Setup Instructions

The following dependencies are required:

- stumpless v2.0.0
- build dependencies for stumpless
- Python 3+

To build:

```sh
mkdir build
cd build
cmake -S . -B build
cmake --build build
```

To run both client and server:

```sh
./run.sh
```
