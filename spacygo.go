package spacygo

import (
	"context"
	"flag"
	"log"
	"os/exec"
	"time"

	pb "github.com/yash1994/spacy-go/pbgo"

	"google.golang.org/grpc"
)

var (
	serverAddr   = flag.String("server_addr", "localhost:50051", "The server address in the format of host:port")
	defaultModel = flag.String("model_name", "en_core_web_sm", "Name of default language model to be loaded for NLP")
	serverPath   = flag.String("server_path", "api/server.py", "Path to NLP server file")
)

var grpcConnection *grpc.ClientConn
var grpcConnError error
var grpcClient pb.NlpClient

func load(modelName string) string {
	if modelName == "" {
		modelName = *defaultModel
	}
	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	defer cancel()

	r, err := grpcClient.LoadModel(ctx, &pb.TextRequest{Text: modelName})

	if err != nil {
		return r.GetMessage()
	}
	return err.Error()
}

func initiateServer() {
	cmd := exec.Command("python3", *serverPath, *serverAddr)
	if err := cmd.Start(); err == nil {
		return
	}
	log.Fatalf("Could not initiate python NLP server")
}

func init() {

	// Set up python server.
	// initiateServer()

	// Set up a connection to the server.
	grpcConnection, grpcConnError = grpc.Dial(*serverAddr, grpc.WithInsecure(), grpc.WithBlock())

	if grpcConnError != nil {
		log.Fatalf("Could not connect to server: %v", grpcConnError)
	}
	defer grpcConnection.Close()

	grpcClient = pb.NewNlpClient(grpcConnection)
}
