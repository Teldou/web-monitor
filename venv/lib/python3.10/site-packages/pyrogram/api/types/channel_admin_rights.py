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


class ChannelAdminRights(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0x5d7ceba5``

    Args:
        change_info: :obj:`bool` (optional)
        post_messages: :obj:`bool` (optional)
        edit_messages: :obj:`bool` (optional)
        delete_messages: :obj:`bool` (optional)
        ban_users: :obj:`bool` (optional)
        invite_users: :obj:`bool` (optional)
        invite_link: :obj:`bool` (optional)
        pin_messages: :obj:`bool` (optional)
        add_admins: :obj:`bool` (optional)
    """
    ID = 0x5d7ceba5

    def __init__(self, change_info=None, post_messages=None, edit_messages=None, delete_messages=None, ban_users=None, invite_users=None, invite_link=None, pin_messages=None, add_admins=None):
        self.change_info = change_info  # flags.0?true
        self.post_messages = post_messages  # flags.1?true
        self.edit_messages = edit_messages  # flags.2?true
        self.delete_messages = delete_messages  # flags.3?true
        self.ban_users = ban_users  # flags.4?true
        self.invite_users = invite_users  # flags.5?true
        self.invite_link = invite_link  # flags.6?true
        self.pin_messages = pin_messages  # flags.7?true
        self.add_admins = add_admins  # flags.9?true

    @staticmethod
    def read(b: BytesIO, *args) -> "ChannelAdminRights":
        flags = Int.read(b)
        
        change_info = True if flags & (1 << 0) else False
        post_messages = True if flags & (1 << 1) else False
        edit_messages = True if flags & (1 << 2) else False
        delete_messages = True if flags & (1 << 3) else False
        ban_users = True if flags & (1 << 4) else False
        invite_users = True if flags & (1 << 5) else False
        invite_link = True if flags & (1 << 6) else False
        pin_messages = True if flags & (1 << 7) else False
        add_admins = True if flags & (1 << 9) else False
        return ChannelAdminRights(change_info, post_messages, edit_messages, delete_messages, ban_users, invite_users, invite_link, pin_messages, add_admins)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.change_info is not None else 0
        flags |= (1 << 1) if self.post_messages is not None else 0
        flags |= (1 << 2) if self.edit_messages is not None else 0
        flags |= (1 << 3) if self.delete_messages is not None else 0
        flags |= (1 << 4) if self.ban_users is not None else 0
        flags |= (1 << 5) if self.invite_users is not None else 0
        flags |= (1 << 6) if self.invite_link is not None else 0
        flags |= (1 << 7) if self.pin_messages is not None else 0
        flags |= (1 << 9) if self.add_admins is not None else 0
        b.write(Int(flags))
        
        return b.getvalue()
