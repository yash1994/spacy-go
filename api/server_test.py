import pytest

from python_stubs.nlp_pb2 import TextRequest

@pytest.fixture(scope='module')
def grpc_add_to_server():
    from python_stubs.nlp_pb2_grpc import add_NlpServicer_to_server

    return add_NlpServicer_to_server

@pytest.fixture(scope='module')
def grpc_servicer():
    from server import NlpService

    return NlpService()

@pytest.fixture(scope='module')
def grpc_stub_cls(grpc_channel):
    from python_stubs.nlp_pb2_grpc import NlpStub

    return NlpStub(grpc_channel)

def test_load_model(grpc_stub_cls):
    request = TextRequest()
    request.text = "en_core_web_sm"
    response = grpc_stub_cls.LoadModel(request)

    assert response.message == "Model loaded 'en_core_web_sm'"

def test_nlp_process(grpc_stub_cls):
    request = TextRequest()
    request.text = "This is a text."
    response = grpc_stub_cls.NlpProcess(request)
    assert response.doc.text == "This is a text."
    assert response.tokens[0].pos == "DET"
    assert response.tokens[0].dep == "nsubj"
    assert response.tokens[3].pos == "NOUN"
    assert response.tokens[3].is_alpha == True
