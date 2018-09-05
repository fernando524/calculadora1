import pytest

from app import soma


def test_soma():
         assert soma(2,2) == 4 
	 assert soma(100,20) == 120 

from app import subtracao

def test_subtracao():
	assert subtracao(5,2) == 3


from app import multiplicacao
def test_multiplicacao():
	assert multiplicacao(5,2) == 10

