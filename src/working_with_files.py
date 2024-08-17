import os
import json
import csv

from src.abs_classes import Files


class JSONSaver(Files):
    def __init__(self, file_path="data/hh.json"):
        self.__file_path = file_path

    def get_data(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r+", encoding="utf-8") as f:
                try:
                    existing_vacancies = json.load(f)
                    return existing_vacancies

                except json.JSONDecodeError:
                    existing_vacancies = []
                    return existing_vacancies
        else:
            existing_vacancies = []
            return existing_vacancies

    def add_vacancies(self, vacancies_list):

        existing_vacancies = self.get_data()

        existing_vacancies_dict = {vacancy['id']: vacancy for vacancy in existing_vacancies}

        for vacancy in vacancies_list:
            if vacancy.id_vacancy in existing_vacancies_dict:
                continue
            existing_vacancies.append({
                "id": vacancy.id_vacancy,
                "name": vacancy.name,
                "url": vacancy.url,
                "description": vacancy.description,
                "salary": vacancy.salary
            })

        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(existing_vacancies, f, ensure_ascii=False, indent=4)

    def delete_vacancy(self, del_num):
        existing_vacancies = self.get_data()
        if not existing_vacancies:
            return []

        for index, vacancy in enumerate(existing_vacancies):
            if str(del_num) in vacancy.values():
                existing_vacancies.pop(index)
                with open(self.__file_path, "w", encoding="utf-8") as file:
                    json.dump(existing_vacancies, file, ensure_ascii=False, indent=4)

                break


class CSVSaver(Files):
    def __init__(self, file_path="data/vacancies.csv"):
        self.__file_path = file_path

    def get_data(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                return list(reader)
        return []

    def add_vacancies(self, vacancies_list):
        with open(self.__file_path, "a", encoding="utf-8", newline='') as f:
            writer = csv.DictWriter(f, fieldnames=vacancies_list[0].keys())
            if f.tell() == 0:
                writer.writeheader()
            for vacancy in vacancies_list:
                writer.writerow(vacancy)

    def delete_vacancy(self, del_number):
        pass
