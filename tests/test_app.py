import unittest
from unittest.mock import patch
from src.app import soma, is_par, cadastro_usuario, cadastro, wellcome

class TestApp(unittest.TestCase):
    
    def test_soma_numeros_positivos(self):
        resultado = soma(2,5)
        self.assertEqual(resultado, 7)

    def test_numero_par(self):
        resultado = is_par(4)
        self.assertTrue(resultado)
    
    def test_numero_impar(self):
        resultado = is_par(3)
        self.assertFalse(resultado)

    def test_cadastro_usuario(self):
        resultado = cadastro_usuario("carlos", "c@gmail.com")
        self.assertEqual(resultado, "sucesso")

    def test_cadastro_usuario_email_existe(self):
        cadastro_usuario("carlos", "c@gmail.com")
        resultado = cadastro_usuario("z", "c@gmail.com")
        self.assertEqual(resultado, "email ja existe")

    @patch("src.app.save", return_value = "ola")
    def test_cadastrar_usuario_valido(self, mock_salvar):
        nome = "Carlos"
        cpf = "213471283"
        resultado = cadastro(nome, cpf)
        self.assertTraue(resultado)
        mock_salvar.assert_called_once_with({'nome':nome, 'cpf':cpf})

    @patch("src.app.send_mail", return_value = True)
    def test_cadastrar_usuario_valido(self, mock_send_mail):
        resultado = wellcome("carlos@gmail.com")
        self.assertEqual(resultado, "emial de boas vindas enviado")
        mock_send_mail.assert_called_once_with("carlos@gmail.com")


if __name__ == '__main__':
    unittest.main()