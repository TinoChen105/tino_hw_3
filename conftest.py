import pytest
from libs.base_session import BaseSession


@pytest.fixture(scope="function")
def base_session():
    return BaseSession()
