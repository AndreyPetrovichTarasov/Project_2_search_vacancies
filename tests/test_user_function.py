from src.user_function import (filter_vacancies, get_vacancies_by_salary, sort_vacancies,
                               get_top_vacancies, print_vacancies)


def test_filter_vacancies(vacancies_fixture):

    result = filter_vacancies(vacancies_fixture, "Python")
    assert len(result) == 3

    result = filter_vacancies(vacancies_fixture, "analytic")
    assert len(result) == 1
    assert result[0].name == "Analytic"

    result = filter_vacancies(vacancies_fixture, "Java")
    assert len(result) == 0


def test_get_vacancies_by_salary(vacancies_fixture):

    result = get_vacancies_by_salary(vacancies_fixture, 100)
    assert len(result) == 3

    result = get_vacancies_by_salary(vacancies_fixture, 35000)
    assert len(result) == 0


def test_sort_vacancies(vacancies_fixture):

    result = sort_vacancies(vacancies_fixture)
    assert result == vacancies_fixture


def test_get_top_vacancies(vacancies_fixture):

    result = get_top_vacancies(vacancies_fixture, 2)
    assert len(result) == 2


def test_print_vacancies(capsys, vacancies_fixture):

    print_vacancies(vacancies_fixture)

    captured = capsys.readouterr()

    expected_output = (
        'Номер: 100. Название: Developer. Зарплата: 10000. Ссылка на вакансию: http://1.com. Описание: Python developer'
        '\nНомер: 200. Название: Analytic. Зарплата: 20000. Ссылка на вакансию: http://2.com. Описание: Python analytic'
        '\nНомер: 300. Название: Manager. Зарплата: 30000. Ссылка на вакансию: http://3.com. Описание: Python manager\n'
    )

    assert captured.out == expected_output
