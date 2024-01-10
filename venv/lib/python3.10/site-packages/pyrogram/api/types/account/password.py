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


class Password(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0x7c18141c``

    Args:
        current_salt: :obj:`bytes`
        new_salt: :obj:`bytes`
        hint: :obj:`string`
        has_recovery: :obj:`bool`
        email_unconfirmed_pattern: :obj:`string`
    """
    ID = 0x7c18141c

    def __init__(self, current_salt, new_salt, hint, has_recovery, email_unconfirmed_pattern):
        self.current_salt = current_salt  # bytes
        self.new_salt = new_salt  # bytes
        self.hint = hint  # string
        self.has_recovery = has_recovery  # Bool
        self.email_unconfirmed_pattern = email_unconfirmed_pattern  # string

    @staticmethod
    def read(b: BytesIO, *args) -> "Password":
        # No flags
        
        current_salt = Bytes.read(b)
        
        new_salt = Bytes.read(b)
        
        hint = String.read(b)
        
        has_recovery = Bool.read(b)
        
        email_unconfirmed_pattern = String.read(b)
        
        return Password(current_salt, new_salt, hint, has_recovery, email_unconfirmed_pattern)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Bytes(self.current_salt))
        
        b.write(Bytes(self.new_salt))
        
        b.write(String(self.hint))
        
        b.write(Bool(self.has_recovery))
        
        b.write(String(self.email_unconfirmed_pattern))
        
        return b.getvalue()
