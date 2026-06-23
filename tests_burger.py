from unittest.mock import Mock
from praktikum.burger import Burger
import pytest


class TestBurger:

    # Тест на установку булочек
    def test_set_buns(self):
        burger = Burger()
       
        mock_bun = Mock()
        mock_bun.get_name.return_value = "black bun"
        mock_bun.get_price.return_value = 100
        burger.set_buns(mock_bun)
        
        assert burger.bun == mock_bun


    # Тест на добавление одного ингредиента
    def test_add_one_ingredient(self):
        burger = Burger()
        
        mock_ingredient = Mock()
        mock_ingredient.get_name.return_value = 'cutlet'
        mock_ingredient.get_price.return_value = 100
        mock_ingredient.get_type.return_value = 'FILLING'
        
        burger.add_ingredient(mock_ingredient)
        
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient


   # Тест на добавление двух ингредиентов
    def test_add_two_ingredients(self):
        burger = Burger()
        
        mock_filling = Mock()
        mock_sauce = Mock()
                
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        
        assert len(burger.ingredients) == 2


    # Тест на удаление ингредиента 
    def test_remove_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        
        assert len(burger.ingredients) == 0
        assert mock_ingredient not in burger.ingredients


    # Тест на перемещение ингредиента
    @pytest.mark.parametrize("old_idx, new_idx, expected_names", [
        (0, 1, ['chili sauce', 'cutlet']),
        (1, 0, ['chili sauce', 'cutlet']),
        (0, 0, ['cutlet', 'chili sauce']),  # перемещение на ту же позицию
        (1, 1, ['cutlet', 'chili sauce']),  # перемещение на ту же позицию
       ])
    def test_move_ingredient(self, old_idx, new_idx, expected_names):
        burger = Burger()
        
        mock_filling = Mock()
        mock_filling.get_name.return_value = 'cutlet'

        mock_sauce = Mock()
        mock_sauce.get_name.return_value = 'chili sauce'
        
        burger.add_ingredient(mock_filling)
        burger.add_ingredient(mock_sauce)
        
        burger.move_ingredient(old_idx, new_idx)
        
        actual_names = [ingredient.get_name() for ingredient in burger.ingredients]
        
        assert actual_names == expected_names


    # Тест на получение цены бургера
    @pytest.mark.parametrize("bun_price, filling_price, sauce_price", [
        (50, 100, 300), # булочки и два ингредиента
        (20, 50, 0),  # булочки и один ингредиент
        (40, 0, 0),  # только булочки
        (0, 0, 0)   # без булочек и без ингредиентов
        ])
    def test_get_price(self, bun_price, filling_price, sauce_price):
        burger = Burger()
       
        mock_bun = Mock()
        mock_bun.get_price.return_value = bun_price
               
        mock_filling = Mock()
        mock_filling.get_price.return_value = filling_price
        
        mock_sauce = Mock()
        mock_sauce.get_price.return_value = sauce_price
        
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)

        expected_price = bun_price * 2 + filling_price + sauce_price
        assert burger.get_price() == expected_price


    # Тест на получение чека на бургер
    def test_get_receipt_with_bun_and_ingredients(self):
        burger = Burger()

        mock_bun = Mock()
        mock_bun.get_name.return_value = "black bun"
        mock_bun.get_price.return_value = 100.0

        mock_filling = Mock()
        mock_filling.get_name.return_value = "cutlet"
        mock_filling.get_type.return_value = "FILLING"
        mock_filling.get_price.return_value = 100.0

        mock_sauce = Mock()
        mock_sauce.get_name.return_value = "chili sauce"
        mock_sauce.get_type.return_value = "SAUCE"
        mock_sauce.get_price.return_value = 300.0

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_filling)
        burger.add_ingredient(mock_sauce)

        expected_price = 600  # Расчёт: 100*2 + 100 + 300 = 600
        burger.get_price = Mock(return_value=expected_price)

        receipt = burger.get_receipt()
        
        expected_receipt = (
            '(==== black bun ====)',
            '= filling cutlet =',
            '= sauce chili sauce =',
            '(==== black bun ====)\n',
            'Price: 600'
        )

        assert receipt == '\n'.join(expected_receipt)