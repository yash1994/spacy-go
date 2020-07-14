import pytest

from python_stubs.nlp_pb2 import TextRequest, TextSimilarityRequest, Rule, Pattern


@pytest.fixture(scope="module")
def grpc_add_to_server():
    from python_stubs.nlp_pb2_grpc import add_NlpServicer_to_server

    return add_NlpServicer_to_server


@pytest.fixture(scope="module")
def grpc_servicer():
    from server import NlpService

    return NlpService()


@pytest.fixture(scope="module")
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


def test_doc_similarity(grpc_stub_cls):
    request = TextSimilarityRequest()
    request.texta = "I like apples"
    request.textb = "I like oranges"
    response = grpc_stub_cls.DocSimilarity(request)
    assert pytest.approx(response.similarity, 0.2) == 0.90


def test_add_matcher(grpc_stub_cls):
    patterns = [{"LOWER": "hello"}, {"LOWER": "world"}]
    rule_id = "HelloWorld"
    request = Rule(
        id=rule_id,
        patterns=[
            Pattern(key=list(pat.keys())[0], value=list(pat.values())[0])
            for pat in patterns
        ],
    )
    response = grpc_stub_cls.AddRule(request)
    assert response.message == "Rule with id '{}' added to matcher.".format(rule_id)


def test_remove_matcher(grpc_stub_cls):
    request = TextRequest(text="HelloWorld")
    response = grpc_stub_cls.RemoveRule(request)
    assert response.message == "Rule with id 'HelloWorld' removed from matcher."


def test_get_matcher(grpc_stub_cls):
    patterns = [{"LOWER": "hello"}, {"LOWER": "world"}]
    rule_id = "HelloWorld"
    request = Rule(
        id=rule_id,
        patterns=[
            Pattern(key=list(pat.keys())[0], value=list(pat.values())[0])
            for pat in patterns
        ],
    )

    _ = grpc_stub_cls.AddRule(request)

    response = grpc_stub_cls.GetRule(TextRequest(text=rule_id))

    assert request.SerializeToString() == response.SerializeToString()


def test_get_matches(grpc_stub_cls):
    patterns = [{"ORTH": "Google"}, {"ORTH": "Maps"}]
    rule_id = "GoogleMaps"
    request = Rule(
        id=rule_id,
        patterns=[
            Pattern(key=list(pat.keys())[0], value=list(pat.values())[0])
            for pat in patterns
        ],
    )

    _ = grpc_stub_cls.AddRule(request)

    response = grpc_stub_cls.GetMatches(TextRequest(text="HELLO WORLD on Google Maps."))

    assert response.matches[0].start == 0
    assert response.matches[0].end == 2
    assert response.matches[1].start == 3
    assert response.matches[1].end == 5


def test_reset_matcher(grpc_stub_cls):
    request = TextRequest(text="")
    response = grpc_stub_cls.ResetMatcher(request)
    
    assert response.message == "Matcher object reset successful."