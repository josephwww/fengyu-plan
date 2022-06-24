from unittest import TestCase
from database.client import EmployeeClient


class TestNormal(TestCase):
    def setUp(self) -> None:
        super().setUp()
        database_client = EmployeeClient()

    def test_parse_command(self):
        Reader
