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


class UploadMedia(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0x519bc2b1``

    Args:
        peer: :class:`pyrogram.api.types.InputPeer`
        media: :class:`pyrogram.api.types.InputMedia`

    Returns:
        :class:`pyrogram.api.types.MessageMediaEmpty` | :class:`pyrogram.api.types.MessageMediaPhoto` | :class:`pyrogram.api.types.MessageMediaGeo` | :class:`pyrogram.api.types.MessageMediaContact` | :class:`pyrogram.api.types.MessageMediaUnsupported` | :class:`pyrogram.api.types.MessageMediaDocument` | :class:`pyrogram.api.types.MessageMediaWebPage` | :class:`pyrogram.api.types.MessageMediaVenue` | :class:`pyrogram.api.types.MessageMediaGame` | :class:`pyrogram.api.types.MessageMediaInvoice` | :class:`pyrogram.api.types.MessageMediaGeoLive`

    Raises:
        :class:`pyrogram.Error`
    """
    ID = 0x519bc2b1

    def __init__(self, peer, media):
        self.peer = peer  # InputPeer
        self.media = media  # InputMedia

    @staticmethod
    def read(b: BytesIO, *args) -> "UploadMedia":
        # No flags
        
        peer = Object.read(b)
        
        media = Object.read(b)
        
        return UploadMedia(peer, media)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(self.media.write())
        
        return b.getvalue()
