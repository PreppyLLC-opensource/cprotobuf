# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='test.proto',
  package='test',
  serialized_pb='\n\ntest.proto\x12\x04test\"\x1f\n\x07SubTest\x12\t\n\x01\x61\x18\x01 \x01(\x05\x12\t\n\x01\x62\x18\x02 \x01(\x11\":\n\x0cRecursiveFoo\x12\x1f\n\x03\x62\x61r\x18\x01 \x01(\x0b\x32\x12.test.RecursiveBar\x12\t\n\x01n\x18\x02 \x01(\x05\"/\n\x0cRecursiveBar\x12\x1f\n\x03\x66oo\x18\x01 \x02(\x0b\x32\x12.test.RecursiveFoo\"1\n\x07SelfRef\x12\x1b\n\x04self\x18\x01 \x01(\x0b\x32\r.test.SelfRef\x12\t\n\x01n\x18\x02 \x01(\x05\"\xc7\x02\n\x04Test\x12\t\n\x01\x61\x18\x01 \x01(\x05\x12\t\n\x01\x62\x18\x02 \x01(\x03\x12\t\n\x01\x63\x18\x03 \x01(\x11\x12\t\n\x01\x64\x18\x04 \x01(\x12\x12\t\n\x01\x65\x18\x05 \x01(\x07\x12\t\n\x01\x66\x18\x06 \x01(\x06\x12\t\n\x01g\x18\x07 \x01(\x0f\x12\t\n\x01h\x18\x08 \x01(\x10\x12\t\n\x01i\x18\t \x01(\x02\x12\t\n\x01j\x18\n \x01(\x01\x12\t\n\x01k\x18\x0b \x01(\r\x12\t\n\x01l\x18\x0c \x01(\x04\x12\t\n\x01m\x18\r \x01(\t\x12\t\n\x01n\x18\x0e \x01(\x08\x12\x18\n\x01o\x18\x0f \x01(\x0b\x32\r.test.SubTest\x12\t\n\x01p\x18\x10 \x03(\x05\x12\r\n\x01q\x18\x11 \x03(\x05\x42\x02\x10\x01\x12\x18\n\x01r\x18\x12 \x03(\x0b\x32\r.test.SubTest\x12\x19\n\x01s\x18\x13 \x01(\x0e\x32\x0e.test.TestType\x12\x1f\n\x03\x66oo\x18\x14 \x01(\x0b\x32\x12.test.RecursiveFoo\x12\x1b\n\x04self\x18\x15 \x01(\x0b\x32\r.test.SelfRef*4\n\x08TestType\x12\x12\n\x05TYPE1\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\t\n\x05TYPE2\x10\x02\x12\t\n\x05TYPE3\x10\x03')

_TESTTYPE = descriptor.EnumDescriptor(
  name='TestType',
  full_name='test.TestType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='TYPE1', index=0, number=-1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='TYPE2', index=1, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='TYPE3', index=2, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=543,
  serialized_end=595,
)


TYPE1 = -1
TYPE2 = 2
TYPE3 = 3



_SUBTEST = descriptor.Descriptor(
  name='SubTest',
  full_name='test.SubTest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='a', full_name='test.SubTest.a', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='b', full_name='test.SubTest.b', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=20,
  serialized_end=51,
)


_RECURSIVEFOO = descriptor.Descriptor(
  name='RecursiveFoo',
  full_name='test.RecursiveFoo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='bar', full_name='test.RecursiveFoo.bar', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='n', full_name='test.RecursiveFoo.n', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=53,
  serialized_end=111,
)


_RECURSIVEBAR = descriptor.Descriptor(
  name='RecursiveBar',
  full_name='test.RecursiveBar',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='foo', full_name='test.RecursiveBar.foo', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
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
  serialized_start=113,
  serialized_end=160,
)


_SELFREF = descriptor.Descriptor(
  name='SelfRef',
  full_name='test.SelfRef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='self', full_name='test.SelfRef.self', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='n', full_name='test.SelfRef.n', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=162,
  serialized_end=211,
)


_TEST = descriptor.Descriptor(
  name='Test',
  full_name='test.Test',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='a', full_name='test.Test.a', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='b', full_name='test.Test.b', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='c', full_name='test.Test.c', index=2,
      number=3, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='d', full_name='test.Test.d', index=3,
      number=4, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='e', full_name='test.Test.e', index=4,
      number=5, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='f', full_name='test.Test.f', index=5,
      number=6, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='g', full_name='test.Test.g', index=6,
      number=7, type=15, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='h', full_name='test.Test.h', index=7,
      number=8, type=16, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='i', full_name='test.Test.i', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='j', full_name='test.Test.j', index=9,
      number=10, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='k', full_name='test.Test.k', index=10,
      number=11, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='l', full_name='test.Test.l', index=11,
      number=12, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='m', full_name='test.Test.m', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='n', full_name='test.Test.n', index=13,
      number=14, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='o', full_name='test.Test.o', index=14,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='p', full_name='test.Test.p', index=15,
      number=16, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='q', full_name='test.Test.q', index=16,
      number=17, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')),
    descriptor.FieldDescriptor(
      name='r', full_name='test.Test.r', index=17,
      number=18, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='s', full_name='test.Test.s', index=18,
      number=19, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='foo', full_name='test.Test.foo', index=19,
      number=20, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='self', full_name='test.Test.self', index=20,
      number=21, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=214,
  serialized_end=541,
)

_RECURSIVEFOO.fields_by_name['bar'].message_type = _RECURSIVEBAR
_RECURSIVEBAR.fields_by_name['foo'].message_type = _RECURSIVEFOO
_SELFREF.fields_by_name['self'].message_type = _SELFREF
_TEST.fields_by_name['o'].message_type = _SUBTEST
_TEST.fields_by_name['r'].message_type = _SUBTEST
_TEST.fields_by_name['s'].enum_type = _TESTTYPE
_TEST.fields_by_name['foo'].message_type = _RECURSIVEFOO
_TEST.fields_by_name['self'].message_type = _SELFREF
DESCRIPTOR.message_types_by_name['SubTest'] = _SUBTEST
DESCRIPTOR.message_types_by_name['RecursiveFoo'] = _RECURSIVEFOO
DESCRIPTOR.message_types_by_name['RecursiveBar'] = _RECURSIVEBAR
DESCRIPTOR.message_types_by_name['SelfRef'] = _SELFREF
DESCRIPTOR.message_types_by_name['Test'] = _TEST

class SubTest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SUBTEST
  
  # @@protoc_insertion_point(class_scope:test.SubTest)

class RecursiveFoo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RECURSIVEFOO
  
  # @@protoc_insertion_point(class_scope:test.RecursiveFoo)

class RecursiveBar(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RECURSIVEBAR
  
  # @@protoc_insertion_point(class_scope:test.RecursiveBar)

class SelfRef(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SELFREF
  
  # @@protoc_insertion_point(class_scope:test.SelfRef)

class Test(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TEST
  
  # @@protoc_insertion_point(class_scope:test.Test)

# @@protoc_insertion_point(module_scope)
