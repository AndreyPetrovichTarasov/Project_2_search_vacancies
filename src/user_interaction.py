def search_query():
    user_query = input("Введите поисковый запрос: ")
    try:
        per_pages = int(input("Введите количество вакансий для загрузки с сайта. Вакансий на странице: "))
        pages = int(input("Всего страниц: "))
    except Exception as e:
        print(f"Неверный ввод. Ошибка запроса - {e}. Перезапустите программу.")
        return None

    return user_query, pages, per_pages


def filter_data():
    print("Данные сформированы.")

    filter_words = input("Введите ключевые слова для фильтрации вакансий: ")

    salary = input("Введите нижний порог зарплаты: ")
    if not salary:
        salary = 0
    else:
        try:
            salary = int(salary)
        except Exception as e:
            print(f"Неверный ввод. Ошибка величины зарплаты - {e}. Перезапустите программу.")
            return None

    try:
        top_n = int(input("Введите количество вакансий для окончательного вывода: "))
    except Exception as e:
        print(f"Неверный ввод. Ошибка количества - {e}. Перезапустите программу.")
        return None

    return filter_words, salary, top_n


def delete_vacancy():
    try:
        del_number = int(input("Если хотите удалить вакансию, введите id (номер вакансии): "))
    except Exception as e:
        print(f"Неверный ввод. Ошибка при удалении - {e}. Перезапустите программу.")
        return None

    return del_number
