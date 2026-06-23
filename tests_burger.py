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

