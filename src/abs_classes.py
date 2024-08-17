from abc import ABC, abstractmethod


class ApiParser(ABC):

    @abstractmethod
    def _get_response(self, keyword, page, per_page):
        pass

    @abstractmethod
    def get_vacancies(self, keyword: str, page: int, per_page: int):
        pass


class Files(ABC):

    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def add_vacancies(self, hh_vacancies):
        pass

    @abstractmethod
    def delete_vacancy(self, del_number):
        pass

