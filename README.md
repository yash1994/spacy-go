# spaCy-Go

[![Build Status](https://travis-ci.org/yash1994/spacy-go.svg?branch=master)](https://travis-ci.org/yash1994/spacy-go)
![GitHub go.mod Go version](https://img.shields.io/github/go-mod/go-version/yash1994/spacy-go)
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![codecov](https://codecov.io/gh/yash1994/spacy-go/branch/master/graph/badge.svg)](https://codecov.io/gh/yash1994/spacy-go)

spacy-go is Golang interface for accessing linguistic annotations provided by
[spaCy](https://spacy.io) using Google's [gRPC](https://grpc.io/). This module only supports basic functionalities like loading language models, linguistic annotation and similarity for text sentences.

## Installation

### Installing Golang library

spacy-go Golang library can be installed by following single command.

```bash
go get -v "github.com/yash1994/spacy-go"
```

### Setting up python gRPC server

The `$GOPATH` environment variable lists places for Go to look for Go Workspaces. By default, Go assumes our GOPATH location is at `$HOME/go`, where `$HOME` is the root directory of our user account on our computer.

Before importing the golang library, these commands need to be executed (inside source package) to spin up the python gRPC server.

`pip install -r $GOPATH/src/github.com/yash1994/spacy-go/requirements.txt`

Install spacy [language models](https://spacy.io/models) with following command.

`python3 -m spacy download en_core_web_sm`

Connection between client and server is secured by TLS/SSL authentication. Use following command to generate unique pair of root certificate that is used to authenticate the server and private key that only the server has access to.

`openssl req -newkey rsa:2048 -nodes -keyout $GOPATH/src/github.com/yash1994/spacy-go/server.key -x509 -days 365 -out $GOPATH/src/github.com/yash1994/spacy-go/server.crt -subj "/CN=localhost"`

The following command will spin up python gRPC server at `localhost:50051`.

`python3 $GOPATH/src/github.com/yash1994/spacy-go/api/server.py &`

## Usage

```Go
package main

import (
	"fmt"

	spacygo "github.com/yash1994/spacy-go"
)

func main() {

	// load language model
	var modelName string = "en_core_web_sm"
	r, err := spacygo.Load(modelName)

	if err != nil {
		return
	}

	fmt.Printf("%v \n", r.GetMessage())

	// annotate text
	var text string = "I propose to consider the question, 'Can machines think?"

	doc, err := spacygo.Nlp(text)

	// print annotated info : part-of-speech
	for i, token := range doc.GetTokens() {
		fmt.Printf("token %v '%v' part-of-speech tag: %v \n", i, token.GetText(), token.GetPos())
	}

	// calculate text similarity
	var texta string = "I like apples"
	var textb string = "I like oranges"

	textSimilarity, err := spacygo.Similarity(texta, textb)

	fmt.Printf("text similarity between %v and %v is %v", texta, textb, textSimilarity.GetSimilarity())
}
```

## :dizzy: APIs

| Function | Arguments | Return Type | Description |
| -------- | --------- | ----------- | ----------- |
| Load | modelName `string` | [`TextResponse`](docs/textResponse.md), `Error` | Load [spaCy's Language Models](https://spacy.io/usage/models) for text annotations. |
| Nlp | text `string` | [`ParsedNLPRes`](docs/parsedNlpRes.md), `Error` | Annotate (parse, tag, ner) text using previously loaded model. |
| Similarity | texta `string`, textb `string` | [`TextSimilarity`](docs/textSimilarity.md), `Error` | Computes semantic similarity between two sentences using loaded language model. |
| PatternMatch | Array of rule `struct`, text `string` | [`Matches`](docs/patternMatches.md), `Error` | Match sequences of tokens, based on pattern rules. |

## ToDos
* [x] Extensive Test cases
* [x] Error handling server side
* [x] Add SSL and auth
* [x] API Docs
* [x] Similarity API
