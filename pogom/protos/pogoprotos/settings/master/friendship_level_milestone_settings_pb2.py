# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/master/friendship_level_milestone_settings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import pokemon_trading_type_pb2 as pogoprotos_dot_enums_dot_pokemon__trading__type__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/master/friendship_level_milestone_settings.proto',
  package='pogoprotos.settings.master',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nDpogoprotos/settings/master/friendship_level_milestone_settings.proto\x12\x1apogoprotos.settings.master\x1a+pogoprotos/enums/pokemon_trading_type.proto\"\xf0\x01\n FriendshipLevelMilestoneSettings\x12\x1b\n\x13min_points_to_reach\x18\x01 \x01(\x05\x12\x1b\n\x13milestone_xp_reward\x18\x02 \x01(\x05\x12\x1f\n\x17\x61ttack_bonus_percentage\x18\x03 \x01(\x02\x12\x17\n\x0fraid_ball_bonus\x18\x04 \x01(\x05\x12>\n\x10unlocked_trading\x18\x05 \x03(\x0e\x32$.pogoprotos.enums.PokemonTradingType\x12\x18\n\x10trading_discount\x18\x06 \x01(\x02\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_pokemon__trading__type__pb2.DESCRIPTOR,])




_FRIENDSHIPLEVELMILESTONESETTINGS = _descriptor.Descriptor(
  name='FriendshipLevelMilestoneSettings',
  full_name='pogoprotos.settings.master.FriendshipLevelMilestoneSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='min_points_to_reach', full_name='pogoprotos.settings.master.FriendshipLevelMilestoneSettings.min_points_to_reach', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='milestone_xp_reward', full_name='pogoprotos.settings.master.FriendshipLevelMilestoneSettings.milestone_xp_reward', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attack_bonus_percentage', full_name='pogoprotos.settings.master.FriendshipLevelMilestoneSettings.attack_bonus_percentage', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='raid_ball_bonus', full_name='pogoprotos.settings.master.FriendshipLevelMilestoneSettings.raid_ball_bonus', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unlocked_trading', full_name='pogoprotos.settings.master.FriendshipLevelMilestoneSettings.unlocked_trading', index=4,
      number=5, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trading_discount', full_name='pogoprotos.settings.master.FriendshipLevelMilestoneSettings.trading_discount', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=146,
  serialized_end=386,
)

_FRIENDSHIPLEVELMILESTONESETTINGS.fields_by_name['unlocked_trading'].enum_type = pogoprotos_dot_enums_dot_pokemon__trading__type__pb2._POKEMONTRADINGTYPE
DESCRIPTOR.message_types_by_name['FriendshipLevelMilestoneSettings'] = _FRIENDSHIPLEVELMILESTONESETTINGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FriendshipLevelMilestoneSettings = _reflection.GeneratedProtocolMessageType('FriendshipLevelMilestoneSettings', (_message.Message,), dict(
  DESCRIPTOR = _FRIENDSHIPLEVELMILESTONESETTINGS,
  __module__ = 'pogoprotos.settings.master.friendship_level_milestone_settings_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.master.FriendshipLevelMilestoneSettings)
  ))
_sym_db.RegisterMessage(FriendshipLevelMilestoneSettings)


# @@protoc_insertion_point(module_scope)
