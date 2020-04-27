import pytest

@pytest.fixture
def my_fixture():
    return 10
@pytest.fixture(autouse=True)
def my_auto_use_fixture():
    return 5

def test_one(my_fixture):
    assert my_fixture + 5 == 15

def test_two(my_fixture):
    assert my_fixture - 5 == 5

def test_three():
    assert my_auto_use_fixture  == 5


# (MyLearningNotes) C:\Users\minal\PycharmProjects\MyLearningNotes\Python\practice\other>pytest -n 2 pytest_fixtures.py
# ======================================================= test session starts ========================================================
# platform win32 -- Python 3.7.7, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
# rootdir: C:\Users\minal\PycharmProjects\MyLearningNotes\Python\practice\other
# plugins: cov-2.8.1, forked-1.1.3, xdist-1.31.0
# gw0 [2] / gw1 [2]
# ..                                                                                                                            [100%]
# ======================================================== 2 passed in 1.39s =========================================================