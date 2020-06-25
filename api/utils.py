from python_stubs import nlp_pb2

def doc2proto(doc, model):
    proto = nlp_pb2.ParsedNLPRes()
    proto.model = model
    
    protoDoc = nlp_pb2.Doc()
    protoDoc.text = doc.text
    protoDoc.text_with_ws = doc.text_with_ws
    protoDoc.is_tagged = doc.is_tagged
    protoDoc.is_parsed = doc.is_parsed
    protoDoc.is_nered = doc.is_nered
    protoDoc.is_sentenced = doc.is_sentenced

    if doc.ents:
        protoEnts = []
        for ent in doc.ents:
            protoEnt = nlp_pb2.Ent()
            protoEnt.start = ent.start
            protoEnt.end = ent.end
            protoEnt.label = ent.label_
            protoEnts.append(protoEnt)
    else:
        protoEnts = []        

    if doc.is_sentenced:
        protoSents = []
        for sent in doc.sents:
            protoSent = nlp_pb2.Sent()
            protoSent.start = sent.start
            protoSent.end = sent.end
            protoSents.append(protoSent)
    else:
        protoSents = []

    if doc.is_tagged and doc.is_parsed:
        protoNounChunks = []
        for chunk in doc.noun_chunks:
            protoNounChunk = nlp_pb2.Noun_chunk()
            protoNounChunk.start = chunk.start
            protoNounChunk.end = chunk.end
            protoNounChunks.append(protoNounChunk)
    else:
        protoNounChunks = []

    protoTokens = []
    for token in doc:
        protoToken = nlp_pb2.Token()
        protoToken.text = token.text
        protoToken.text_with_ws = token.text_with_ws
        protoToken.whitespace = token.whitespace_
        protoToken.ent_type = token.ent_type_
        protoToken.ent_iob = token.ent_iob_
        protoToken.lemma = token.lemma_
        protoToken.norm = token.norm_
        protoToken.lower = token.lower_
        protoToken.shape = token.shape_
        protoToken.prefix = token.prefix_
        protoToken.suffix = token.suffix_
        protoToken.pos = token.pos_
        protoToken.tag = token.tag_
        protoToken.dep = token.dep_
        protoToken.is_alpha = token.is_alpha
        protoToken.is_ascii = token.is_ascii
        protoToken.is_digit = token.is_digit
        protoToken.is_lower = token.is_lower
        protoToken.is_upper = token.is_upper
        protoToken.is_title = token.is_title
        protoToken.is_punct = token.is_punct
        protoToken.is_left_punct = token.is_left_punct
        protoToken.is_right_punct = token.is_right_punct
        protoToken.is_space = token.is_space
        protoToken.is_bracket = token.is_bracket
        protoToken.is_currency = token.is_currency
        protoToken.like_url = token.like_url
        protoToken.like_num = token.like_num
        protoToken.like_email = token.like_email
        protoToken.is_oov = token.is_oov
        protoToken.is_stop = token.is_stop
        protoToken.is_sent_start = token.is_sent_start if token.is_sent_start is not None else False
        protoToken.head = token.head.i
        protoTokens.append(protoToken)

    proto.doc.MergeFrom(protoDoc)
    proto.ents.MergeFrom(protoEnts)
    proto.sents.MergeFrom(protoSents)
    proto.noun_chunks.MergeFrom(protoNounChunks)
    proto.tokens.MergeFrom(protoTokens)

    return proto