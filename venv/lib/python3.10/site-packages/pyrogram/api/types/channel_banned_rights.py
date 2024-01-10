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


class ChannelBannedRights(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0x58cf4249``

    Args:
        until_date: :obj:`int`
        view_messages: :obj:`bool` (optional)
        send_messages: :obj:`bool` (optional)
        send_media: :obj:`bool` (optional)
        send_stickers: :obj:`bool` (optional)
        send_gifs: :obj:`bool` (optional)
        send_games: :obj:`bool` (optional)
        send_inline: :obj:`bool` (optional)
        embed_links: :obj:`bool` (optional)
    """
    ID = 0x58cf4249

    def __init__(self, until_date, view_messages=None, send_messages=None, send_media=None, send_stickers=None, send_gifs=None, send_games=None, send_inline=None, embed_links=None):
        self.view_messages = view_messages  # flags.0?true
        self.send_messages = send_messages  # flags.1?true
        self.send_media = send_media  # flags.2?true
        self.send_stickers = send_stickers  # flags.3?true
        self.send_gifs = send_gifs  # flags.4?true
        self.send_games = send_games  # flags.5?true
        self.send_inline = send_inline  # flags.6?true
        self.embed_links = embed_links  # flags.7?true
        self.until_date = until_date  # int

    @staticmethod
    def read(b: BytesIO, *args) -> "ChannelBannedRights":
        flags = Int.read(b)
        
        view_messages = True if flags & (1 << 0) else False
        send_messages = True if flags & (1 << 1) else False
        send_media = True if flags & (1 << 2) else False
        send_stickers = True if flags & (1 << 3) else False
        send_gifs = True if flags & (1 << 4) else False
        send_games = True if flags & (1 << 5) else False
        send_inline = True if flags & (1 << 6) else False
        embed_links = True if flags & (1 << 7) else False
        until_date = Int.read(b)
        
        return ChannelBannedRights(until_date, view_messages, send_messages, send_media, send_stickers, send_gifs, send_games, send_inline, embed_links)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.view_messages is not None else 0
        flags |= (1 << 1) if self.send_messages is not None else 0
        flags |= (1 << 2) if self.send_media is not None else 0
        flags |= (1 << 3) if self.send_stickers is not None else 0
        flags |= (1 << 4) if self.send_gifs is not None else 0
        flags |= (1 << 5) if self.send_games is not None else 0
        flags |= (1 << 6) if self.send_inline is not None else 0
        flags |= (1 << 7) if self.embed_links is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.until_date))
        
        return b.getvalue()
