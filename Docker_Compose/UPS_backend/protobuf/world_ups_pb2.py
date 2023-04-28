# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: world_ups.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='world_ups.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0fworld_ups.proto\".\n\nUInitTruck\x12\n\n\x02id\x18\x01 \x02(\x05\x12\t\n\x01x\x18\x02 \x02(\x05\x12\t\n\x01y\x18\x03 \x02(\x05\"J\n\x08UConnect\x12\x0f\n\x07worldid\x18\x01 \x01(\x03\x12\x1b\n\x06trucks\x18\x02 \x03(\x0b\x32\x0b.UInitTruck\x12\x10\n\x08isAmazon\x18\x03 \x02(\x08\"-\n\nUConnected\x12\x0f\n\x07worldid\x18\x01 \x02(\x03\x12\x0e\n\x06result\x18\x02 \x02(\t\":\n\tUGoPickup\x12\x0f\n\x07truckid\x18\x01 \x02(\x05\x12\x0c\n\x04whid\x18\x02 \x02(\x05\x12\x0e\n\x06seqnum\x18\x03 \x02(\x03\"R\n\tUFinished\x12\x0f\n\x07truckid\x18\x01 \x02(\x05\x12\t\n\x01x\x18\x02 \x02(\x05\x12\t\n\x01y\x18\x03 \x02(\x05\x12\x0e\n\x06status\x18\x04 \x02(\t\x12\x0e\n\x06seqnum\x18\x05 \x02(\x03\"C\n\rUDeliveryMade\x12\x0f\n\x07truckid\x18\x01 \x02(\x05\x12\x11\n\tpackageid\x18\x02 \x02(\x03\x12\x0e\n\x06seqnum\x18\x03 \x02(\x03\"<\n\x11UDeliveryLocation\x12\x11\n\tpackageid\x18\x01 \x02(\x03\x12\t\n\x01x\x18\x02 \x02(\x05\x12\t\n\x01y\x18\x03 \x02(\x05\"S\n\nUGoDeliver\x12\x0f\n\x07truckid\x18\x01 \x02(\x05\x12$\n\x08packages\x18\x02 \x03(\x0b\x32\x12.UDeliveryLocation\x12\x0e\n\x06seqnum\x18\x03 \x02(\x03\"9\n\x04UErr\x12\x0b\n\x03\x65rr\x18\x01 \x02(\t\x12\x14\n\x0coriginseqnum\x18\x02 \x02(\x03\x12\x0e\n\x06seqnum\x18\x03 \x02(\x03\")\n\x06UQuery\x12\x0f\n\x07truckid\x18\x01 \x02(\x05\x12\x0e\n\x06seqnum\x18\x02 \x02(\x03\"O\n\x06UTruck\x12\x0f\n\x07truckid\x18\x01 \x02(\x05\x12\x0e\n\x06status\x18\x02 \x02(\t\x12\t\n\x01x\x18\x03 \x02(\x05\x12\t\n\x01y\x18\x04 \x02(\x05\x12\x0e\n\x06seqnum\x18\x05 \x02(\x03\"\x97\x01\n\tUCommands\x12\x1b\n\x07pickups\x18\x01 \x03(\x0b\x32\n.UGoPickup\x12\x1f\n\ndeliveries\x18\x02 \x03(\x0b\x32\x0b.UGoDeliver\x12\x10\n\x08simspeed\x18\x03 \x01(\r\x12\x12\n\ndisconnect\x18\x04 \x01(\x08\x12\x18\n\x07queries\x18\x05 \x03(\x0b\x32\x07.UQuery\x12\x0c\n\x04\x61\x63ks\x18\x06 \x03(\x03\"\xa4\x01\n\nUResponses\x12\x1f\n\x0b\x63ompletions\x18\x01 \x03(\x0b\x32\n.UFinished\x12!\n\tdelivered\x18\x02 \x03(\x0b\x32\x0e.UDeliveryMade\x12\x10\n\x08\x66inished\x18\x03 \x01(\x08\x12\x0c\n\x04\x61\x63ks\x18\x04 \x03(\x03\x12\x1c\n\x0btruckstatus\x18\x05 \x03(\x0b\x32\x07.UTruck\x12\x14\n\x05\x65rror\x18\x06 \x03(\x0b\x32\x05.UErr'
)




_UINITTRUCK = _descriptor.Descriptor(
  name='UInitTruck',
  full_name='UInitTruck',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='UInitTruck.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='x', full_name='UInitTruck.x', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='y', full_name='UInitTruck.y', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=19,
  serialized_end=65,
)


_UCONNECT = _descriptor.Descriptor(
  name='UConnect',
  full_name='UConnect',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='worldid', full_name='UConnect.worldid', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='trucks', full_name='UConnect.trucks', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='isAmazon', full_name='UConnect.isAmazon', index=2,
      number=3, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=67,
  serialized_end=141,
)


_UCONNECTED = _descriptor.Descriptor(
  name='UConnected',
  full_name='UConnected',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='worldid', full_name='UConnected.worldid', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result', full_name='UConnected.result', index=1,
      number=2, type=9, cpp_type=9, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=143,
  serialized_end=188,
)


_UGOPICKUP = _descriptor.Descriptor(
  name='UGoPickup',
  full_name='UGoPickup',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='truckid', full_name='UGoPickup.truckid', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='whid', full_name='UGoPickup.whid', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='seqnum', full_name='UGoPickup.seqnum', index=2,
      number=3, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=190,
  serialized_end=248,
)


_UFINISHED = _descriptor.Descriptor(
  name='UFinished',
  full_name='UFinished',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='truckid', full_name='UFinished.truckid', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='x', full_name='UFinished.x', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='y', full_name='UFinished.y', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='UFinished.status', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='seqnum', full_name='UFinished.seqnum', index=4,
      number=5, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=250,
  serialized_end=332,
)


_UDELIVERYMADE = _descriptor.Descriptor(
  name='UDeliveryMade',
  full_name='UDeliveryMade',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='truckid', full_name='UDeliveryMade.truckid', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='packageid', full_name='UDeliveryMade.packageid', index=1,
      number=2, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='seqnum', full_name='UDeliveryMade.seqnum', index=2,
      number=3, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=334,
  serialized_end=401,
)


_UDELIVERYLOCATION = _descriptor.Descriptor(
  name='UDeliveryLocation',
  full_name='UDeliveryLocation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='packageid', full_name='UDeliveryLocation.packageid', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='x', full_name='UDeliveryLocation.x', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='y', full_name='UDeliveryLocation.y', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=403,
  serialized_end=463,
)


_UGODELIVER = _descriptor.Descriptor(
  name='UGoDeliver',
  full_name='UGoDeliver',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='truckid', full_name='UGoDeliver.truckid', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='packages', full_name='UGoDeliver.packages', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='seqnum', full_name='UGoDeliver.seqnum', index=2,
      number=3, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=465,
  serialized_end=548,
)


_UERR = _descriptor.Descriptor(
  name='UErr',
  full_name='UErr',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='err', full_name='UErr.err', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='originseqnum', full_name='UErr.originseqnum', index=1,
      number=2, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='seqnum', full_name='UErr.seqnum', index=2,
      number=3, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=550,
  serialized_end=607,
)


_UQUERY = _descriptor.Descriptor(
  name='UQuery',
  full_name='UQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='truckid', full_name='UQuery.truckid', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='seqnum', full_name='UQuery.seqnum', index=1,
      number=2, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=609,
  serialized_end=650,
)


_UTRUCK = _descriptor.Descriptor(
  name='UTruck',
  full_name='UTruck',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='truckid', full_name='UTruck.truckid', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='UTruck.status', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='x', full_name='UTruck.x', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='y', full_name='UTruck.y', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='seqnum', full_name='UTruck.seqnum', index=4,
      number=5, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=652,
  serialized_end=731,
)


_UCOMMANDS = _descriptor.Descriptor(
  name='UCommands',
  full_name='UCommands',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='pickups', full_name='UCommands.pickups', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='deliveries', full_name='UCommands.deliveries', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='simspeed', full_name='UCommands.simspeed', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='disconnect', full_name='UCommands.disconnect', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='queries', full_name='UCommands.queries', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='acks', full_name='UCommands.acks', index=5,
      number=6, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=734,
  serialized_end=885,
)


_URESPONSES = _descriptor.Descriptor(
  name='UResponses',
  full_name='UResponses',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='completions', full_name='UResponses.completions', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='delivered', full_name='UResponses.delivered', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='finished', full_name='UResponses.finished', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='acks', full_name='UResponses.acks', index=3,
      number=4, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='truckstatus', full_name='UResponses.truckstatus', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error', full_name='UResponses.error', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=888,
  serialized_end=1052,
)

_UCONNECT.fields_by_name['trucks'].message_type = _UINITTRUCK
_UGODELIVER.fields_by_name['packages'].message_type = _UDELIVERYLOCATION
_UCOMMANDS.fields_by_name['pickups'].message_type = _UGOPICKUP
_UCOMMANDS.fields_by_name['deliveries'].message_type = _UGODELIVER
_UCOMMANDS.fields_by_name['queries'].message_type = _UQUERY
_URESPONSES.fields_by_name['completions'].message_type = _UFINISHED
_URESPONSES.fields_by_name['delivered'].message_type = _UDELIVERYMADE
_URESPONSES.fields_by_name['truckstatus'].message_type = _UTRUCK
_URESPONSES.fields_by_name['error'].message_type = _UERR
DESCRIPTOR.message_types_by_name['UInitTruck'] = _UINITTRUCK
DESCRIPTOR.message_types_by_name['UConnect'] = _UCONNECT
DESCRIPTOR.message_types_by_name['UConnected'] = _UCONNECTED
DESCRIPTOR.message_types_by_name['UGoPickup'] = _UGOPICKUP
DESCRIPTOR.message_types_by_name['UFinished'] = _UFINISHED
DESCRIPTOR.message_types_by_name['UDeliveryMade'] = _UDELIVERYMADE
DESCRIPTOR.message_types_by_name['UDeliveryLocation'] = _UDELIVERYLOCATION
DESCRIPTOR.message_types_by_name['UGoDeliver'] = _UGODELIVER
DESCRIPTOR.message_types_by_name['UErr'] = _UERR
DESCRIPTOR.message_types_by_name['UQuery'] = _UQUERY
DESCRIPTOR.message_types_by_name['UTruck'] = _UTRUCK
DESCRIPTOR.message_types_by_name['UCommands'] = _UCOMMANDS
DESCRIPTOR.message_types_by_name['UResponses'] = _URESPONSES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UInitTruck = _reflection.GeneratedProtocolMessageType('UInitTruck', (_message.Message,), {
  'DESCRIPTOR' : _UINITTRUCK,
  '__module__' : 'world_ups_pb2'
  # @@protoc_insertion_point(class_scope:UInitTruck)
  })
_sym_db.RegisterMessage(UInitTruck)

UConnect = _reflection.GeneratedProtocolMessageType('UConnect', (_message.Message,), {
  'DESCRIPTOR' : _UCONNECT,
  '__module__' : 'world_ups_pb2'
  # @@protoc_insertion_point(class_scope:UConnect)
  })
_sym_db.RegisterMessage(UConnect)

UConnected = _reflection.GeneratedProtocolMessageType('UConnected', (_message.Message,), {
  'DESCRIPTOR' : _UCONNECTED,
  '__module__' : 'world_ups_pb2'
  # @@protoc_insertion_point(class_scope:UConnected)
  })
_sym_db.RegisterMessage(UConnected)

UGoPickup = _reflection.GeneratedProtocolMessageType('UGoPickup', (_message.Message,), {
  'DESCRIPTOR' : _UGOPICKUP,
  '__module__' : 'world_ups_pb2'
  # @@protoc_insertion_point(class_scope:UGoPickup)
  })
_sym_db.RegisterMessage(UGoPickup)

UFinished = _reflection.GeneratedProtocolMessageType('UFinished', (_message.Message,), {
  'DESCRIPTOR' : _UFINISHED,
  '__module__' : 'world_ups_pb2'
  # @@protoc_insertion_point(class_scope:UFinished)
  })
_sym_db.RegisterMessage(UFinished)

UDeliveryMade = _reflection.GeneratedProtocolMessageType('UDeliveryMade', (_message.Message,), {
  'DESCRIPTOR' : _UDELIVERYMADE,
  '__module__' : 'world_ups_pb2'
  # @@protoc_insertion_point(class_scope:UDeliveryMade)
  })
_sym_db.RegisterMessage(UDeliveryMade)

UDeliveryLocation = _reflection.GeneratedProtocolMessageType('UDeliveryLocation', (_message.Message,), {
  'DESCRIPTOR' : _UDELIVERYLOCATION,
  '__module__' : 'world_ups_pb2'
  # @@protoc_insertion_point(class_scope:UDeliveryLocation)
  })
_sym_db.RegisterMessage(UDeliveryLocation)

UGoDeliver = _reflection.GeneratedProtocolMessageType('UGoDeliver', (_message.Message,), {
  'DESCRIPTOR' : _UGODELIVER,
  '__module__' : 'world_ups_pb2'
  # @@protoc_insertion_point(class_scope:UGoDeliver)
  })
_sym_db.RegisterMessage(UGoDeliver)

UErr = _reflection.GeneratedProtocolMessageType('UErr', (_message.Message,), {
  'DESCRIPTOR' : _UERR,
  '__module__' : 'world_ups_pb2'
  # @@protoc_insertion_point(class_scope:UErr)
  })
_sym_db.RegisterMessage(UErr)

UQuery = _reflection.GeneratedProtocolMessageType('UQuery', (_message.Message,), {
  'DESCRIPTOR' : _UQUERY,
  '__module__' : 'world_ups_pb2'
  # @@protoc_insertion_point(class_scope:UQuery)
  })
_sym_db.RegisterMessage(UQuery)

UTruck = _reflection.GeneratedProtocolMessageType('UTruck', (_message.Message,), {
  'DESCRIPTOR' : _UTRUCK,
  '__module__' : 'world_ups_pb2'
  # @@protoc_insertion_point(class_scope:UTruck)
  })
_sym_db.RegisterMessage(UTruck)

UCommands = _reflection.GeneratedProtocolMessageType('UCommands', (_message.Message,), {
  'DESCRIPTOR' : _UCOMMANDS,
  '__module__' : 'world_ups_pb2'
  # @@protoc_insertion_point(class_scope:UCommands)
  })
_sym_db.RegisterMessage(UCommands)

UResponses = _reflection.GeneratedProtocolMessageType('UResponses', (_message.Message,), {
  'DESCRIPTOR' : _URESPONSES,
  '__module__' : 'world_ups_pb2'
  # @@protoc_insertion_point(class_scope:UResponses)
  })
_sym_db.RegisterMessage(UResponses)


# @@protoc_insertion_point(module_scope)
