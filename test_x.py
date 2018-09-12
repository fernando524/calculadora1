import pytest

from app import soma, subtracao, multiplicacao


def test_soma():
	assert soma(2,2) == 4
	assert soma('2','2') == 4
	
def test_subtracao():
	assert subtracao(5,2) == 3
def test_multiplicacao():
	assert multiplicacao(5,2) == 10

