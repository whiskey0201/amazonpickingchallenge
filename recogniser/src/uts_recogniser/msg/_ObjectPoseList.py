"""autogenerated by genpy from uts_recogniser/ObjectPoseList.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import uts_recogniser.msg
import genpy
import std_msgs.msg

class ObjectPoseList(genpy.Message):
  _md5sum = "8374d419f4435fc3eaa2652d85ff89d7"
  _type = "uts_recogniser/ObjectPoseList"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """Header header

ObjectPose[] object_list

time originalTimeStamp

time requestTimeStamp


================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.secs: seconds (stamp_secs) since epoch
# * stamp.nsecs: nanoseconds since stamp_secs
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: uts_recogniser/ObjectPose
string name

geometry_msgs/Pose pose

int16[] convex_hull_x
int16[] convex_hull_y

float32 mean_quality
int16 used_points

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
  __slots__ = ['header','object_list','originalTimeStamp','requestTimeStamp']
  _slot_types = ['std_msgs/Header','uts_recogniser/ObjectPose[]','time','time']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,object_list,originalTimeStamp,requestTimeStamp

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(ObjectPoseList, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.object_list is None:
        self.object_list = []
      if self.originalTimeStamp is None:
        self.originalTimeStamp = genpy.Time()
      if self.requestTimeStamp is None:
        self.requestTimeStamp = genpy.Time()
    else:
      self.header = std_msgs.msg.Header()
      self.object_list = []
      self.originalTimeStamp = genpy.Time()
      self.requestTimeStamp = genpy.Time()

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
      _x = self
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.object_list)
      buff.write(_struct_I.pack(length))
      for val1 in self.object_list:
        _x = val1.name
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _v1 = val1.pose
        _v2 = _v1.position
        _x = _v2
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
        _v3 = _v1.orientation
        _x = _v3
        buff.write(_struct_4d.pack(_x.x, _x.y, _x.z, _x.w))
        length = len(val1.convex_hull_x)
        buff.write(_struct_I.pack(length))
        pattern = '<%sh'%length
        buff.write(struct.pack(pattern, *val1.convex_hull_x))
        length = len(val1.convex_hull_y)
        buff.write(_struct_I.pack(length))
        pattern = '<%sh'%length
        buff.write(struct.pack(pattern, *val1.convex_hull_y))
        _x = val1
        buff.write(_struct_fh.pack(_x.mean_quality, _x.used_points))
        length = len(val1.properties)
        buff.write(_struct_I.pack(length))
        for val2 in val1.properties:
          _x = val2.name
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.pack('<I%ss'%length, length, _x))
          _x = val2.type
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.pack('<I%ss'%length, length, _x))
          _x = val2.value
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.pack('<I%ss'%length, length, _x))
        length = len(val1.pose_uncertainty_list)
        buff.write(_struct_I.pack(length))
        for val2 in val1.pose_uncertainty_list:
          _v4 = val2.position
          _x = _v4
          buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
          _v5 = val2.orientation
          _x = _v5
          buff.write(_struct_4d.pack(_x.x, _x.y, _x.z, _x.w))
      _x = self
      buff.write(_struct_4I.pack(_x.originalTimeStamp.secs, _x.originalTimeStamp.nsecs, _x.requestTimeStamp.secs, _x.requestTimeStamp.nsecs))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.object_list is None:
        self.object_list = None
      if self.originalTimeStamp is None:
        self.originalTimeStamp = genpy.Time()
      if self.requestTimeStamp is None:
        self.requestTimeStamp = genpy.Time()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.object_list = []
      for i in range(0, length):
        val1 = uts_recogniser.msg.ObjectPose()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.name = str[start:end].decode('utf-8')
        else:
          val1.name = str[start:end]
        _v6 = val1.pose
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
        val1.convex_hull_x = struct.unpack(pattern, str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sh'%length
        start = end
        end += struct.calcsize(pattern)
        val1.convex_hull_y = struct.unpack(pattern, str[start:end])
        _x = val1
        start = end
        end += 6
        (_x.mean_quality, _x.used_points,) = _struct_fh.unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.properties = []
        for i in range(0, length):
          val2 = uts_recogniser.msg.NameTypeValue()
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.name = str[start:end].decode('utf-8')
          else:
            val2.name = str[start:end]
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.type = str[start:end].decode('utf-8')
          else:
            val2.type = str[start:end]
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.value = str[start:end].decode('utf-8')
          else:
            val2.value = str[start:end]
          val1.properties.append(val2)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.pose_uncertainty_list = []
        for i in range(0, length):
          val2 = geometry_msgs.msg.Pose()
          _v9 = val2.position
          _x = _v9
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
          _v10 = val2.orientation
          _x = _v10
          start = end
          end += 32
          (_x.x, _x.y, _x.z, _x.w,) = _struct_4d.unpack(str[start:end])
          val1.pose_uncertainty_list.append(val2)
        self.object_list.append(val1)
      _x = self
      start = end
      end += 16
      (_x.originalTimeStamp.secs, _x.originalTimeStamp.nsecs, _x.requestTimeStamp.secs, _x.requestTimeStamp.nsecs,) = _struct_4I.unpack(str[start:end])
      self.originalTimeStamp.canon()
      self.requestTimeStamp.canon()
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
      _x = self
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.object_list)
      buff.write(_struct_I.pack(length))
      for val1 in self.object_list:
        _x = val1.name
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _v11 = val1.pose
        _v12 = _v11.position
        _x = _v12
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
        _v13 = _v11.orientation
        _x = _v13
        buff.write(_struct_4d.pack(_x.x, _x.y, _x.z, _x.w))
        length = len(val1.convex_hull_x)
        buff.write(_struct_I.pack(length))
        pattern = '<%sh'%length
        buff.write(val1.convex_hull_x.tostring())
        length = len(val1.convex_hull_y)
        buff.write(_struct_I.pack(length))
        pattern = '<%sh'%length
        buff.write(val1.convex_hull_y.tostring())
        _x = val1
        buff.write(_struct_fh.pack(_x.mean_quality, _x.used_points))
        length = len(val1.properties)
        buff.write(_struct_I.pack(length))
        for val2 in val1.properties:
          _x = val2.name
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.pack('<I%ss'%length, length, _x))
          _x = val2.type
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.pack('<I%ss'%length, length, _x))
          _x = val2.value
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.pack('<I%ss'%length, length, _x))
        length = len(val1.pose_uncertainty_list)
        buff.write(_struct_I.pack(length))
        for val2 in val1.pose_uncertainty_list:
          _v14 = val2.position
          _x = _v14
          buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
          _v15 = val2.orientation
          _x = _v15
          buff.write(_struct_4d.pack(_x.x, _x.y, _x.z, _x.w))
      _x = self
      buff.write(_struct_4I.pack(_x.originalTimeStamp.secs, _x.originalTimeStamp.nsecs, _x.requestTimeStamp.secs, _x.requestTimeStamp.nsecs))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.object_list is None:
        self.object_list = None
      if self.originalTimeStamp is None:
        self.originalTimeStamp = genpy.Time()
      if self.requestTimeStamp is None:
        self.requestTimeStamp = genpy.Time()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.object_list = []
      for i in range(0, length):
        val1 = uts_recogniser.msg.ObjectPose()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.name = str[start:end].decode('utf-8')
        else:
          val1.name = str[start:end]
        _v16 = val1.pose
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
        val1.convex_hull_x = numpy.frombuffer(str[start:end], dtype=numpy.int16, count=length)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sh'%length
        start = end
        end += struct.calcsize(pattern)
        val1.convex_hull_y = numpy.frombuffer(str[start:end], dtype=numpy.int16, count=length)
        _x = val1
        start = end
        end += 6
        (_x.mean_quality, _x.used_points,) = _struct_fh.unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.properties = []
        for i in range(0, length):
          val2 = uts_recogniser.msg.NameTypeValue()
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.name = str[start:end].decode('utf-8')
          else:
            val2.name = str[start:end]
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.type = str[start:end].decode('utf-8')
          else:
            val2.type = str[start:end]
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.value = str[start:end].decode('utf-8')
          else:
            val2.value = str[start:end]
          val1.properties.append(val2)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.pose_uncertainty_list = []
        for i in range(0, length):
          val2 = geometry_msgs.msg.Pose()
          _v19 = val2.position
          _x = _v19
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
          _v20 = val2.orientation
          _x = _v20
          start = end
          end += 32
          (_x.x, _x.y, _x.z, _x.w,) = _struct_4d.unpack(str[start:end])
          val1.pose_uncertainty_list.append(val2)
        self.object_list.append(val1)
      _x = self
      start = end
      end += 16
      (_x.originalTimeStamp.secs, _x.originalTimeStamp.nsecs, _x.requestTimeStamp.secs, _x.requestTimeStamp.nsecs,) = _struct_4I.unpack(str[start:end])
      self.originalTimeStamp.canon()
      self.requestTimeStamp.canon()
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_fh = struct.Struct("<fh")
_struct_3I = struct.Struct("<3I")
_struct_4I = struct.Struct("<4I")
_struct_4d = struct.Struct("<4d")
_struct_3d = struct.Struct("<3d")
