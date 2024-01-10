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


class GetRecentLocations(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0xbbc45b09``

    Args:
        peer: :class:`pyrogram.api.types.InputPeer`
        limit: :obj:`int`
        hash: :obj:`int`

    Returns:
        :class:`pyrogram.api.types.messages.Messages` | :class:`pyrogram.api.types.messages.MessagesSlice` | :class:`pyrogram.api.types.messages.ChannelMessages` | :class:`pyrogram.api.types.messages.MessagesNotModified`

    Raises:
        :class:`pyrogram.Error`
    """
    ID = 0xbbc45b09

    def __init__(self, peer, limit, hash):
        self.peer = peer  # InputPeer
        self.limit = limit  # int
        self.hash = hash  # int

    @staticmethod
    def read(b: BytesIO, *args) -> "GetRecentLocations":
        # No flags
        
        peer = Object.read(b)
        
        limit = Int.read(b)
        
        hash = Int.read(b)
        
        return GetRecentLocations(peer, limit, hash)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Int(self.limit))
        
        b.write(Int(self.hash))
        
        return b.getvalue()
