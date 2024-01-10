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


class GetChannelDifference(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0x03173d78``

    Args:
        channel: :class:`pyrogram.api.types.InputChannel`
        filter: :class:`pyrogram.api.types.ChannelMessagesFilter`
        pts: :obj:`int`
        limit: :obj:`int`
        force: :obj:`bool` (optional)

    Returns:
        :class:`pyrogram.api.types.updates.ChannelDifferenceEmpty` | :class:`pyrogram.api.types.updates.ChannelDifferenceTooLong` | :class:`pyrogram.api.types.updates.ChannelDifference`

    Raises:
        :class:`pyrogram.Error`
    """
    ID = 0x03173d78

    def __init__(self, channel, filter, pts, limit, force=None):
        self.force = force  # flags.0?true
        self.channel = channel  # InputChannel
        self.filter = filter  # ChannelMessagesFilter
        self.pts = pts  # int
        self.limit = limit  # int

    @staticmethod
    def read(b: BytesIO, *args) -> "GetChannelDifference":
        flags = Int.read(b)
        
        force = True if flags & (1 << 0) else False
        channel = Object.read(b)
        
        filter = Object.read(b)
        
        pts = Int.read(b)
        
        limit = Int.read(b)
        
        return GetChannelDifference(channel, filter, pts, limit, force)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.force is not None else 0
        b.write(Int(flags))
        
        b.write(self.channel.write())
        
        b.write(self.filter.write())
        
        b.write(Int(self.pts))
        
        b.write(Int(self.limit))
        
        return b.getvalue()
