from abc import ABC, abstractmethod
from typing import List


class ApiParser(ABC):
    """����������� ����� ��� ������ � ��� HH.RU"""
    @abstractmethod
    def _get_response(self, keyword: str, page: int, per_page: int):
        """����������� ����� ��� ����������� � ���"""
        pass

    @abstractmethod
    def get_vacancies(self, keyword: str, page: int, per_page: int):
        """����������� ����� ��� �������������� ������ � ��� � Python ������"""
        pass


class Files(ABC):
    """����������� ����� ��� ������ � �������"""
    @abstractmethod
    def get_data(self) -> List:
        """����������� ����� ��� ��������� ������ �� �����"""
        pass

    @abstractmethod
    def add_vacancies(self, hh_vacancies: List) -> None:
        """����������� ����� ��� ���������� �������� � ����"""
        pass

    @abstractmethod
    def delete_vacancy(self, del_number: str) -> List | None:
        """����������� ����� ��� �������� �������� �� �����"""
        pass
