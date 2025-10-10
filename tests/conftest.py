import pytest
from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def sample_burger():
    """Фикстура для создания тестового бургера"""
    from praktikum.burger import Burger
    return Burger()


@pytest.fixture
def mock_bun():
    """Фикстура для мока булочки"""
    mock = Mock(spec=Bun)
    mock.get_name.return_value = "test bun"
    mock.get_price.return_value = 100
    return mock


@pytest.fixture
def mock_sauce():
    """Фикстура для мока соуса"""
    mock = Mock(spec=Ingredient)
    mock.get_name.return_value = "test sauce"
    mock.get_price.return_value = 50
    mock.get_type.return_value = INGREDIENT_TYPE_SAUCE
    return mock


@pytest.fixture
def mock_filling():
    """Фикстура для мока начинки"""
    mock = Mock(spec=Ingredient)
    mock.get_name.return_value = "test filling"
    mock.get_price.return_value = 80
    mock.get_type.return_value = INGREDIENT_TYPE_FILLING
    return mock


@pytest.fixture
def burger_with_ingredients(sample_burger, mock_bun, mock_sauce, mock_filling):
    """Фикстура для бургера с ингредиентами"""
    sample_burger.set_buns(mock_bun)
    sample_burger.add_ingredient(mock_sauce)
    sample_burger.add_ingredient(mock_filling)
    return sample_burger