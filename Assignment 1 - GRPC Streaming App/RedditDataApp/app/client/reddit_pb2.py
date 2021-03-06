# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: reddit.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='reddit.proto',
  package='app',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0creddit.proto\x12\x03\x61pp\"\x1f\n\x0bPostRequest\x12\x10\n\x08response\x18\x01 \x01(\t\"\xf2\x01\n\x07GetPost\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\r\n\x05score\x18\x03 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x04 \x01(\t\x12\x19\n\x11\x61uthor_flair_text\x18\x05 \x01(\t\x12\x12\n\nremoved_by\x18\x06 \x01(\t\x12\x1d\n\x15total_awards_received\x18\x07 \x01(\t\x12\x10\n\x08\x61warders\x18\x08 \x01(\t\x12\x13\n\x0b\x63reated_utc\x18\t \x01(\t\x12\x11\n\tfull_link\x18\n \x01(\t\x12\x14\n\x0cnum_comments\x18\x0b \x01(\t\x12\x0f\n\x07over_18\x18\x0c \x01(\t28\n\x06Reddit\x12.\n\x08SendPost\x12\x10.app.PostRequest\x1a\x0c.app.GetPost\"\x00\x30\x01\x62\x06proto3'
)




_POSTREQUEST = _descriptor.Descriptor(
  name='PostRequest',
  full_name='app.PostRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='app.PostRequest.response', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=21,
  serialized_end=52,
)


_GETPOST = _descriptor.Descriptor(
  name='GetPost',
  full_name='app.GetPost',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='app.GetPost.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='title', full_name='app.GetPost.title', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='score', full_name='app.GetPost.score', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='author', full_name='app.GetPost.author', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='author_flair_text', full_name='app.GetPost.author_flair_text', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='removed_by', full_name='app.GetPost.removed_by', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_awards_received', full_name='app.GetPost.total_awards_received', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='awarders', full_name='app.GetPost.awarders', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_utc', full_name='app.GetPost.created_utc', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='full_link', full_name='app.GetPost.full_link', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='num_comments', full_name='app.GetPost.num_comments', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='over_18', full_name='app.GetPost.over_18', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=55,
  serialized_end=297,
)

DESCRIPTOR.message_types_by_name['PostRequest'] = _POSTREQUEST
DESCRIPTOR.message_types_by_name['GetPost'] = _GETPOST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PostRequest = _reflection.GeneratedProtocolMessageType('PostRequest', (_message.Message,), {
  'DESCRIPTOR' : _POSTREQUEST,
  '__module__' : 'reddit_pb2'
  # @@protoc_insertion_point(class_scope:app.PostRequest)
  })
_sym_db.RegisterMessage(PostRequest)

GetPost = _reflection.GeneratedProtocolMessageType('GetPost', (_message.Message,), {
  'DESCRIPTOR' : _GETPOST,
  '__module__' : 'reddit_pb2'
  # @@protoc_insertion_point(class_scope:app.GetPost)
  })
_sym_db.RegisterMessage(GetPost)



_REDDIT = _descriptor.ServiceDescriptor(
  name='Reddit',
  full_name='app.Reddit',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=299,
  serialized_end=355,
  methods=[
  _descriptor.MethodDescriptor(
    name='SendPost',
    full_name='app.Reddit.SendPost',
    index=0,
    containing_service=None,
    input_type=_POSTREQUEST,
    output_type=_GETPOST,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_REDDIT)

DESCRIPTOR.services_by_name['Reddit'] = _REDDIT

# @@protoc_insertion_point(module_scope)
