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


class GetMessageEditData(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0xfda68d36``

    Args:
        peer: :class:`pyrogram.api.types.InputPeer`
        id: :obj:`int`

    Returns:
        :class:`pyrogram.api.types.messages.MessageEditData`

    Raises:
        :class:`pyrogram.Error`
    """
    ID = 0xfda68d36

    def __init__(self, peer, id):
        self.peer = peer  # InputPeer
        self.id = id  # int

    @staticmethod
    def read(b: BytesIO, *args) -> "GetMessageEditData":
        # No flags
        
        peer = Object.read(b)
        
        id = Int.read(b)
        
        return GetMessageEditData(peer, id)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Int(self.id))
        
        return b.getvalue()
