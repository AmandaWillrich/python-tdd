import pytest
from pytest import mark

from codigo.bytebank import Funcionario


class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        # Given
        entrada = '13/03/2000'
        esperado = 23

        funcionario_teste = Funcionario('Teste', entrada, 1115)
        # when
        resultado = funcionario_teste.idade()

        # then
        assert resultado == esperado

    def test_quando_nome_completo_recebe_Lucas_Carvalho_deve_retornar_Carvalho(self):
        entrada = 'Lucas Carvalho '
        esperado = 'Carvalho'

        lucas = Funcionario(entrada, 11/11/2000, 1111)
        resultado = lucas.sobrenome()

        assert resultado == esperado

    def test_quando_diretor_decrescimo_salario_100000_deve_retornar_90000(self):
        entrada_salario = 100000
        entrada_nome = 'Paulo Silva'
        esperado = 90000

        funcionario1 = Funcionario(entrada_nome, '11/11/2000', entrada_salario)
        funcionario1.decrescimo_salario()
        resultado = funcionario1.salario

        assert resultado == esperado

    # @mark.calcularbonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada_salario = 1000
        esperado = 100

        funcionario2 = Funcionario('Teste', '11/11/2000', entrada_salario)
        resultado = funcionario2.calcular_bonus()

        assert resultado == esperado

    # @mark.calcularbonus
    def test_quando_calcular_bonus_recebe_50000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada_salario = 50000

            funcionario3 = Funcionario('Func', '11/11/2000', entrada_salario)
            resultado = funcionario3.calcular_bonus()

            assert resultado
