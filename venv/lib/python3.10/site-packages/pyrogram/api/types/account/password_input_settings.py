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


class PasswordInputSettings(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0x86916deb``

    Args:
        new_salt: :obj:`bytes` (optional)
        new_password_hash: :obj:`bytes` (optional)
        hint: :obj:`string` (optional)
        email: :obj:`string` (optional)
    """
    ID = 0x86916deb

    def __init__(self, new_salt=None, new_password_hash=None, hint=None, email=None):
        self.new_salt = new_salt  # flags.0?bytes
        self.new_password_hash = new_password_hash  # flags.0?bytes
        self.hint = hint  # flags.0?string
        self.email = email  # flags.1?string

    @staticmethod
    def read(b: BytesIO, *args) -> "PasswordInputSettings":
        flags = Int.read(b)
        
        new_salt = Bytes.read(b) if flags & (1 << 0) else None
        new_password_hash = Bytes.read(b) if flags & (1 << 0) else None
        hint = String.read(b) if flags & (1 << 0) else None
        email = String.read(b) if flags & (1 << 1) else None
        return PasswordInputSettings(new_salt, new_password_hash, hint, email)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.new_salt is not None else 0
        flags |= (1 << 0) if self.new_password_hash is not None else 0
        flags |= (1 << 0) if self.hint is not None else 0
        flags |= (1 << 1) if self.email is not None else 0
        b.write(Int(flags))
        
        if self.new_salt is not None:
            b.write(Bytes(self.new_salt))
        
        if self.new_password_hash is not None:
            b.write(Bytes(self.new_password_hash))
        
        if self.hint is not None:
            b.write(String(self.hint))
        
        if self.email is not None:
            b.write(String(self.email))
        
        return b.getvalue()
