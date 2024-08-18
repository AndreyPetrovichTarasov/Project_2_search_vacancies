import pytest

from src.vacancy import Vacancy


@pytest.fixture
def vacancies_fixture():
    vacancies = [
        Vacancy("100", "Developer", "http://1.com", "Python developer", 10000),
        Vacancy("200", "Analytic", "http://2.com", "Python analytic", 20000),
        Vacancy("300", "Manager", "http://3.com", "Python manager", 30000),
    ]

    return vacancies


@pytest.fixture
def vacancies_fixture2():
    vacancies = [
        Vacancy("100", "Developer", "http://1.com", "Python developer", 10000),
        Vacancy("200", "Analytic", "http://2.com", "Python analytic", 20000),
        Vacancy("300", "Manager", "http://3.com", "Python manager", 10000),
    ]

    return vacancies