#!/usr/bin/env python
# -*- coding: UTF-8 -*-'
'''
@author : yuyanmei
@Date :2020/11/9 10:53
'''
import pytest

from app.Pages.main_page import MainPage


class TestAddMemberPage():
    @pytest.mark.parametrize('name,phoneNum', [('小兰', '15811112222')])
    def test_add_member(self, name, phoneNum):
        MainPage().goto_contactList().add_contact().goto_addMember_manual().add_member(name, phoneNum)