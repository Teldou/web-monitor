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


class EditMessage(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0x05d1b8dd``

    Args:
        peer: :class:`pyrogram.api.types.InputPeer`
        id: :obj:`int`
        no_webpage: :obj:`bool` (optional)
        stop_geo_live: :obj:`bool` (optional)
        message: :obj:`string` (optional)
        reply_markup: :class:`pyrogram.api.types.ReplyMarkup` (optional)
        entities: List of :class:`pyrogram.api.types.MessageEntity` (optional)
        geo_point: :class:`pyrogram.api.types.InputGeoPoint` (optional)

    Returns:
        :class:`pyrogram.api.types.UpdatesTooLong` | :class:`pyrogram.api.types.UpdateShortMessage` | :class:`pyrogram.api.types.UpdateShortChatMessage` | :class:`pyrogram.api.types.UpdateShort` | :class:`pyrogram.api.types.UpdatesCombined` | :class:`pyrogram.api.types.Update` | :class:`pyrogram.api.types.UpdateShortSentMessage`

    Raises:
        :class:`pyrogram.Error`
    """
    ID = 0x05d1b8dd

    def __init__(self, peer, id, no_webpage=None, stop_geo_live=None, message=None, reply_markup=None, entities=None, geo_point=None):
        self.no_webpage = no_webpage  # flags.1?true
        self.stop_geo_live = stop_geo_live  # flags.12?true
        self.peer = peer  # InputPeer
        self.id = id  # int
        self.message = message  # flags.11?string
        self.reply_markup = reply_markup  # flags.2?ReplyMarkup
        self.entities = entities  # flags.3?Vector<MessageEntity>
        self.geo_point = geo_point  # flags.13?InputGeoPoint

    @staticmethod
    def read(b: BytesIO, *args) -> "EditMessage":
        flags = Int.read(b)
        
        no_webpage = True if flags & (1 << 1) else False
        stop_geo_live = True if flags & (1 << 12) else False
        peer = Object.read(b)
        
        id = Int.read(b)
        
        message = String.read(b) if flags & (1 << 11) else None
        reply_markup = Object.read(b) if flags & (1 << 2) else None
        
        entities = Object.read(b) if flags & (1 << 3) else []
        
        geo_point = Object.read(b) if flags & (1 << 13) else None
        
        return EditMessage(peer, id, no_webpage, stop_geo_live, message, reply_markup, entities, geo_point)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.no_webpage is not None else 0
        flags |= (1 << 12) if self.stop_geo_live is not None else 0
        flags |= (1 << 11) if self.message is not None else 0
        flags |= (1 << 2) if self.reply_markup is not None else 0
        flags |= (1 << 3) if self.entities is not None else 0
        flags |= (1 << 13) if self.geo_point is not None else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(Int(self.id))
        
        if self.message is not None:
            b.write(String(self.message))
        
        if self.reply_markup is not None:
            b.write(self.reply_markup.write())
        
        if self.entities is not None:
            b.write(Vector(self.entities))
        
        if self.geo_point is not None:
            b.write(self.geo_point.write())
        
        return b.getvalue()
