from abc import ABC, abstractmethod
from typing import Any, Dict, List


class AbsApi(ABC):
    """
    Абстрактный класс работы с API
        connect(self) -> Dict[Any, Any]:
            Метод подключения к API
    """

    @abstractmethod
    def connect(self) -> Dict[Any, Any]:
        """Метод подключения к API"""
        pass


class AbsPostgresSQL(ABC):
    """
    Абстрактный класс работы с PostgresSQL
        connect(self) -> Dict[Any, Any]:
            Метод подключения к API
    """

    @abstractmethod
    def __connect(self) -> Dict[Any, Any]:
        """Метод подключение к БД"""
        pass