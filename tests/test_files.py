from src.working_with_files import JSONSaver


def test_add_vacancies(vacancies_fixture):

    filepath = "test.json"
    with open(filepath, "w"):

        saver = JSONSaver(filepath)

        saver.add_vacancies(vacancies_fixture)
        data = saver.get_data()

        assert len(data) == 3
        assert data[0]['name'] == "Developer"
        assert data[1]['name'] == "Analytic"


def test_delete_vacancy(vacancies_fixture):

    filepath = "test.json"

    saver = JSONSaver(filepath)

    saver.add_vacancies(vacancies_fixture)
    saver.delete_vacancy(100)

    data = saver.get_data()
    assert len(data) == 2

