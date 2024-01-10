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


class Config(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0x86b5778e``

    Args:
        date: :obj:`int`
        expires: :obj:`int`
        test_mode: :obj:`bool`
        this_dc: :obj:`int`
        dc_options: List of :class:`pyrogram.api.types.DcOption`
        chat_size_max: :obj:`int`
        megagroup_size_max: :obj:`int`
        forwarded_count_max: :obj:`int`
        online_update_period_ms: :obj:`int`
        offline_blur_timeout_ms: :obj:`int`
        offline_idle_timeout_ms: :obj:`int`
        online_cloud_timeout_ms: :obj:`int`
        notify_cloud_delay_ms: :obj:`int`
        notify_default_delay_ms: :obj:`int`
        push_chat_period_ms: :obj:`int`
        push_chat_limit: :obj:`int`
        saved_gifs_limit: :obj:`int`
        edit_time_limit: :obj:`int`
        revoke_time_limit: :obj:`int`
        revoke_pm_time_limit: :obj:`int`
        rating_e_decay: :obj:`int`
        stickers_recent_limit: :obj:`int`
        stickers_faved_limit: :obj:`int`
        channels_read_media_period: :obj:`int`
        pinned_dialogs_count_max: :obj:`int`
        call_receive_timeout_ms: :obj:`int`
        call_ring_timeout_ms: :obj:`int`
        call_connect_timeout_ms: :obj:`int`
        call_packet_timeout_ms: :obj:`int`
        me_url_prefix: :obj:`string`
        phonecalls_enabled: :obj:`bool` (optional)
        default_p2p_contacts: :obj:`bool` (optional)
        preload_featured_stickers: :obj:`bool` (optional)
        ignore_phone_entities: :obj:`bool` (optional)
        revoke_pm_inbox: :obj:`bool` (optional)
        tmp_sessions: :obj:`int` (optional)
        suggested_lang_code: :obj:`string` (optional)
        lang_pack_version: :obj:`int` (optional)
    """
    ID = 0x86b5778e

    def __init__(self, date, expires, test_mode, this_dc, dc_options, chat_size_max, megagroup_size_max, forwarded_count_max, online_update_period_ms, offline_blur_timeout_ms, offline_idle_timeout_ms, online_cloud_timeout_ms, notify_cloud_delay_ms, notify_default_delay_ms, push_chat_period_ms, push_chat_limit, saved_gifs_limit, edit_time_limit, revoke_time_limit, revoke_pm_time_limit, rating_e_decay, stickers_recent_limit, stickers_faved_limit, channels_read_media_period, pinned_dialogs_count_max, call_receive_timeout_ms, call_ring_timeout_ms, call_connect_timeout_ms, call_packet_timeout_ms, me_url_prefix, phonecalls_enabled=None, default_p2p_contacts=None, preload_featured_stickers=None, ignore_phone_entities=None, revoke_pm_inbox=None, tmp_sessions=None, suggested_lang_code=None, lang_pack_version=None):
        self.phonecalls_enabled = phonecalls_enabled  # flags.1?true
        self.default_p2p_contacts = default_p2p_contacts  # flags.3?true
        self.preload_featured_stickers = preload_featured_stickers  # flags.4?true
        self.ignore_phone_entities = ignore_phone_entities  # flags.5?true
        self.revoke_pm_inbox = revoke_pm_inbox  # flags.6?true
        self.date = date  # int
        self.expires = expires  # int
        self.test_mode = test_mode  # Bool
        self.this_dc = this_dc  # int
        self.dc_options = dc_options  # Vector<DcOption>
        self.chat_size_max = chat_size_max  # int
        self.megagroup_size_max = megagroup_size_max  # int
        self.forwarded_count_max = forwarded_count_max  # int
        self.online_update_period_ms = online_update_period_ms  # int
        self.offline_blur_timeout_ms = offline_blur_timeout_ms  # int
        self.offline_idle_timeout_ms = offline_idle_timeout_ms  # int
        self.online_cloud_timeout_ms = online_cloud_timeout_ms  # int
        self.notify_cloud_delay_ms = notify_cloud_delay_ms  # int
        self.notify_default_delay_ms = notify_default_delay_ms  # int
        self.push_chat_period_ms = push_chat_period_ms  # int
        self.push_chat_limit = push_chat_limit  # int
        self.saved_gifs_limit = saved_gifs_limit  # int
        self.edit_time_limit = edit_time_limit  # int
        self.revoke_time_limit = revoke_time_limit  # int
        self.revoke_pm_time_limit = revoke_pm_time_limit  # int
        self.rating_e_decay = rating_e_decay  # int
        self.stickers_recent_limit = stickers_recent_limit  # int
        self.stickers_faved_limit = stickers_faved_limit  # int
        self.channels_read_media_period = channels_read_media_period  # int
        self.tmp_sessions = tmp_sessions  # flags.0?int
        self.pinned_dialogs_count_max = pinned_dialogs_count_max  # int
        self.call_receive_timeout_ms = call_receive_timeout_ms  # int
        self.call_ring_timeout_ms = call_ring_timeout_ms  # int
        self.call_connect_timeout_ms = call_connect_timeout_ms  # int
        self.call_packet_timeout_ms = call_packet_timeout_ms  # int
        self.me_url_prefix = me_url_prefix  # string
        self.suggested_lang_code = suggested_lang_code  # flags.2?string
        self.lang_pack_version = lang_pack_version  # flags.2?int

    @staticmethod
    def read(b: BytesIO, *args) -> "Config":
        flags = Int.read(b)
        
        phonecalls_enabled = True if flags & (1 << 1) else False
        default_p2p_contacts = True if flags & (1 << 3) else False
        preload_featured_stickers = True if flags & (1 << 4) else False
        ignore_phone_entities = True if flags & (1 << 5) else False
        revoke_pm_inbox = True if flags & (1 << 6) else False
        date = Int.read(b)
        
        expires = Int.read(b)
        
        test_mode = Bool.read(b)
        
        this_dc = Int.read(b)
        
        dc_options = Object.read(b)
        
        chat_size_max = Int.read(b)
        
        megagroup_size_max = Int.read(b)
        
        forwarded_count_max = Int.read(b)
        
        online_update_period_ms = Int.read(b)
        
        offline_blur_timeout_ms = Int.read(b)
        
        offline_idle_timeout_ms = Int.read(b)
        
        online_cloud_timeout_ms = Int.read(b)
        
        notify_cloud_delay_ms = Int.read(b)
        
        notify_default_delay_ms = Int.read(b)
        
        push_chat_period_ms = Int.read(b)
        
        push_chat_limit = Int.read(b)
        
        saved_gifs_limit = Int.read(b)
        
        edit_time_limit = Int.read(b)
        
        revoke_time_limit = Int.read(b)
        
        revoke_pm_time_limit = Int.read(b)
        
        rating_e_decay = Int.read(b)
        
        stickers_recent_limit = Int.read(b)
        
        stickers_faved_limit = Int.read(b)
        
        channels_read_media_period = Int.read(b)
        
        tmp_sessions = Int.read(b) if flags & (1 << 0) else None
        pinned_dialogs_count_max = Int.read(b)
        
        call_receive_timeout_ms = Int.read(b)
        
        call_ring_timeout_ms = Int.read(b)
        
        call_connect_timeout_ms = Int.read(b)
        
        call_packet_timeout_ms = Int.read(b)
        
        me_url_prefix = String.read(b)
        
        suggested_lang_code = String.read(b) if flags & (1 << 2) else None
        lang_pack_version = Int.read(b) if flags & (1 << 2) else None
        return Config(date, expires, test_mode, this_dc, dc_options, chat_size_max, megagroup_size_max, forwarded_count_max, online_update_period_ms, offline_blur_timeout_ms, offline_idle_timeout_ms, online_cloud_timeout_ms, notify_cloud_delay_ms, notify_default_delay_ms, push_chat_period_ms, push_chat_limit, saved_gifs_limit, edit_time_limit, revoke_time_limit, revoke_pm_time_limit, rating_e_decay, stickers_recent_limit, stickers_faved_limit, channels_read_media_period, pinned_dialogs_count_max, call_receive_timeout_ms, call_ring_timeout_ms, call_connect_timeout_ms, call_packet_timeout_ms, me_url_prefix, phonecalls_enabled, default_p2p_contacts, preload_featured_stickers, ignore_phone_entities, revoke_pm_inbox, tmp_sessions, suggested_lang_code, lang_pack_version)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.phonecalls_enabled is not None else 0
        flags |= (1 << 3) if self.default_p2p_contacts is not None else 0
        flags |= (1 << 4) if self.preload_featured_stickers is not None else 0
        flags |= (1 << 5) if self.ignore_phone_entities is not None else 0
        flags |= (1 << 6) if self.revoke_pm_inbox is not None else 0
        flags |= (1 << 0) if self.tmp_sessions is not None else 0
        flags |= (1 << 2) if self.suggested_lang_code is not None else 0
        flags |= (1 << 2) if self.lang_pack_version is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.date))
        
        b.write(Int(self.expires))
        
        b.write(Bool(self.test_mode))
        
        b.write(Int(self.this_dc))
        
        b.write(Vector(self.dc_options))
        
        b.write(Int(self.chat_size_max))
        
        b.write(Int(self.megagroup_size_max))
        
        b.write(Int(self.forwarded_count_max))
        
        b.write(Int(self.online_update_period_ms))
        
        b.write(Int(self.offline_blur_timeout_ms))
        
        b.write(Int(self.offline_idle_timeout_ms))
        
        b.write(Int(self.online_cloud_timeout_ms))
        
        b.write(Int(self.notify_cloud_delay_ms))
        
        b.write(Int(self.notify_default_delay_ms))
        
        b.write(Int(self.push_chat_period_ms))
        
        b.write(Int(self.push_chat_limit))
        
        b.write(Int(self.saved_gifs_limit))
        
        b.write(Int(self.edit_time_limit))
        
        b.write(Int(self.revoke_time_limit))
        
        b.write(Int(self.revoke_pm_time_limit))
        
        b.write(Int(self.rating_e_decay))
        
        b.write(Int(self.stickers_recent_limit))
        
        b.write(Int(self.stickers_faved_limit))
        
        b.write(Int(self.channels_read_media_period))
        
        if self.tmp_sessions is not None:
            b.write(Int(self.tmp_sessions))
        
        b.write(Int(self.pinned_dialogs_count_max))
        
        b.write(Int(self.call_receive_timeout_ms))
        
        b.write(Int(self.call_ring_timeout_ms))
        
        b.write(Int(self.call_connect_timeout_ms))
        
        b.write(Int(self.call_packet_timeout_ms))
        
        b.write(String(self.me_url_prefix))
        
        if self.suggested_lang_code is not None:
            b.write(String(self.suggested_lang_code))
        
        if self.lang_pack_version is not None:
            b.write(Int(self.lang_pack_version))
        
        return b.getvalue()
