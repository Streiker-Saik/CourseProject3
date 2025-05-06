import psycopg2


class DBManager:
    """
    Класс работы с БД PostgreSQL
    """
    __db_key: str

    def __init__(self, __db_key: str):
        """Инициализация класса DBManager"""
        self.__host = "localhost"
        self.__port = 5432
        self.__database = "analysis"
        self.__user = "postgres"
        self.__password = __db_key

    def connect(self):
        """"""
        return self.__connect

    def __connect(self):
        """"""
        conn_params = {
            "host": self.__host,
            "database": self.__database,
            "user": self.__user,
            "password": self.__password
        }
        self.conn = psycopg2.connect(**conn_params)

    def get_companies_and_vacancies_count(self):
        """Метод получает список всех компаний и количество вакансий у каждой компании"""
        pass

    def get_all_vacancies(self):
        """Метод получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию"""
        pass

    def get_avg_salary(self):
        """Метод получает среднюю зарплату по вакансиям"""
        pass

    def get_vacancies_with_higher_salary(self):
        """Метод получает список всех вакансий, у которых зарплата выше средней по всем вакансиям"""
        pass

    def get_vacancies_with_keyword(self, keyword):
        """Метод получает список всех вакансий, в названии которых содержатся переданные в метод слова"""
        pass