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


class InputBotInlineMessageText(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0x3dcd7a87``

    Args:
        message: :obj:`string`
        no_webpage: :obj:`bool` (optional)
        entities: List of :class:`pyrogram.api.types.MessageEntity` (optional)
        reply_markup: :class:`pyrogram.api.types.ReplyMarkup` (optional)
    """
    ID = 0x3dcd7a87

    def __init__(self, message, no_webpage=None, entities=None, reply_markup=None):
        self.no_webpage = no_webpage  # flags.0?true
        self.message = message  # string
        self.entities = entities  # flags.1?Vector<MessageEntity>
        self.reply_markup = reply_markup  # flags.2?ReplyMarkup

    @staticmethod
    def read(b: BytesIO, *args) -> "InputBotInlineMessageText":
        flags = Int.read(b)
        
        no_webpage = True if flags & (1 << 0) else False
        message = String.read(b)
        
        entities = Object.read(b) if flags & (1 << 1) else []
        
        reply_markup = Object.read(b) if flags & (1 << 2) else None
        
        return InputBotInlineMessageText(message, no_webpage, entities, reply_markup)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.no_webpage is not None else 0
        flags |= (1 << 1) if self.entities is not None else 0
        flags |= (1 << 2) if self.reply_markup is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.message))
        
        if self.entities is not None:
            b.write(Vector(self.entities))
        
        if self.reply_markup is not None:
            b.write(self.reply_markup.write())
        
        return b.getvalue()
