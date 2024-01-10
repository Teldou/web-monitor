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


class UpdatePinnedMessage(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0xa72ded52``

    Args:
        channel: :class:`pyrogram.api.types.InputChannel`
        id: :obj:`int`
        silent: :obj:`bool` (optional)

    Returns:
        :class:`pyrogram.api.types.UpdatesTooLong` | :class:`pyrogram.api.types.UpdateShortMessage` | :class:`pyrogram.api.types.UpdateShortChatMessage` | :class:`pyrogram.api.types.UpdateShort` | :class:`pyrogram.api.types.UpdatesCombined` | :class:`pyrogram.api.types.Update` | :class:`pyrogram.api.types.UpdateShortSentMessage`

    Raises:
        :class:`pyrogram.Error`
    """
    ID = 0xa72ded52

    def __init__(self, channel, id, silent=None):
        self.silent = silent  # flags.0?true
        self.channel = channel  # InputChannel
        self.id = id  # int

    @staticmethod
    def read(b: BytesIO, *args) -> "UpdatePinnedMessage":
        flags = Int.read(b)
        
        silent = True if flags & (1 << 0) else False
        channel = Object.read(b)
        
        id = Int.read(b)
        
        return UpdatePinnedMessage(channel, id, silent)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.silent is not None else 0
        b.write(Int(flags))
        
        b.write(self.channel.write())
        
        b.write(Int(self.id))
        
        return b.getvalue()
