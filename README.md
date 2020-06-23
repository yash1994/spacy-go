# spaCy-Go

[![Build Status](https://travis-ci.org/yash1994/spacy-go.svg?branch=master)](https://travis-ci.org/yash1994/spacy-go)
![GitHub go.mod Go version](https://img.shields.io/github/go-mod/go-version/yash1994/spacy-go)
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)

spacy-go is Golang interface for accessing linguistic annotations provided by
[spaCy](https://spacy.io) using Google's [gRPC](https://grpc.io/). This module only supports basic functionalities like loading language models and providing linguistic annotation for text sentences.

## Installation

### Installing Golang library

spacy-go Golang library can be installed by following single command.

```bash
go get -v "github.com/yash1994/spacy-go"
```

### Setting up python gRPC server

Before importing the golang library, these commands need to be executed (inside source package) to spin up the python gRPC server.

`pip install -r requirements.txt`

`python3 -m grpc_tools.protoc --proto_path=protos --python_out=api --grpc_python_out=api protos/nlp.proto`

`python3 api/server.py &`

## Usage

### load language model

```Go
package main

import (
    "fmt"
    spacygo "github.com/yash1994/spacy-go"
)

func main() {

    res := spacygo.load("en_core_web_sm")
    fmt.Printf("%v", res)
}
```

## TODOS
* [ ] Extensive Test cases
* [ ] API Docs
* [ ] Similarity API