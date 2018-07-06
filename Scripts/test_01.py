import allure, pytest

class Test_001:
    @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    @allure.step(title="登陆")
    def test_001_1(self):
        allure.attach('描述', '输入用户名')
        allure.attach('描述', '输入密码')
        allure.attach('描述', '点击登陆')
        assert 1

    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.step(title="注册")
    def test_001_2(self):
        allure.attach('描述', '这里完成了注册操作')
        assert 1
