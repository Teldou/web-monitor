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


class CreateStickerSet(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0x9bd86e6a``

    Args:
        user_id: :class:`pyrogram.api.types.InputUser`
        title: :obj:`string`
        short_name: :obj:`string`
        stickers: List of :class:`pyrogram.api.types.InputStickerSetItem`
        masks: :obj:`bool` (optional)

    Returns:
        :class:`pyrogram.api.types.messages.StickerSet`

    Raises:
        :class:`pyrogram.Error`
    """
    ID = 0x9bd86e6a

    def __init__(self, user_id, title, short_name, stickers, masks=None):
        self.masks = masks  # flags.0?true
        self.user_id = user_id  # InputUser
        self.title = title  # string
        self.short_name = short_name  # string
        self.stickers = stickers  # Vector<InputStickerSetItem>

    @staticmethod
    def read(b: BytesIO, *args) -> "CreateStickerSet":
        flags = Int.read(b)
        
        masks = True if flags & (1 << 0) else False
        user_id = Object.read(b)
        
        title = String.read(b)
        
        short_name = String.read(b)
        
        stickers = Object.read(b)
        
        return CreateStickerSet(user_id, title, short_name, stickers, masks)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.masks is not None else 0
        b.write(Int(flags))
        
        b.write(self.user_id.write())
        
        b.write(String(self.title))
        
        b.write(String(self.short_name))
        
        b.write(Vector(self.stickers))
        
        return b.getvalue()
