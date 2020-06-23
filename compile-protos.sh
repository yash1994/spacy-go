# PBGO_FILE=pbgo/nlp.pb.go
PB2_FILE=api/nlp_pb2.py
PB2_GRPC_FILE=api/nlp_pb2_grpc.py

# if [ -f "$PBGO_FILE" ]; then
#     rm $PBGO_FILE
# fi

if [ -f "$PB2_FILE" ]; then
    rm $PB2_FILE
fi

if [ -f "$PB2_GRPC_FILE" ]; then
    rm $PB2_GRPC_FILE
fi

# mkdir pbgo

python3 -m grpc_tools.protoc --proto_path=protos --python_out=api --grpc_python_out=api protos/nlp.proto
# protoc --proto_path=protos --go_out=plugins=grpc:pbgo protos/nlp.proto