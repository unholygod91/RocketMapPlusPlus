# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/enums/pokemon_go_plus_ids.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/enums/pokemon_go_plus_ids.proto',
  package='pogoprotos.enums',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n*pogoprotos/enums/pokemon_go_plus_ids.proto\x12\x10pogoprotos.enums*\xc4\x03\n\x10PokemonGoPlusIds\x12#\n\x1fUNDEFINED_POKEMON_GO_PLUS_EVENT\x10\x00\x12\x19\n\x15\x43\x41NNOT_CONNECT_TO_PGP\x10\x01\x12\x1a\n\x16REGISTERING_PGP_FAILED\x10\x02\x12\x15\n\x11REGISTERING_RETRY\x10\x03\x12\x16\n\x12\x43ONNECTION_SUCCESS\x10\x04\x12\x1c\n\x18PGP_DISCONNECTED_BY_USER\x10\x05\x12\x1f\n\x1bPGP_DISCONNECTED_BY_TIMEOUT\x10\x06\x12\x1d\n\x19PGP_DISCONNECTED_BY_ERROR\x10\x07\x12\x13\n\x0fPGP_LOW_BATTERY\x10\x08\x12\x18\n\x14\x42LUETOOTH_SENT_ERROR\x10\t\x12\x16\n\x12PGP_SEEN_BY_DEVICE\x10\n\x12\x12\n\x0ePOKEMON_CAUGHT\x10\x0b\x12\x16\n\x12POKEMON_NOT_CAUGHT\x10\x0c\x12 \n\x1cPOKEMON_NOT_CAUGHT_DUE_ERROR\x10\r\x12\x11\n\rPOKESTOP_SPUN\x10\x0e\x12\x1f\n\x1bPOKESTOP_NOT_SPUN_DUE_ERROR\x10\x0f\x62\x06proto3')
)

_POKEMONGOPLUSIDS = _descriptor.EnumDescriptor(
  name='PokemonGoPlusIds',
  full_name='pogoprotos.enums.PokemonGoPlusIds',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED_POKEMON_GO_PLUS_EVENT', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_CONNECT_TO_PGP', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REGISTERING_PGP_FAILED', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REGISTERING_RETRY', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONNECTION_SUCCESS', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PGP_DISCONNECTED_BY_USER', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PGP_DISCONNECTED_BY_TIMEOUT', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PGP_DISCONNECTED_BY_ERROR', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PGP_LOW_BATTERY', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLUETOOTH_SENT_ERROR', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PGP_SEEN_BY_DEVICE', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POKEMON_CAUGHT', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POKEMON_NOT_CAUGHT', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POKEMON_NOT_CAUGHT_DUE_ERROR', index=13, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POKESTOP_SPUN', index=14, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POKESTOP_NOT_SPUN_DUE_ERROR', index=15, number=15,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=65,
  serialized_end=517,
)
_sym_db.RegisterEnumDescriptor(_POKEMONGOPLUSIDS)

PokemonGoPlusIds = enum_type_wrapper.EnumTypeWrapper(_POKEMONGOPLUSIDS)
UNDEFINED_POKEMON_GO_PLUS_EVENT = 0
CANNOT_CONNECT_TO_PGP = 1
REGISTERING_PGP_FAILED = 2
REGISTERING_RETRY = 3
CONNECTION_SUCCESS = 4
PGP_DISCONNECTED_BY_USER = 5
PGP_DISCONNECTED_BY_TIMEOUT = 6
PGP_DISCONNECTED_BY_ERROR = 7
PGP_LOW_BATTERY = 8
BLUETOOTH_SENT_ERROR = 9
PGP_SEEN_BY_DEVICE = 10
POKEMON_CAUGHT = 11
POKEMON_NOT_CAUGHT = 12
POKEMON_NOT_CAUGHT_DUE_ERROR = 13
POKESTOP_SPUN = 14
POKESTOP_NOT_SPUN_DUE_ERROR = 15


DESCRIPTOR.enum_types_by_name['PokemonGoPlusIds'] = _POKEMONGOPLUSIDS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
