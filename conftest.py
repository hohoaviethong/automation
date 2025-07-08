from utils.read_config import ConfigReader
import pytest

@pytest.fixture
def config():
    return ConfigReader.load_config()