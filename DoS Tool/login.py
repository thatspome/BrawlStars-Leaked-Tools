import struct
from utils import Writer

class login:
   def header(self, data):
      w = Writer()
      header = b''
      header += w.writeShort(10101)
      header += len(data).to_bytes(3, 'big')
      header += w.writeShort(0)
      header += data
      return header

   def send_hello(self, version: int):
      w = Writer()
      message = b''
      message += w.writeInt(0) # HighID
      message += w.writeInt(0) # LowID
      message += w.writeStringLength("")
      message += w.writeString("") # Token
      message += w.writeInt(version) # Major
      message += w.writeInt(version) # Minor
      message += w.writeInt(165) # Build
      message += w.writeStringLength("")
      message += w.writeString("") # Fingerprint SHA
      message += w.writeString("") # Device Model
      message += w.writeVInt(2) # isAndroid
      message += w.writeVInt(0) # Unknown
      message += w.writeString("ar") # Device Language
      message += w.writeString("10") # OS Version
      message += w.writeInt(0)
      message += w.writeVInt(0)
      message += w.writeString("lol")
      message += w.writeVInt(0)
      message += w.writeInt(0)
      message += w.writeInt(0)
      message += w.writeString("")
      return self.header(message)
