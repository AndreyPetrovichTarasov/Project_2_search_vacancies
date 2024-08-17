class Vacancy:
    __slots__ = ("id_vacancy", "name", "url", "description", "salary")

    def __init__(self, id_vacancy, name, url, description, salary):
        # Валидация данных перед присвоением
        self.id_vacancy = self.__validate_id(id_vacancy)
        self.name = self.__validate_name(name)
        self.url = self.__validate_url(url)
        self.description = self.__validate_description(description)
        self.salary = self.__validate_salary(salary)

    def __str__(self):
        return (f"Номер: {self.id_vacancy}. Название: {self.name}. "
                f"Зарплата: {self.salary}. Ссылка на вакансию: {self.url}. "
                f"Описание: {self.description.replace('\u2060', '')}")

    # Приватные методы для валидации данных
    @staticmethod
    def __validate_id(id_vacancy):
        if not isinstance(id_vacancy, str) or not id_vacancy.isdigit():
            raise ValueError("Invalid id")
        return id_vacancy

    @staticmethod
    def __validate_name(name):
        if not isinstance(name, str) or not name:
            raise ValueError("Invalid name")
        return name

    @staticmethod
    def __validate_url(url):
        if not isinstance(url, str) or not url.startswith("http"):
            raise ValueError("Invalid URL")
        return url

    @staticmethod
    def __validate_description(description):
        if not isinstance(description, str):
            raise ValueError("Invalid description")
        return description

    @staticmethod
    def __validate_salary(salary):
        if salary is None:
            return 0
        elif not (isinstance(salary, int) or isinstance(salary, float)) or salary < 0:
            raise ValueError("Invalid salary_min")
        return salary

    @staticmethod
    def salary_data(vacancy):
        if vacancy.get("salary") is None:
            return 0
        elif vacancy.get("salary").get("from") and vacancy.get("salary").get("to") is None:
            return vacancy.get("salary").get("from")
        elif vacancy.get("salary").get("from") is None and vacancy.get("salary").get("to"):
            return vacancy.get("salary").get("to")
        else:
            return (vacancy.get("salary").get("to") + vacancy.get("salary").get("from")) / 2

    @classmethod
    def cast_to_object_list(cls, hh_vacancies):
        vacancy_objects = []
        for vacancy in hh_vacancies:
            try:
                salary = cls.salary_data(vacancy)

                vacancy = cls(
                    id_vacancy=vacancy.get("id"),
                    name=vacancy.get("name"),
                    url=vacancy.get("alternate_url"),
                    description=vacancy.get("snippet", {}).get("requirement", ""),
                    salary=round(salary)
                )
                vacancy_objects.append(vacancy)
            except ValueError as e:
                print(f"Skipping invalid vacancy: {e}")
        return vacancy_objects

    def __eq__(self, other):
        """Сравнение на равенство по минимальной зарплате"""
        if isinstance(other, Vacancy):
            return self.salary == other.salary
        return NotImplemented

    def __lt__(self, other):
        """Сравнение вакансий: меньше по минимальной зарплате"""
        if isinstance(other, Vacancy):
            return self.salary < other.salary
        return NotImplemented

    def __le__(self, other):
        """Сравнение вакансий: меньше или равно по минимальной зарплате"""
        if isinstance(other, Vacancy):
            return self.salary <= other.salary
        return NotImplemented

    def __gt__(self, other):
        """Сравнение вакансий: больше по минимальной зарплате"""
        if isinstance(other, Vacancy):
            return self.salary > other.salary
        return NotImplemented

    def __ge__(self, other):
        """Сравнение вакансий: больше или равно по минимальной зарплате"""
        if isinstance(other, Vacancy):
            return self.salary >= other.salary
        return NotImplemented

    def __repr__(self):
        """Представление объекта Vacancy"""
        return f"Vacancy(title={self.name}, salary={self.salary})"