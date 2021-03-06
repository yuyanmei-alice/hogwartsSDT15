#!/usr/bin/env python
# -*- coding: UTF-8 -*-'
'''
@author : yuyanmei
@Date :2020/11/7 20:26
'''
import pytest

from app.Pages.main_page import MainPage


class TestContactDetailPage():
    # 首页>通讯录>搜索>输入名称搜索>选中查询结果进入个人信息页面>更多>编辑成员
    @pytest.mark.parametrize('name', ['王五'])
    def test_goto_more(self, name):
        contactdetailpage = MainPage().goto_contactList().goto_search_contact().search_by_name(name).\
            goto_contact_detail_page().goto_more()
        contactdetailpage.goto_edit_contact()

