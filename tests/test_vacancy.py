from src.vacancy import Vacancy


def test_vacancy(vacancies_fixture):

    vacancy = {"salary": None}
    result = Vacancy.salary_data(vacancy)
    assert result == 0

    vacancy = {"salary": {"from": 1, "to": None}}
    result = Vacancy.salary_data(vacancy)
    assert result == 1

    vacancy = {"salary": {"from": None, "to": 2}}
    result = Vacancy.salary_data(vacancy)
    assert result == 2

    vacancy = {"salary": {"from": 4, "to": 2}}
    result = Vacancy.salary_data(vacancy)
    assert result == 3


def test_dunder_methods(vacancies_fixture2):

    assert vacancies_fixture2[0] == vacancies_fixture2[2]

    assert vacancies_fixture2[1] > vacancies_fixture2[2]

    assert vacancies_fixture2[1] != vacancies_fixture2[2]

    assert vacancies_fixture2[0] >= vacancies_fixture2[2]

    assert vacancies_fixture2[0] <= vacancies_fixture2[2]

    assert vacancies_fixture2[2] < vacancies_fixture2[1]

    non_vacancy_object = "not a vacancy"

    assert (vacancies_fixture2[0] == non_vacancy_object) is False
