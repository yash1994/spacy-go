# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nlp.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='nlp.proto',
  package='nlp',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\tnlp.proto\x12\x03nlp\"\x1b\n\x0bTextRequest\x12\x0c\n\x04text\x18\x01 \x01(\t\"\x1f\n\x0cTextResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"w\n\x03\x44oc\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x14\n\x0ctext_with_ws\x18\x02 \x01(\t\x12\x11\n\tis_tagged\x18\x03 \x01(\x08\x12\x11\n\tis_parsed\x18\x04 \x01(\x08\x12\x10\n\x08is_nered\x18\x05 \x01(\x08\x12\x14\n\x0cis_sentenced\x18\x06 \x01(\x08\"0\n\x03\x45nt\x12\r\n\x05start\x18\x01 \x01(\x05\x12\x0b\n\x03\x65nd\x18\x02 \x01(\x05\x12\r\n\x05label\x18\x03 \x01(\t\"\"\n\x04Sent\x12\r\n\x05start\x18\x01 \x01(\x05\x12\x0b\n\x03\x65nd\x18\x02 \x01(\x05\"(\n\nNoun_chunk\x12\r\n\x05start\x18\x01 \x01(\x05\x12\x0b\n\x03\x65nd\x18\x02 \x01(\x05\"\xca\x04\n\x05Token\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x14\n\x0ctext_with_ws\x18\x02 \x01(\t\x12\x12\n\nwhitespace\x18\x03 \x01(\t\x12\x10\n\x08\x65nt_type\x18\x05 \x01(\t\x12\x0f\n\x07\x65nt_iob\x18\x06 \x01(\t\x12\r\n\x05lemma\x18\x07 \x01(\t\x12\x0c\n\x04norm\x18\x08 \x01(\t\x12\r\n\x05lower\x18\t \x01(\t\x12\r\n\x05shape\x18\n \x01(\t\x12\x0e\n\x06prefix\x18\x0b \x01(\t\x12\x0e\n\x06suffix\x18\x0c \x01(\t\x12\x0b\n\x03pos\x18\r \x01(\t\x12\x0b\n\x03tag\x18\x0e \x01(\t\x12\x0b\n\x03\x64\x65p\x18\x0f \x01(\t\x12\x10\n\x08is_alpha\x18\x10 \x01(\x08\x12\x10\n\x08is_ascii\x18\x11 \x01(\x08\x12\x10\n\x08is_digit\x18\x12 \x01(\x08\x12\x10\n\x08is_lower\x18\x13 \x01(\x08\x12\x10\n\x08is_upper\x18\x14 \x01(\x08\x12\x10\n\x08is_title\x18\x15 \x01(\x08\x12\x10\n\x08is_punct\x18\x16 \x01(\x08\x12\x15\n\ris_left_punct\x18\x17 \x01(\x08\x12\x16\n\x0eis_right_punct\x18\x18 \x01(\x08\x12\x10\n\x08is_space\x18\x19 \x01(\x08\x12\x12\n\nis_bracket\x18\x1a \x01(\x08\x12\x13\n\x0bis_currency\x18\x1b \x01(\x08\x12\x10\n\x08like_url\x18\x1c \x01(\x08\x12\x10\n\x08like_num\x18\x1d \x01(\x08\x12\x12\n\nlike_email\x18\x1e \x01(\x08\x12\x0e\n\x06is_oov\x18\x1f \x01(\x08\x12\x0f\n\x07is_stop\x18  \x01(\x08\x12\x15\n\ris_sent_start\x18! \x01(\x08\x12\x0c\n\x04head\x18\" \x01(\x05\"\xa8\x01\n\x0cParsedNLPRes\x12\r\n\x05model\x18\x01 \x01(\t\x12\x15\n\x03\x64oc\x18\x02 \x01(\x0b\x32\x08.nlp.Doc\x12\x16\n\x04\x65nts\x18\x03 \x03(\x0b\x32\x08.nlp.Ent\x12\x18\n\x05sents\x18\x04 \x03(\x0b\x32\t.nlp.Sent\x12$\n\x0bnoun_chunks\x18\x05 \x03(\x0b\x32\x0f.nlp.Noun_chunk\x12\x1a\n\x06tokens\x18\x06 \x03(\x0b\x32\n.nlp.Token2n\n\x03Nlp\x12\x32\n\tLoadModel\x12\x10.nlp.TextRequest\x1a\x11.nlp.TextResponse\"\x00\x12\x33\n\nNlpProcess\x12\x10.nlp.TextRequest\x1a\x11.nlp.ParsedNLPRes\"\x00\x62\x06proto3'
)




_TEXTREQUEST = _descriptor.Descriptor(
  name='TextRequest',
  full_name='nlp.TextRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='nlp.TextRequest.text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=45,
)


_TEXTRESPONSE = _descriptor.Descriptor(
  name='TextResponse',
  full_name='nlp.TextResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='nlp.TextResponse.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=47,
  serialized_end=78,
)


_DOC = _descriptor.Descriptor(
  name='Doc',
  full_name='nlp.Doc',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='nlp.Doc.text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text_with_ws', full_name='nlp.Doc.text_with_ws', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_tagged', full_name='nlp.Doc.is_tagged', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_parsed', full_name='nlp.Doc.is_parsed', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_nered', full_name='nlp.Doc.is_nered', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_sentenced', full_name='nlp.Doc.is_sentenced', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=80,
  serialized_end=199,
)


_ENT = _descriptor.Descriptor(
  name='Ent',
  full_name='nlp.Ent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start', full_name='nlp.Ent.start', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end', full_name='nlp.Ent.end', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='label', full_name='nlp.Ent.label', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=201,
  serialized_end=249,
)


_SENT = _descriptor.Descriptor(
  name='Sent',
  full_name='nlp.Sent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start', full_name='nlp.Sent.start', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end', full_name='nlp.Sent.end', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=251,
  serialized_end=285,
)


_NOUN_CHUNK = _descriptor.Descriptor(
  name='Noun_chunk',
  full_name='nlp.Noun_chunk',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start', full_name='nlp.Noun_chunk.start', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end', full_name='nlp.Noun_chunk.end', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=287,
  serialized_end=327,
)


_TOKEN = _descriptor.Descriptor(
  name='Token',
  full_name='nlp.Token',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='nlp.Token.text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text_with_ws', full_name='nlp.Token.text_with_ws', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='whitespace', full_name='nlp.Token.whitespace', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ent_type', full_name='nlp.Token.ent_type', index=3,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ent_iob', full_name='nlp.Token.ent_iob', index=4,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lemma', full_name='nlp.Token.lemma', index=5,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='norm', full_name='nlp.Token.norm', index=6,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lower', full_name='nlp.Token.lower', index=7,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shape', full_name='nlp.Token.shape', index=8,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prefix', full_name='nlp.Token.prefix', index=9,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='suffix', full_name='nlp.Token.suffix', index=10,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pos', full_name='nlp.Token.pos', index=11,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tag', full_name='nlp.Token.tag', index=12,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dep', full_name='nlp.Token.dep', index=13,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_alpha', full_name='nlp.Token.is_alpha', index=14,
      number=16, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_ascii', full_name='nlp.Token.is_ascii', index=15,
      number=17, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_digit', full_name='nlp.Token.is_digit', index=16,
      number=18, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_lower', full_name='nlp.Token.is_lower', index=17,
      number=19, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_upper', full_name='nlp.Token.is_upper', index=18,
      number=20, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_title', full_name='nlp.Token.is_title', index=19,
      number=21, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_punct', full_name='nlp.Token.is_punct', index=20,
      number=22, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_left_punct', full_name='nlp.Token.is_left_punct', index=21,
      number=23, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_right_punct', full_name='nlp.Token.is_right_punct', index=22,
      number=24, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_space', full_name='nlp.Token.is_space', index=23,
      number=25, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_bracket', full_name='nlp.Token.is_bracket', index=24,
      number=26, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_currency', full_name='nlp.Token.is_currency', index=25,
      number=27, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='like_url', full_name='nlp.Token.like_url', index=26,
      number=28, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='like_num', full_name='nlp.Token.like_num', index=27,
      number=29, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='like_email', full_name='nlp.Token.like_email', index=28,
      number=30, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_oov', full_name='nlp.Token.is_oov', index=29,
      number=31, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_stop', full_name='nlp.Token.is_stop', index=30,
      number=32, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_sent_start', full_name='nlp.Token.is_sent_start', index=31,
      number=33, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='head', full_name='nlp.Token.head', index=32,
      number=34, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=330,
  serialized_end=916,
)


_PARSEDNLPRES = _descriptor.Descriptor(
  name='ParsedNLPRes',
  full_name='nlp.ParsedNLPRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='model', full_name='nlp.ParsedNLPRes.model', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='doc', full_name='nlp.ParsedNLPRes.doc', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ents', full_name='nlp.ParsedNLPRes.ents', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sents', full_name='nlp.ParsedNLPRes.sents', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='noun_chunks', full_name='nlp.ParsedNLPRes.noun_chunks', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tokens', full_name='nlp.ParsedNLPRes.tokens', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=919,
  serialized_end=1087,
)

_PARSEDNLPRES.fields_by_name['doc'].message_type = _DOC
_PARSEDNLPRES.fields_by_name['ents'].message_type = _ENT
_PARSEDNLPRES.fields_by_name['sents'].message_type = _SENT
_PARSEDNLPRES.fields_by_name['noun_chunks'].message_type = _NOUN_CHUNK
_PARSEDNLPRES.fields_by_name['tokens'].message_type = _TOKEN
DESCRIPTOR.message_types_by_name['TextRequest'] = _TEXTREQUEST
DESCRIPTOR.message_types_by_name['TextResponse'] = _TEXTRESPONSE
DESCRIPTOR.message_types_by_name['Doc'] = _DOC
DESCRIPTOR.message_types_by_name['Ent'] = _ENT
DESCRIPTOR.message_types_by_name['Sent'] = _SENT
DESCRIPTOR.message_types_by_name['Noun_chunk'] = _NOUN_CHUNK
DESCRIPTOR.message_types_by_name['Token'] = _TOKEN
DESCRIPTOR.message_types_by_name['ParsedNLPRes'] = _PARSEDNLPRES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TextRequest = _reflection.GeneratedProtocolMessageType('TextRequest', (_message.Message,), {
  'DESCRIPTOR' : _TEXTREQUEST,
  '__module__' : 'nlp_pb2'
  # @@protoc_insertion_point(class_scope:nlp.TextRequest)
  })
_sym_db.RegisterMessage(TextRequest)

TextResponse = _reflection.GeneratedProtocolMessageType('TextResponse', (_message.Message,), {
  'DESCRIPTOR' : _TEXTRESPONSE,
  '__module__' : 'nlp_pb2'
  # @@protoc_insertion_point(class_scope:nlp.TextResponse)
  })
_sym_db.RegisterMessage(TextResponse)

Doc = _reflection.GeneratedProtocolMessageType('Doc', (_message.Message,), {
  'DESCRIPTOR' : _DOC,
  '__module__' : 'nlp_pb2'
  # @@protoc_insertion_point(class_scope:nlp.Doc)
  })
_sym_db.RegisterMessage(Doc)

Ent = _reflection.GeneratedProtocolMessageType('Ent', (_message.Message,), {
  'DESCRIPTOR' : _ENT,
  '__module__' : 'nlp_pb2'
  # @@protoc_insertion_point(class_scope:nlp.Ent)
  })
_sym_db.RegisterMessage(Ent)

Sent = _reflection.GeneratedProtocolMessageType('Sent', (_message.Message,), {
  'DESCRIPTOR' : _SENT,
  '__module__' : 'nlp_pb2'
  # @@protoc_insertion_point(class_scope:nlp.Sent)
  })
_sym_db.RegisterMessage(Sent)

Noun_chunk = _reflection.GeneratedProtocolMessageType('Noun_chunk', (_message.Message,), {
  'DESCRIPTOR' : _NOUN_CHUNK,
  '__module__' : 'nlp_pb2'
  # @@protoc_insertion_point(class_scope:nlp.Noun_chunk)
  })
_sym_db.RegisterMessage(Noun_chunk)

Token = _reflection.GeneratedProtocolMessageType('Token', (_message.Message,), {
  'DESCRIPTOR' : _TOKEN,
  '__module__' : 'nlp_pb2'
  # @@protoc_insertion_point(class_scope:nlp.Token)
  })
_sym_db.RegisterMessage(Token)

ParsedNLPRes = _reflection.GeneratedProtocolMessageType('ParsedNLPRes', (_message.Message,), {
  'DESCRIPTOR' : _PARSEDNLPRES,
  '__module__' : 'nlp_pb2'
  # @@protoc_insertion_point(class_scope:nlp.ParsedNLPRes)
  })
_sym_db.RegisterMessage(ParsedNLPRes)



_NLP = _descriptor.ServiceDescriptor(
  name='Nlp',
  full_name='nlp.Nlp',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1089,
  serialized_end=1199,
  methods=[
  _descriptor.MethodDescriptor(
    name='LoadModel',
    full_name='nlp.Nlp.LoadModel',
    index=0,
    containing_service=None,
    input_type=_TEXTREQUEST,
    output_type=_TEXTRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='NlpProcess',
    full_name='nlp.Nlp.NlpProcess',
    index=1,
    containing_service=None,
    input_type=_TEXTREQUEST,
    output_type=_PARSEDNLPRES,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_NLP)

DESCRIPTOR.services_by_name['Nlp'] = _NLP

# @@protoc_insertion_point(module_scope)