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

