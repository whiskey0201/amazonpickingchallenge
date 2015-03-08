"""autogenerated by genpy from uts_recogniser/RowBinObjects.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import uts_recogniser.msg

class RowBinObjects(genpy.Message):
  _md5sum = "c4e5af7e70f72f36c1d7e6a05a1ba9eb"
  _type = "uts_recogniser/RowBinObjects"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """BinObjects[] items_in_row
================================================================================
MSG: uts_recogniser/BinObjects
string bin_id

Object[] items_in_bin
================================================================================
MSG: uts_recogniser/Object
string name

geometry_msgs/Pose pose

int16[] convex_hull_x
int16[] convex_hull_y

float32 mean_quality

NameTypeValue[] properties

geometry_msgs/Pose[] pose_uncertainty_list

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of postion and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

================================================================================
MSG: uts_recogniser/NameTypeValue
string name
string type
string value

"""
  __slots__ = ['items_in_row']
  _slot_types = ['uts_recogniser/BinObjects[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       items_in_row

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(RowBinObjects, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.items_in_row is None:
        self.items_in_row = []
    else:
      self.items_in_row = []

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      length = len(self.items_in_row)
      buff.write(_struct_I.pack(length))
      for val1 in self.items_in_row:
        _x = val1.bin_id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        length = len(val1.items_in_bin)
        buff.write(_struct_I.pack(length))
        for val2 in val1.items_in_bin:
          _x = val2.name
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.pack('<I%ss'%length, length, _x))
          _v1 = val2.pose
          _v2 = _v1.position
          _x = _v2
          buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
          _v3 = _v1.orientation
          _x = _v3
          buff.write(_struct_4d.pack(_x.x, _x.y, _x.z, _x.w))
          length = len(val2.convex_hull_x)
          buff.write(_struct_I.pack(length))
          pattern = '<%sh'%length
          buff.write(struct.pack(pattern, *val2.convex_hull_x))
          length = len(val2.convex_hull_y)
          buff.write(_struct_I.pack(length))
          pattern = '<%sh'%length
          buff.write(struct.pack(pattern, *val2.convex_hull_y))
          buff.write(_struct_f.pack(val2.mean_quality))
          length = len(val2.properties)
          buff.write(_struct_I.pack(length))
          for val3 in val2.properties:
            _x = val3.name
            length = len(_x)
            if python3 or type(_x) == unicode:
              _x = _x.encode('utf-8')
              length = len(_x)
            buff.write(struct.pack('<I%ss'%length, length, _x))
            _x = val3.type
            length = len(_x)
            if python3 or type(_x) == unicode:
              _x = _x.encode('utf-8')
              length = len(_x)
            buff.write(struct.pack('<I%ss'%length, length, _x))
            _x = val3.value
            length = len(_x)
            if python3 or type(_x) == unicode:
              _x = _x.encode('utf-8')
              length = len(_x)
            buff.write(struct.pack('<I%ss'%length, length, _x))
          length = len(val2.pose_uncertainty_list)
          buff.write(_struct_I.pack(length))
          for val3 in val2.pose_uncertainty_list:
            _v4 = val3.position
            _x = _v4
            buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
            _v5 = val3.orientation
            _x = _v5
            buff.write(_struct_4d.pack(_x.x, _x.y, _x.z, _x.w))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.items_in_row is None:
        self.items_in_row = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.items_in_row = []
      for i in range(0, length):
        val1 = uts_recogniser.msg.BinObjects()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.bin_id = str[start:end].decode('utf-8')
        else:
          val1.bin_id = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.items_in_bin = []
        for i in range(0, length):
          val2 = uts_recogniser.msg.Object()
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.name = str[start:end].decode('utf-8')
          else:
            val2.name = str[start:end]
          _v6 = val2.pose
          _v7 = _v6.position
          _x = _v7
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
          _v8 = _v6.orientation
          _x = _v8
          start = end
          end += 32
          (_x.x, _x.y, _x.z, _x.w,) = _struct_4d.unpack(str[start:end])
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          pattern = '<%sh'%length
          start = end
          end += struct.calcsize(pattern)
          val2.convex_hull_x = struct.unpack(pattern, str[start:end])
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          pattern = '<%sh'%length
          start = end
          end += struct.calcsize(pattern)
          val2.convex_hull_y = struct.unpack(pattern, str[start:end])
          start = end
          end += 4
          (val2.mean_quality,) = _struct_f.unpack(str[start:end])
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          val2.properties = []
          for i in range(0, length):
            val3 = uts_recogniser.msg.NameTypeValue()
            start = end
            end += 4
            (length,) = _struct_I.unpack(str[start:end])
            start = end
            end += length
            if python3:
              val3.name = str[start:end].decode('utf-8')
            else:
              val3.name = str[start:end]
            start = end
            end += 4
            (length,) = _struct_I.unpack(str[start:end])
            start = end
            end += length
            if python3:
              val3.type = str[start:end].decode('utf-8')
            else:
              val3.type = str[start:end]
            start = end
            end += 4
            (length,) = _struct_I.unpack(str[start:end])
            start = end
            end += length
            if python3:
              val3.value = str[start:end].decode('utf-8')
            else:
              val3.value = str[start:end]
            val2.properties.append(val3)
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          val2.pose_uncertainty_list = []
          for i in range(0, length):
            val3 = geometry_msgs.msg.Pose()
            _v9 = val3.position
            _x = _v9
            start = end
            end += 24
            (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
            _v10 = val3.orientation
            _x = _v10
            start = end
            end += 32
            (_x.x, _x.y, _x.z, _x.w,) = _struct_4d.unpack(str[start:end])
            val2.pose_uncertainty_list.append(val3)
          val1.items_in_bin.append(val2)
        self.items_in_row.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      length = len(self.items_in_row)
      buff.write(_struct_I.pack(length))
      for val1 in self.items_in_row:
        _x = val1.bin_id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        length = len(val1.items_in_bin)
        buff.write(_struct_I.pack(length))
        for val2 in val1.items_in_bin:
          _x = val2.name
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.pack('<I%ss'%length, length, _x))
          _v11 = val2.pose
          _v12 = _v11.position
          _x = _v12
          buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
          _v13 = _v11.orientation
          _x = _v13
          buff.write(_struct_4d.pack(_x.x, _x.y, _x.z, _x.w))
          length = len(val2.convex_hull_x)
          buff.write(_struct_I.pack(length))
          pattern = '<%sh'%length
          buff.write(val2.convex_hull_x.tostring())
          length = len(val2.convex_hull_y)
          buff.write(_struct_I.pack(length))
          pattern = '<%sh'%length
          buff.write(val2.convex_hull_y.tostring())
          buff.write(_struct_f.pack(val2.mean_quality))
          length = len(val2.properties)
          buff.write(_struct_I.pack(length))
          for val3 in val2.properties:
            _x = val3.name
            length = len(_x)
            if python3 or type(_x) == unicode:
              _x = _x.encode('utf-8')
              length = len(_x)
            buff.write(struct.pack('<I%ss'%length, length, _x))
            _x = val3.type
            length = len(_x)
            if python3 or type(_x) == unicode:
              _x = _x.encode('utf-8')
              length = len(_x)
            buff.write(struct.pack('<I%ss'%length, length, _x))
            _x = val3.value
            length = len(_x)
            if python3 or type(_x) == unicode:
              _x = _x.encode('utf-8')
              length = len(_x)
            buff.write(struct.pack('<I%ss'%length, length, _x))
          length = len(val2.pose_uncertainty_list)
          buff.write(_struct_I.pack(length))
          for val3 in val2.pose_uncertainty_list:
            _v14 = val3.position
            _x = _v14
            buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
            _v15 = val3.orientation
            _x = _v15
            buff.write(_struct_4d.pack(_x.x, _x.y, _x.z, _x.w))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.items_in_row is None:
        self.items_in_row = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.items_in_row = []
      for i in range(0, length):
        val1 = uts_recogniser.msg.BinObjects()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.bin_id = str[start:end].decode('utf-8')
        else:
          val1.bin_id = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.items_in_bin = []
        for i in range(0, length):
          val2 = uts_recogniser.msg.Object()
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.name = str[start:end].decode('utf-8')
          else:
            val2.name = str[start:end]
          _v16 = val2.pose
          _v17 = _v16.position
          _x = _v17
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
          _v18 = _v16.orientation
          _x = _v18
          start = end
          end += 32
          (_x.x, _x.y, _x.z, _x.w,) = _struct_4d.unpack(str[start:end])
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          pattern = '<%sh'%length
          start = end
          end += struct.calcsize(pattern)
          val2.convex_hull_x = numpy.frombuffer(str[start:end], dtype=numpy.int16, count=length)
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          pattern = '<%sh'%length
          start = end
          end += struct.calcsize(pattern)
          val2.convex_hull_y = numpy.frombuffer(str[start:end], dtype=numpy.int16, count=length)
          start = end
          end += 4
          (val2.mean_quality,) = _struct_f.unpack(str[start:end])
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          val2.properties = []
          for i in range(0, length):
            val3 = uts_recogniser.msg.NameTypeValue()
            start = end
            end += 4
            (length,) = _struct_I.unpack(str[start:end])
            start = end
            end += length
            if python3:
              val3.name = str[start:end].decode('utf-8')
            else:
              val3.name = str[start:end]
            start = end
            end += 4
            (length,) = _struct_I.unpack(str[start:end])
            start = end
            end += length
            if python3:
              val3.type = str[start:end].decode('utf-8')
            else:
              val3.type = str[start:end]
            start = end
            end += 4
            (length,) = _struct_I.unpack(str[start:end])
            start = end
            end += length
            if python3:
              val3.value = str[start:end].decode('utf-8')
            else:
              val3.value = str[start:end]
            val2.properties.append(val3)
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          val2.pose_uncertainty_list = []
          for i in range(0, length):
            val3 = geometry_msgs.msg.Pose()
            _v19 = val3.position
            _x = _v19
            start = end
            end += 24
            (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
            _v20 = val3.orientation
            _x = _v20
            start = end
            end += 32
            (_x.x, _x.y, _x.z, _x.w,) = _struct_4d.unpack(str[start:end])
            val2.pose_uncertainty_list.append(val3)
          val1.items_in_bin.append(val2)
        self.items_in_row.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_4d = struct.Struct("<4d")
_struct_f = struct.Struct("<f")
_struct_3d = struct.Struct("<3d")
