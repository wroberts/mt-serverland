# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


DESCRIPTOR = descriptor.FileDescriptor(
  name='TranslationRequestMessage.proto',
  package='serverland',
  serialized_pb='\n\x1fTranslationRequestMessage.proto\x12\nserverland\"\x80\x02\n\x19TranslationRequestMessage\x12\x12\n\nrequest_id\x18\x01 \x02(\t\x12\x17\n\x0fsource_language\x18\x02 \x02(\t\x12\x17\n\x0ftarget_language\x18\x03 \x02(\t\x12\x13\n\x0bsource_text\x18\x04 \x02(\t\x12\x13\n\x0btarget_text\x18\x05 \x01(\t\x12G\n\x0bpacket_data\x18\x06 \x03(\x0b\x32\x32.serverland.TranslationRequestMessage.KeyValuePair\x1a*\n\x0cKeyValuePair\x12\x0b\n\x03key\x18\x01 \x02(\t\x12\r\n\x05value\x18\x02 \x02(\t')




_TRANSLATIONREQUESTMESSAGE_KEYVALUEPAIR = descriptor.Descriptor(
  name='KeyValuePair',
  full_name='serverland.TranslationRequestMessage.KeyValuePair',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='key', full_name='serverland.TranslationRequestMessage.KeyValuePair.key', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='value', full_name='serverland.TranslationRequestMessage.KeyValuePair.value', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=262,
  serialized_end=304,
)

_TRANSLATIONREQUESTMESSAGE = descriptor.Descriptor(
  name='TranslationRequestMessage',
  full_name='serverland.TranslationRequestMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='request_id', full_name='serverland.TranslationRequestMessage.request_id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='source_language', full_name='serverland.TranslationRequestMessage.source_language', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='target_language', full_name='serverland.TranslationRequestMessage.target_language', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='source_text', full_name='serverland.TranslationRequestMessage.source_text', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='target_text', full_name='serverland.TranslationRequestMessage.target_text', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='packet_data', full_name='serverland.TranslationRequestMessage.packet_data', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_TRANSLATIONREQUESTMESSAGE_KEYVALUEPAIR, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=48,
  serialized_end=304,
)


_TRANSLATIONREQUESTMESSAGE_KEYVALUEPAIR.containing_type = _TRANSLATIONREQUESTMESSAGE;
_TRANSLATIONREQUESTMESSAGE.fields_by_name['packet_data'].message_type = _TRANSLATIONREQUESTMESSAGE_KEYVALUEPAIR

class TranslationRequestMessage(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  
  class KeyValuePair(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _TRANSLATIONREQUESTMESSAGE_KEYVALUEPAIR
    
    # @@protoc_insertion_point(class_scope:serverland.TranslationRequestMessage.KeyValuePair)
  DESCRIPTOR = _TRANSLATIONREQUESTMESSAGE
  
  # @@protoc_insertion_point(class_scope:serverland.TranslationRequestMessage)

# @@protoc_insertion_point(module_scope)
