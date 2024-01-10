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


class BadServerSalt(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0xedab447b``

    Args:
        bad_msg_id: :obj:`int`
        bad_msg_seqno: :obj:`int`
        error_code: :obj:`int`
        new_server_salt: :obj:`int`
    """
    ID = 0xedab447b

    def __init__(self, bad_msg_id, bad_msg_seqno, error_code, new_server_salt):
        self.bad_msg_id = bad_msg_id  # long
        self.bad_msg_seqno = bad_msg_seqno  # int
        self.error_code = error_code  # int
        self.new_server_salt = new_server_salt  # long

    @staticmethod
    def read(b: BytesIO, *args) -> "BadServerSalt":
        # No flags
        
        bad_msg_id = Long.read(b)
        
        bad_msg_seqno = Int.read(b)
        
        error_code = Int.read(b)
        
        new_server_salt = Long.read(b)
        
        return BadServerSalt(bad_msg_id, bad_msg_seqno, error_code, new_server_salt)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.bad_msg_id))
        
        b.write(Int(self.bad_msg_seqno))
        
        b.write(Int(self.error_code))
        
        b.write(Long(self.new_server_salt))
        
        return b.getvalue()
