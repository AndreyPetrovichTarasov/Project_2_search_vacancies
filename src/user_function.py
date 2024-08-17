def filter_vacancies(vacancies_list, filter_words):
    filtered_vacancies = []
    for vacancy in vacancies_list:
        if filter_words in vacancy.description:
            filtered_vacancies.append(vacancy)

    return filtered_vacancies


def get_vacancies_by_salary(filtered_vacancies, salary):
    ranged_vacancies = []
    for vacancy in filtered_vacancies:
        if vacancy.salary > salary:
            ranged_vacancies.append(vacancy)

    return ranged_vacancies


def sort_vacancies(ranged_vacancies):
    return sorted(ranged_vacancies, key=lambda x: x.salary)


def get_top_vacancies(sorted_vacancies, top_n=10):
    if top_n > len(sorted_vacancies):
        top_n = len(sorted_vacancies)

    return sorted_vacancies[:top_n]


def print_vacancies(top_vacancies):
    for vacancy in top_vacancies:
        print(vacancy)
