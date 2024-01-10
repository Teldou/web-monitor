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


class EditChatPhoto(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0xca4c79d8``

    Args:
        chat_id: :obj:`int`
        photo: :class:`pyrogram.api.types.InputChatPhoto`

    Returns:
        :class:`pyrogram.api.types.UpdatesTooLong` | :class:`pyrogram.api.types.UpdateShortMessage` | :class:`pyrogram.api.types.UpdateShortChatMessage` | :class:`pyrogram.api.types.UpdateShort` | :class:`pyrogram.api.types.UpdatesCombined` | :class:`pyrogram.api.types.Update` | :class:`pyrogram.api.types.UpdateShortSentMessage`

    Raises:
        :class:`pyrogram.Error`
    """
    ID = 0xca4c79d8

    def __init__(self, chat_id, photo):
        self.chat_id = chat_id  # int
        self.photo = photo  # InputChatPhoto

    @staticmethod
    def read(b: BytesIO, *args) -> "EditChatPhoto":
        # No flags
        
        chat_id = Int.read(b)
        
        photo = Object.read(b)
        
        return EditChatPhoto(chat_id, photo)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.chat_id))
        
        b.write(self.photo.write())
        
        return b.getvalue()
