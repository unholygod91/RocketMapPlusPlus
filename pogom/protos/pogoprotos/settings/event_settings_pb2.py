# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/event_settings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/event_settings.proto',
  package='pogoprotos.settings',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n(pogoprotos/settings/event_settings.proto\x12\x13pogoprotos.settings\"2\n\rEventSettings\x12!\n\x19\x63ondolence_ribbon_country\x18\x01 \x03(\tb\x06proto3')
)




_EVENTSETTINGS = _descriptor.Descriptor(
  name='EventSettings',
  full_name='pogoprotos.settings.EventSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='condolence_ribbon_country', full_name='pogoprotos.settings.EventSettings.condolence_ribbon_country', index=0,
      number=1, type=9, cpp_type=9, label=3,
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
  serialized_start=65,
  serialized_end=115,
)

DESCRIPTOR.message_types_by_name['EventSettings'] = _EVENTSETTINGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EventSettings = _reflection.GeneratedProtocolMessageType('EventSettings', (_message.Message,), dict(
  DESCRIPTOR = _EVENTSETTINGS,
  __module__ = 'pogoprotos.settings.event_settings_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.EventSettings)
  ))
_sym_db.RegisterMessage(EventSettings)


# @@protoc_insertion_point(module_scope)
