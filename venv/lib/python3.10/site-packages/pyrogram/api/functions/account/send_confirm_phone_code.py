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


class SendConfirmPhoneCode(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0x1516d7bd``

    Args:
        hash: :obj:`string`
        allow_flashcall: :obj:`bool` (optional)
        current_number: :obj:`bool` (optional)

    Returns:
        :class:`pyrogram.api.types.auth.SentCode`

    Raises:
        :class:`pyrogram.Error`
    """
    ID = 0x1516d7bd

    def __init__(self, hash, allow_flashcall=None, current_number=None):
        self.allow_flashcall = allow_flashcall  # flags.0?true
        self.hash = hash  # string
        self.current_number = current_number  # flags.0?Bool

    @staticmethod
    def read(b: BytesIO, *args) -> "SendConfirmPhoneCode":
        flags = Int.read(b)
        
        allow_flashcall = True if flags & (1 << 0) else False
        hash = String.read(b)
        
        current_number = Bool.read(b) if flags & (1 << 0) else None
        return SendConfirmPhoneCode(hash, allow_flashcall, current_number)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.allow_flashcall is not None else 0
        flags |= (1 << 0) if self.current_number is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.hash))
        
        if self.current_number is not None:
            b.write(Bool(self.current_number))
        
        return b.getvalue()
