#coding:utf-8
import pytest
import os
if __name__=='__main__':
    pytest.main()
    os.system("allure generate ./case -o ./reports")
    