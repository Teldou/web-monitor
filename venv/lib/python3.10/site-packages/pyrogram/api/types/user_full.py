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


class UserFull(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0x0f220f3f``

    Args:
        user: :class:`pyrogram.api.types.User`
        link: :class:`pyrogram.api.types.contacts.Link`
        notify_settings: :class:`pyrogram.api.types.PeerNotifySettings`
        common_chats_count: :obj:`int`
        blocked: :obj:`bool` (optional)
        phone_calls_available: :obj:`bool` (optional)
        phone_calls_private: :obj:`bool` (optional)
        about: :obj:`string` (optional)
        profile_photo: :class:`pyrogram.api.types.Photo` (optional)
        bot_info: :class:`pyrogram.api.types.BotInfo` (optional)
    """
    ID = 0x0f220f3f

    def __init__(self, user, link, notify_settings, common_chats_count, blocked=None, phone_calls_available=None, phone_calls_private=None, about=None, profile_photo=None, bot_info=None):
        self.blocked = blocked  # flags.0?true
        self.phone_calls_available = phone_calls_available  # flags.4?true
        self.phone_calls_private = phone_calls_private  # flags.5?true
        self.user = user  # User
        self.about = about  # flags.1?string
        self.link = link  # contacts.Link
        self.profile_photo = profile_photo  # flags.2?Photo
        self.notify_settings = notify_settings  # PeerNotifySettings
        self.bot_info = bot_info  # flags.3?BotInfo
        self.common_chats_count = common_chats_count  # int

    @staticmethod
    def read(b: BytesIO, *args) -> "UserFull":
        flags = Int.read(b)
        
        blocked = True if flags & (1 << 0) else False
        phone_calls_available = True if flags & (1 << 4) else False
        phone_calls_private = True if flags & (1 << 5) else False
        user = Object.read(b)
        
        about = String.read(b) if flags & (1 << 1) else None
        link = Object.read(b)
        
        profile_photo = Object.read(b) if flags & (1 << 2) else None
        
        notify_settings = Object.read(b)
        
        bot_info = Object.read(b) if flags & (1 << 3) else None
        
        common_chats_count = Int.read(b)
        
        return UserFull(user, link, notify_settings, common_chats_count, blocked, phone_calls_available, phone_calls_private, about, profile_photo, bot_info)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.blocked is not None else 0
        flags |= (1 << 4) if self.phone_calls_available is not None else 0
        flags |= (1 << 5) if self.phone_calls_private is not None else 0
        flags |= (1 << 1) if self.about is not None else 0
        flags |= (1 << 2) if self.profile_photo is not None else 0
        flags |= (1 << 3) if self.bot_info is not None else 0
        b.write(Int(flags))
        
        b.write(self.user.write())
        
        if self.about is not None:
            b.write(String(self.about))
        
        b.write(self.link.write())
        
        if self.profile_photo is not None:
            b.write(self.profile_photo.write())
        
        b.write(self.notify_settings.write())
        
        if self.bot_info is not None:
            b.write(self.bot_info.write())
        
        b.write(Int(self.common_chats_count))
        
        return b.getvalue()
