# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: RRWorkload.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10RRWorkload.proto\"\x94\x01\n\x03RFW\x12\x0e\n\x06rfw_id\x18\x01 \x01(\x05\x12\x16\n\x0e\x62\x65nchmark_type\x18\x02 \x01(\x05\x12\x17\n\x0fworkload_metric\x18\x03 \x01(\x05\x12\x12\n\nbatch_unit\x18\x04 \x01(\x05\x12\x10\n\x08\x62\x61tch_id\x18\x05 \x01(\x05\x12\x12\n\nbatch_size\x18\x06 \x01(\x05\x12\x12\n\nbatch_type\x18\x07 \x01(\x05\"L\n\x03RFD\x12\x0e\n\x06rfw_id\x18\x01 \x01(\x05\x12\x15\n\rlast_batch_id\x18\x02 \x01(\x05\x12\x1e\n\x16\x64\x61ta_samples_requested\x18\x03 \x03(\x02\x32-\n\x0fWorkloadService\x12\x1a\n\x0cWorkloadData\x12\x04.RFW\x1a\x04.RFDb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'RRWorkload_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _RFW._serialized_start=21
  _RFW._serialized_end=169
  _RFD._serialized_start=171
  _RFD._serialized_end=247
  _WORKLOADSERVICE._serialized_start=249
  _WORKLOADSERVICE._serialized_end=294
# @@protoc_insertion_point(module_scope)
