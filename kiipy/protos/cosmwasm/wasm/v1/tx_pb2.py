# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmwasm/wasm/v1/tx.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmwasm.wasm.v1 import types_pb2 as cosmwasm_dot_wasm_dot_v1_dot_types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x63osmwasm/wasm/v1/tx.proto\x12\x10\x63osmwasm.wasm.v1\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x14gogoproto/gogo.proto\x1a\x1c\x63osmwasm/wasm/v1/types.proto\"\x94\x01\n\x0cMsgStoreCode\x12\x0e\n\x06sender\x18\x01 \x01(\t\x12(\n\x0ewasm_byte_code\x18\x02 \x01(\x0c\x42\x10\xe2\xde\x1f\x0cWASMByteCode\x12>\n\x16instantiate_permission\x18\x05 \x01(\x0b\x32\x1e.cosmwasm.wasm.v1.AccessConfigJ\x04\x08\x03\x10\x04J\x04\x08\x04\x10\x05\"3\n\x14MsgStoreCodeResponse\x12\x1b\n\x07\x63ode_id\x18\x01 \x01(\x04\x42\n\xe2\xde\x1f\x06\x43odeID\"\xe4\x01\n\x16MsgInstantiateContract\x12\x0e\n\x06sender\x18\x01 \x01(\t\x12\r\n\x05\x61\x64min\x18\x02 \x01(\t\x12\x1b\n\x07\x63ode_id\x18\x03 \x01(\x04\x42\n\xe2\xde\x1f\x06\x43odeID\x12\r\n\x05label\x18\x04 \x01(\t\x12#\n\x03msg\x18\x05 \x01(\x0c\x42\x16\xfa\xde\x1f\x12RawContractMessage\x12Z\n\x05\x66unds\x18\x06 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\"?\n\x1eMsgInstantiateContractResponse\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"\xb7\x01\n\x12MsgExecuteContract\x12\x0e\n\x06sender\x18\x01 \x01(\t\x12\x10\n\x08\x63ontract\x18\x02 \x01(\t\x12#\n\x03msg\x18\x03 \x01(\x0c\x42\x16\xfa\xde\x1f\x12RawContractMessage\x12Z\n\x05\x66unds\x18\x05 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\"*\n\x1aMsgExecuteContractResponse\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\"x\n\x12MsgMigrateContract\x12\x0e\n\x06sender\x18\x01 \x01(\t\x12\x10\n\x08\x63ontract\x18\x02 \x01(\t\x12\x1b\n\x07\x63ode_id\x18\x03 \x01(\x04\x42\n\xe2\xde\x1f\x06\x43odeID\x12#\n\x03msg\x18\x04 \x01(\x0c\x42\x16\xfa\xde\x1f\x12RawContractMessage\"*\n\x1aMsgMigrateContractResponse\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\"E\n\x0eMsgUpdateAdmin\x12\x0e\n\x06sender\x18\x01 \x01(\t\x12\x11\n\tnew_admin\x18\x02 \x01(\t\x12\x10\n\x08\x63ontract\x18\x03 \x01(\t\"\x18\n\x16MsgUpdateAdminResponse\"1\n\rMsgClearAdmin\x12\x0e\n\x06sender\x18\x01 \x01(\t\x12\x10\n\x08\x63ontract\x18\x03 \x01(\t\"\x17\n\x15MsgClearAdminResponse2\xce\x04\n\x03Msg\x12S\n\tStoreCode\x12\x1e.cosmwasm.wasm.v1.MsgStoreCode\x1a&.cosmwasm.wasm.v1.MsgStoreCodeResponse\x12q\n\x13InstantiateContract\x12(.cosmwasm.wasm.v1.MsgInstantiateContract\x1a\x30.cosmwasm.wasm.v1.MsgInstantiateContractResponse\x12\x65\n\x0f\x45xecuteContract\x12$.cosmwasm.wasm.v1.MsgExecuteContract\x1a,.cosmwasm.wasm.v1.MsgExecuteContractResponse\x12\x65\n\x0fMigrateContract\x12$.cosmwasm.wasm.v1.MsgMigrateContract\x1a,.cosmwasm.wasm.v1.MsgMigrateContractResponse\x12Y\n\x0bUpdateAdmin\x12 .cosmwasm.wasm.v1.MsgUpdateAdmin\x1a(.cosmwasm.wasm.v1.MsgUpdateAdminResponse\x12V\n\nClearAdmin\x12\x1f.cosmwasm.wasm.v1.MsgClearAdmin\x1a\'.cosmwasm.wasm.v1.MsgClearAdminResponseB,Z&github.com/CosmWasm/wasmd/x/wasm/types\xc8\xe1\x1e\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmwasm.wasm.v1.tx_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z&github.com/CosmWasm/wasmd/x/wasm/types\310\341\036\000'
  _MSGSTORECODE.fields_by_name['wasm_byte_code']._options = None
  _MSGSTORECODE.fields_by_name['wasm_byte_code']._serialized_options = b'\342\336\037\014WASMByteCode'
  _MSGSTORECODERESPONSE.fields_by_name['code_id']._options = None
  _MSGSTORECODERESPONSE.fields_by_name['code_id']._serialized_options = b'\342\336\037\006CodeID'
  _MSGINSTANTIATECONTRACT.fields_by_name['code_id']._options = None
  _MSGINSTANTIATECONTRACT.fields_by_name['code_id']._serialized_options = b'\342\336\037\006CodeID'
  _MSGINSTANTIATECONTRACT.fields_by_name['msg']._options = None
  _MSGINSTANTIATECONTRACT.fields_by_name['msg']._serialized_options = b'\372\336\037\022RawContractMessage'
  _MSGINSTANTIATECONTRACT.fields_by_name['funds']._options = None
  _MSGINSTANTIATECONTRACT.fields_by_name['funds']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'
  _MSGEXECUTECONTRACT.fields_by_name['msg']._options = None
  _MSGEXECUTECONTRACT.fields_by_name['msg']._serialized_options = b'\372\336\037\022RawContractMessage'
  _MSGEXECUTECONTRACT.fields_by_name['funds']._options = None
  _MSGEXECUTECONTRACT.fields_by_name['funds']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'
  _MSGMIGRATECONTRACT.fields_by_name['code_id']._options = None
  _MSGMIGRATECONTRACT.fields_by_name['code_id']._serialized_options = b'\342\336\037\006CodeID'
  _MSGMIGRATECONTRACT.fields_by_name['msg']._options = None
  _MSGMIGRATECONTRACT.fields_by_name['msg']._serialized_options = b'\372\336\037\022RawContractMessage'
  _globals['_MSGSTORECODE']._serialized_start=132
  _globals['_MSGSTORECODE']._serialized_end=280
  _globals['_MSGSTORECODERESPONSE']._serialized_start=282
  _globals['_MSGSTORECODERESPONSE']._serialized_end=333
  _globals['_MSGINSTANTIATECONTRACT']._serialized_start=336
  _globals['_MSGINSTANTIATECONTRACT']._serialized_end=564
  _globals['_MSGINSTANTIATECONTRACTRESPONSE']._serialized_start=566
  _globals['_MSGINSTANTIATECONTRACTRESPONSE']._serialized_end=629
  _globals['_MSGEXECUTECONTRACT']._serialized_start=632
  _globals['_MSGEXECUTECONTRACT']._serialized_end=815
  _globals['_MSGEXECUTECONTRACTRESPONSE']._serialized_start=817
  _globals['_MSGEXECUTECONTRACTRESPONSE']._serialized_end=859
  _globals['_MSGMIGRATECONTRACT']._serialized_start=861
  _globals['_MSGMIGRATECONTRACT']._serialized_end=981
  _globals['_MSGMIGRATECONTRACTRESPONSE']._serialized_start=983
  _globals['_MSGMIGRATECONTRACTRESPONSE']._serialized_end=1025
  _globals['_MSGUPDATEADMIN']._serialized_start=1027
  _globals['_MSGUPDATEADMIN']._serialized_end=1096
  _globals['_MSGUPDATEADMINRESPONSE']._serialized_start=1098
  _globals['_MSGUPDATEADMINRESPONSE']._serialized_end=1122
  _globals['_MSGCLEARADMIN']._serialized_start=1124
  _globals['_MSGCLEARADMIN']._serialized_end=1173
  _globals['_MSGCLEARADMINRESPONSE']._serialized_start=1175
  _globals['_MSGCLEARADMINRESPONSE']._serialized_end=1198
  _globals['_MSG']._serialized_start=1201
  _globals['_MSG']._serialized_end=1791
# @@protoc_insertion_point(module_scope)
