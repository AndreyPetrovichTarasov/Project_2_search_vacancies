from src.hh_api import HeadHunterAPI
from src.vacancy import Vacancy
from src.working_with_files import JSONSaver
from src.user_function import (filter_vacancies, get_vacancies_by_salary,
                               sort_vacancies, get_top_vacancies, print_vacancies)
from src.user_interaction import search_query, filter_data, delete_vacancy


def user_interaction() -> None:
    """Главная функция взаимодействия с пользователем."""
    user_query, pages, per_pages = search_query()

    hh_api = HeadHunterAPI()

    hh_vacancies = hh_api.get_vacancies(user_query, pages, per_pages)

    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)

    json_saver = JSONSaver("data/hh2.json")
    json_saver.add_vacancies(vacancies_list)

    filter_words, salary, top_n = filter_data()

    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)

    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary)

    sorted_vacancies = sort_vacancies(ranged_vacancies)

    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)

    print_vacancies(top_vacancies)

    del_number = delete_vacancy()
    json_saver.delete_vacancy(del_number)


if __name__ == "__main__":
    user_interaction()
