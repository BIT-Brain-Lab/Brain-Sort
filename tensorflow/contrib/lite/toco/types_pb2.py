# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/contrib/lite/toco/types.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorflow/contrib/lite/toco/types.proto',
  package='toco',
  syntax='proto2',
  serialized_pb=_b('\n(tensorflow/contrib/lite/toco/types.proto\x12\x04toco*}\n\nIODataType\x12\x18\n\x14IO_DATA_TYPE_UNKNOWN\x10\x00\x12\t\n\x05\x46LOAT\x10\x01\x12\x13\n\x0fQUANTIZED_UINT8\x10\x02\x12\t\n\x05INT32\x10\x03\x12\t\n\x05INT64\x10\x04\x12\n\n\x06STRING\x10\x05\x12\x13\n\x0fQUANTIZED_INT16\x10\x06')
)

_IODATATYPE = _descriptor.EnumDescriptor(
  name='IODataType',
  full_name='toco.IODataType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='IO_DATA_TYPE_UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLOAT', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUANTIZED_UINT8', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INT32', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INT64', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STRING', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUANTIZED_INT16', index=6, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=50,
  serialized_end=175,
)
_sym_db.RegisterEnumDescriptor(_IODATATYPE)

IODataType = enum_type_wrapper.EnumTypeWrapper(_IODATATYPE)
IO_DATA_TYPE_UNKNOWN = 0
FLOAT = 1
QUANTIZED_UINT8 = 2
INT32 = 3
INT64 = 4
STRING = 5
QUANTIZED_INT16 = 6


DESCRIPTOR.enum_types_by_name['IODataType'] = _IODATATYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
