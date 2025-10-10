import pytest
from unittest.mock import Mock
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurgerGetReceipt:
    """Тесты для метода get_receipt класса Burger"""
    
    def test_get_receipt_format_with_ingredients(self, sample_burger, mock_bun, mock_sauce, mock_filling):
        """Тест формата чека с ингредиентами"""
        mock_bun.get_name.return_value = "black bun"
        mock_bun.get_price.return_value = 100
        
        mock_sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_sauce.get_name.return_value = "hot sauce"
        mock_sauce.get_price.return_value = 50
        
        mock_filling.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_filling.get_name.return_value = "cutlet"
        mock_filling.get_price.return_value = 80
        
        sample_burger.set_buns(mock_bun)
        sample_burger.add_ingredient(mock_sauce)
        sample_burger.add_ingredient(mock_filling)
        
        receipt = sample_burger.get_receipt()
        
        # Проверяем основные элементы чека
        lines = receipt.split('\n')
        assert len(lines) == 6  # 2 булочки + 2 ингредиента + пустая строка + цена
        assert "(==== black bun ====)" in lines[0]
        assert "= sauce hot sauce =" in lines[1]
        assert "= filling cutlet =" in lines[2]
        assert "(==== black bun ====)" in lines[3]
        assert lines[4] == ""  # Пустая строка
        assert "Price: 330" in lines[5]  # 100*2 + 50 + 80

    def test_get_receipt_format_only_bun(self, sample_burger, mock_bun):
        """Тест формата чека только с булочкой"""
        mock_bun.get_name.return_value = "white bun"
        mock_bun.get_price.return_value = 200
        
        sample_burger.set_buns(mock_bun)
        
        receipt = sample_burger.get_receipt()
        
        lines = receipt.split('\n')
        assert len(lines) == 4  # 2 булочки + пустая строка + цена
        assert "(==== white bun ====)" in lines[0]
        assert "(==== white bun ====)" in lines[1]
        assert lines[2] == ""  # Пустая строка
        assert "Price: 400" in lines[3]  # 200*2

    def test_get_receipt_no_bun(self, sample_burger):
        """Тест получения чека без булочки (должен упасть с AttributeError)"""
        with pytest.raises(AttributeError):
            sample_burger.get_receipt()

    def test_get_receipt_with_real_objects(self, sample_burger):
        """Тест получения чека с реальными объектами"""
        from praktikum.bun import Bun
        from praktikum.ingredient import Ingredient
        from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
        
        bun = Bun("red bun", 300)
        sauce = Ingredient(INGREDIENT_TYPE_SAUCE, "chili sauce", 300)
        filling = Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 200)
        
        sample_burger.set_buns(bun)
        sample_burger.add_ingredient(sauce)
        sample_burger.add_ingredient(filling)
        
        receipt = sample_burger.get_receipt()
        
        assert "red bun" in receipt
        assert "chili sauce" in receipt
        assert "dinosaur" in receipt
        assert "Price: 1100" in receipt