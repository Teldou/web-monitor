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


class GetMessagesViews(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0xc4c8a55d``

    Args:
        peer: :class:`pyrogram.api.types.InputPeer`
        id: List of :obj:`int`
        increment: :obj:`bool`

    Returns:
        List of :obj:`int`

    Raises:
        :class:`pyrogram.Error`
    """
    ID = 0xc4c8a55d

    def __init__(self, peer, id, increment):
        self.peer = peer  # InputPeer
        self.id = id  # Vector<int>
        self.increment = increment  # Bool

    @staticmethod
    def read(b: BytesIO, *args) -> "GetMessagesViews":
        # No flags
        
        peer = Object.read(b)
        
        id = Object.read(b, Int)
        
        increment = Bool.read(b)
        
        return GetMessagesViews(peer, id, increment)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Vector(self.id, Int))
        
        b.write(Bool(self.increment))
        
        return b.getvalue()
