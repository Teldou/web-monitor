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


class MessageMediaInvoice(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0x84551347``

    Args:
        title: :obj:`string`
        description: :obj:`string`
        currency: :obj:`string`
        total_amount: :obj:`int`
        start_param: :obj:`string`
        shipping_address_requested: :obj:`bool` (optional)
        test: :obj:`bool` (optional)
        photo: :class:`pyrogram.api.types.WebDocument` (optional)
        receipt_msg_id: :obj:`int` (optional)
    """
    ID = 0x84551347

    def __init__(self, title, description, currency, total_amount, start_param, shipping_address_requested=None, test=None, photo=None, receipt_msg_id=None):
        self.shipping_address_requested = shipping_address_requested  # flags.1?true
        self.test = test  # flags.3?true
        self.title = title  # string
        self.description = description  # string
        self.photo = photo  # flags.0?WebDocument
        self.receipt_msg_id = receipt_msg_id  # flags.2?int
        self.currency = currency  # string
        self.total_amount = total_amount  # long
        self.start_param = start_param  # string

    @staticmethod
    def read(b: BytesIO, *args) -> "MessageMediaInvoice":
        flags = Int.read(b)
        
        shipping_address_requested = True if flags & (1 << 1) else False
        test = True if flags & (1 << 3) else False
        title = String.read(b)
        
        description = String.read(b)
        
        photo = Object.read(b) if flags & (1 << 0) else None
        
        receipt_msg_id = Int.read(b) if flags & (1 << 2) else None
        currency = String.read(b)
        
        total_amount = Long.read(b)
        
        start_param = String.read(b)
        
        return MessageMediaInvoice(title, description, currency, total_amount, start_param, shipping_address_requested, test, photo, receipt_msg_id)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.shipping_address_requested is not None else 0
        flags |= (1 << 3) if self.test is not None else 0
        flags |= (1 << 0) if self.photo is not None else 0
        flags |= (1 << 2) if self.receipt_msg_id is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.title))
        
        b.write(String(self.description))
        
        if self.photo is not None:
            b.write(self.photo.write())
        
        if self.receipt_msg_id is not None:
            b.write(Int(self.receipt_msg_id))
        
        b.write(String(self.currency))
        
        b.write(Long(self.total_amount))
        
        b.write(String(self.start_param))
        
        return b.getvalue()
