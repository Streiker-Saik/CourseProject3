from src.hh_api import HeadHunterAPI, HHVacanciesAPI, HHEmployerAPI, HHEmployersAPI
from src.exceptions import APIError
from unittest.mock import MagicMock, patch
import requests
from typing import Any, Dict, List
import pytest


@patch.object(HeadHunterAPI, "_HeadHunterAPI__connect")
def test_connect(mock_connect: MagicMock) -> None:
    """Тестирование, работы запроса API"""
    expected_result: Dict[str, Any] = {}
    mock_connect.return_value = expected_result
    hh_api = HeadHunterAPI()
    assert hh_api.connect() == expected_result


@patch("requests.get")
def test_private_connect(mock_request: MagicMock) -> None:
    """Тестирование, работы приватного запроса API"""
    expected_result = {"id": "123"}
    mock_request.return_value.json.return_value = expected_result
    mock_request.return_value.status_code = 200
    hh_api = HeadHunterAPI()
    assert hh_api.connect() == expected_result
    mock_request.assert_called_once_with(
        "https://api.hh.ru",
        headers={"User-Agent": "HH-User-Agent"},
        params={},
    )


@patch("requests.get")
def test_private_connect_invalid(mock_request: MagicMock) -> None:
    """Тестирование, работы приватного запроса API, если выдается не словарь"""
    with pytest.raises(ValueError) as exc_info:
        expected_result = "Error"
        mock_request.return_value.result = expected_result
        mock_request.return_value.status_code = 200
        hh_api = HeadHunterAPI()
        hh_api.connect()
    assert str(exc_info.value) == "API выдает не словарь"
    mock_request.assert_called_once_with(
        "https://api.hh.ru",
        headers={"User-Agent": "HH-User-Agent"},
        params={},
    )


@patch("requests.get")
def test_private_connect_error(mock_request: MagicMock) -> None:
    """Тестирование, работы приватного запроса API с ошибкой статуса"""
    expected_result = "Параметры переданы с ошибкой"
    mock_request.return_value.json.return_value = expected_result
    mock_request.return_value.status_code = 400
    mock_request.return_value.text = expected_result

    hh_api = HeadHunterAPI()

    with pytest.raises(APIError, match=f"Ошибка API: 400 - {expected_result}"):
        hh_api.connect()

    mock_request.assert_called_once_with(
        "https://api.hh.ru",
        headers={"User-Agent": "HH-User-Agent"},
        params={},
    )

@patch("requests.get")
def test_private_request_exception(mock_request: MagicMock) -> None:
    """Тестирование, работы приватного запроса API с ошибкой статуса"""
    expected_result = "Network error"
    mock_request.side_effect = requests.RequestException(expected_result) # имитация ошибки соединения
    hh_api = HeadHunterAPI()
    with pytest.raises(APIError, match=f"Ошибка при запросе: {expected_result}"):
        hh_api.connect()


@patch.object(HHVacanciesAPI, "connect")
def test_get_vacancies_by_employer_id(mock_connect: MagicMock) -> None:
    """Тестирование метода получения вакансий по id работодателя"""
    mock_connect.return_value = {"items": [{"id": "123"}]}
    vacancies_api = HHVacanciesAPI()
    vacancies = vacancies_api.get_vacancies_by_employer_id("12345", 1)
    assert len(vacancies) == 1
    assert vacancies[0]["id"] == "123"
    mock_connect.assert_called_once_with()


@patch.object(HHVacanciesAPI, "connect")
def test_get_vacancies_none_key(mock_connect: MagicMock) -> None:
    """Тестирование метода get_vacancies_by_employer_id при отсутствии данных"""
    mock_connect.return_value = {"error": "error message"}
    vacancies_api = HHVacanciesAPI()
    vacancies = vacancies_api.get_vacancies_by_employer_id("123", 1)
    assert len(vacancies) == 0
    mock_connect.assert_called_once_with()



@patch.object(HHEmployerAPI, "connect")
def test_get_employer_by_id(mock_connect: MagicMock) -> None:
    """"""
    excepted_result = {"id": "123"}
    mock_connect.return_value = excepted_result
    employer_api = HHEmployerAPI()
    employer = employer_api.get_employer_by_id("12345")
    assert employer == excepted_result
    mock_connect.assert_called_once_with()


@patch.object(HHEmployersAPI, "connect")
def test_search_employers_id(mock_connect: MagicMock) -> None:
    """"""
    mock_connect.return_value = {"items": [{"id": "123"}]}
    employers_api = HHEmployersAPI()
    employers = employers_api.search_employers_id("12345")
    assert len(employers) == 1
    mock_connect.assert_called_once_with()





