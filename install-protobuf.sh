#!/bin/sh
set -ex
wget https://github.com/protocolbuffers/protobuf/releases/download/v3.12.3/protobuf-all-3.12.3.tar.gz
tar -xzvf protobuf-all-3.12.3.tar.gz
cd protobuf-3.12.3 && ./configure --prefix=/usr && make && sudo make install && rm -rf protobuf-3.12.3