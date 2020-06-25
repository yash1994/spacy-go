import sys
import grpc
import time
import spacy
import utils
from python_stubs import nlp_pb2
from python_stubs import nlp_pb2_grpc

from concurrent import futures

class NlpService(nlp_pb2_grpc.NlpServicer):
    def __init__(self):
        self.modelName = None
        self.nlp = None

    def LoadModel(self, request, context):
        self.modelName = request.text
        self.nlp = spacy.load(request.text)
        response = nlp_pb2.TextResponse()
        response.message = "Model loaded '{}'".format(request.text)
        return response

    def NlpProcess(self, request, context):
        doc = self.nlp(request.text)
        response = utils.doc2proto(doc, self.modelName)
        return response

def serve(server_address):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    nlp_pb2_grpc.add_NlpServicer_to_server(NlpService(), server)
    server.add_insecure_port(server_address)
    server.start()
    try:
        while True:
            time.sleep(10000)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == "__main__":

    if len(sys.argv) != 2:
        server_address = "localhost:50051"
        print("Default Server Address: {}".format(server_address))
    else:
        server_address = sys.argv[1]
        print("Custom Server Address: {}".format(server_address))
    
    serve(server_address)