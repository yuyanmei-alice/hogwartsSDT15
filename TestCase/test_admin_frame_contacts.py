#!/usr/bin/env python
# -*- coding: UTF-8 -*-'
'''
@author : yuyanmei
@Date :2020/10/29 15:03
'''
from Pages.admin_frame_page import AdminFramePage


class TestAdminFrameContacts():
    def test_addMember(self):
        AdminFramePage().common_entrance_add_member().addMember()

