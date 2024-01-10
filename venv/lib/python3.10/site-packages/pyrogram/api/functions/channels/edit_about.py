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


class EditAbout(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0x13e27f1e``

    Args:
        channel: :class:`pyrogram.api.types.InputChannel`
        about: :obj:`string`

    Returns:
        :obj:`bool`

    Raises:
        :class:`pyrogram.Error`
    """
    ID = 0x13e27f1e

    def __init__(self, channel, about):
        self.channel = channel  # InputChannel
        self.about = about  # string

    @staticmethod
    def read(b: BytesIO, *args) -> "EditAbout":
        # No flags
        
        channel = Object.read(b)
        
        about = String.read(b)
        
        return EditAbout(channel, about)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.channel.write())
        
        b.write(String(self.about))
        
        return b.getvalue()
