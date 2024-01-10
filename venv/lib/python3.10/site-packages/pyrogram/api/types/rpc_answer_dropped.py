# Pyrogram - Telegram MTProto API Client Library for Python
# Copyright (C) 2017-2018 Dan Tès <https://github.com/delivrance>
#
# This file is part of Pyrogram.
#
# Pyrogram is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Pyrogram is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

from io import BytesIO

from pyrogram.api.core import *


class RpcAnswerDropped(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0xa43ad8b7``

    Args:
        msg_id: :obj:`int`
        seq_no: :obj:`int`
        bytes: :obj:`int`
    """
    ID = 0xa43ad8b7

    def __init__(self, msg_id, seq_no, bytes):
        self.msg_id = msg_id  # long
        self.seq_no = seq_no  # int
        self.bytes = bytes  # int

    @staticmethod
    def read(b: BytesIO, *args) -> "RpcAnswerDropped":
        # No flags
        
        msg_id = Long.read(b)
        
        seq_no = Int.read(b)
        
        bytes = Int.read(b)
        
        return RpcAnswerDropped(msg_id, seq_no, bytes)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.msg_id))
        
        b.write(Int(self.seq_no))
        
        b.write(Int(self.bytes))
        
        return b.getvalue()
