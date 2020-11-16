#!/usr/bin/env python
# -*- coding: UTF-8 -*-'
'''
@author : yuyanmei
@Date :2020/11/16 18:13
'''
import allure


def handle_black(fun):
    def wrapper(*args, **kwargs):
        from app1.Pages.base_page import BasePage
        instance: BasePage = args[0]
        try:
            result = fun(*args, **kwargs)
            instance._error_num = 0
            return result
        except Exception as e:
            if instance.error_num > instance.max_error_num:
                raise e
            else:
                print("----进入黑名单异常处理---")
                instance._error_num = instance.error_num + 1
                instance.driver.save_screenshot("tmp.png")
                with open("tmp.png", "rb") as f:
                    content = f.read()
                allure.attach(content, attachment_type=allure.attachment_type.PNG)
                for black_ele in instance.black_list:
                    result = instance.driver.find_elements(black_ele['by'], black_ele['locator'])
                    if len(result) > 0:
                        result[0].click()
                        return wrapper(*args, **kwargs)
    return wrapper
