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


class PeerNotifySettings(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0x9acda4c0``

    Args:
        mute_until: :obj:`int`
        sound: :obj:`string`
        show_previews: :obj:`bool` (optional)
        silent: :obj:`bool` (optional)
    """
    ID = 0x9acda4c0

    def __init__(self, mute_until, sound, show_previews=None, silent=None):
        self.show_previews = show_previews  # flags.0?true
        self.silent = silent  # flags.1?true
        self.mute_until = mute_until  # int
        self.sound = sound  # string

    @staticmethod
    def read(b: BytesIO, *args) -> "PeerNotifySettings":
        flags = Int.read(b)
        
        show_previews = True if flags & (1 << 0) else False
        silent = True if flags & (1 << 1) else False
        mute_until = Int.read(b)
        
        sound = String.read(b)
        
        return PeerNotifySettings(mute_until, sound, show_previews, silent)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.show_previews is not None else 0
        flags |= (1 << 1) if self.silent is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.mute_until))
        
        b.write(String(self.sound))
        
        return b.getvalue()
