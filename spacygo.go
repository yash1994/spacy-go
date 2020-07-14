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

type pattern struct {
	key, value string
}

type rule struct {
	id       string
	patterns []pattern
}

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

// PatternMatch : Match sequences of tokens, based on pattern rules
func PatternMatch(matchrules []rule, text string) (r *pb.Matches, err error) {
	for _, mrule := range matchrules {

		var tempRuleArray []*pb.Pattern

		for _, pat := range mrule.patterns {
			patpb := &pb.Pattern{Key: pat.key, Value: pat.value}
			tempRuleArray = append(tempRuleArray, patpb)
		}
		rulepb := &pb.Rule{Id: mrule.id, Patterns: tempRuleArray}

		arctx, arcancle := context.WithTimeout(context.Background(), time.Second)
		defer arcancle()

		arresp, arerror := grpcClient.AddRule(arctx, rulepb)

		if arerror != nil {
			log.Fatalf("Add rule error: %v", arerror.Error())
		} else {
			log.Printf("%v", arresp.GetMessage())
		}

	}
	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	defer cancel()

	r, err = grpcClient.GetMatches(ctx, &pb.TextRequest{Text: text})

	rsctx, rscancel := context.WithTimeout(context.Background(), time.Second)

	resetresp, reseterr := grpcClient.ResetMatcher(rsctx, &pb.TextRequest{Text: ""})
	defer rscancel()

	if reseterr != nil {
		log.Fatalf("Reset Matcher error: %v", reseterr.Error())
	} else {
		log.Printf("%v", resetresp.GetMessage())
	}

	if err != nil {
		return nil, err
	}

	return r, nil

}

func init() {

	// Set up a connection to the server.
	var tslFilePath string

	if _, oserr := os.Stat("server.crt"); oserr == nil {
		tslFilePath = "server.crt"
	} else {
		tslFilePath = path.Join(os.Getenv("GOPATH"), "src/github.com/yash1994/spacy-go/server.crt")
	}

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
