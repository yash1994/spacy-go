package spacygo

import (
	"context"
	"log"
	"os"
	"path"
	"time"

	pb "github.com/yash1994/spacy-go/go-stubs"

	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials"
)

const (
	serverAddr   string = "localhost:50051"
	defaultModel string = "en_core_web_sm"
)

var grpcConnection *grpc.ClientConn
var grpcConnError error
var grpcClient pb.NlpClient

// Load : load language model
func Load(modelName string) (r *pb.TextResponse, err error) {
	if modelName == "" {
		modelName = defaultModel
	}
	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	defer cancel()

	r, err = grpcClient.LoadModel(ctx, &pb.TextRequest{Text: modelName})

	if err != nil {
		return nil, err
	}

	return r, nil
}

// Nlp : annotate text
func Nlp(text string) (r *pb.ParsedNLPRes, err error) {
	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	defer cancel()

	r, err = grpcClient.NlpProcess(ctx, &pb.TextRequest{Text: text})

	if err != nil {
		return nil, err
	}
	return r, nil
}

// Similarity : compute vector similarity between two texts
func Similarity(texta string, textb string) (r *pb.TextSimilarity, err error) {
	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	defer cancel()

	r, err = grpcClient.DocSimilarity(ctx, &pb.TextSimilarityRequest{Texta: texta, Textb: textb})

	if err != nil {
		return nil, err
	}
	return r, nil
}

func init() {

	// Set up a connection to the server.
	var tslFilePath string = path.Join(os.Getenv("GOPATH"), "src/github.com/yash1994/spacy-go/server.key")

	// SSL Credentials
	clientCert, err := credentials.NewClientTLSFromFile(tslFilePath, "")

	if err != nil {
		log.Fatalf("Could not create client SSL certificate: %v", err)
	}

	grpcConnection, grpcConnError = grpc.Dial(serverAddr, grpc.WithTransportCredentials(clientCert), grpc.WithBlock())

	if grpcConnError != nil {
		log.Fatalf("Could not connect to server: %v", grpcConnError)
	}

	//defer grpcConnection.Close()

	grpcClient = pb.NewNlpClient(grpcConnection)

}
