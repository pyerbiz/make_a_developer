class TestClassDemoInstance:
    value = 0
    # attributes will be shared
    # across tests,
    # instances for each test wil lbe unique

    def test_one(self):
        self.value = 1
        assert self.value == 1

    def test_two(self):
        assert self.value == 1
