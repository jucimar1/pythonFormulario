from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
import sys

from numpy import double
from qtpy import uic
import sqlite3


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        self.tela = uic.loadUi('listar_dados.ui', self)
        self.tela2 = uic.loadUi('formulario.ui',self)

        self.button = self.findChild(QtWidgets.QPushButton, "pushButton")
        self.button.clicked.connect(self.listar)

        self.button2 = self.findChild(QtWidgets.QPushButton, "pushButton_salvar")
        self.button2.clicked.connect(self.salvar_dados)


        print("escrever o nome")
        self.input1 = self.findChild(QtWidgets.QLineEdit,'lineEdit_nome')
        print("escrever o valor")
        self.input2 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_valor')
        valor =0

        self.show()

    def salvar_dados(self):
        nome = self.tela2.input1.text()
        print("recebeu o nome")
        valor1 = (self.tela2.input2.text())
        print( "recebeu o valor")
        valor = (valor1)
        print("converteu o valor em double")





        try:
            banco = sqlite3.connect('banco_cadastro.db ')
            cursor = banco.cursor()

            # cursor.execute("Create TABLE IF NOT EXISTS tabela1 (nome text, valor numeric")
            print("inserir os valores")
            cursor.execute("INSERT INTO tabela1 (nome,valor) VALUES ('"+nome+"' ,'"+valor+"')")
            print("banco recebeu os valores")
            banco.commit()
            banco.close()
            # self.tela2.lineEdit_nome.setText("")
            # self.tela2.lineEdit_valor.setText("")
            print("dados inseridos")
        except sqlite3.Error as erro:
            print("Aconteceu alguma coisa o erro esta: ",  erro)

    def listar(self):
        print("ok")
        self.tela.show()
        banco = sqlite3.connect('banco_cadastro.db ')
        cursor = banco.cursor()

        # cursor.execute("Create TABLE IF NOT EXISTS tabela1( nome text, valor numeric)")
        # cursor.execute("INSERT INTO tabela1 (nome, valor) Values('careca',300.22) ")

        cursor.execute("SELECT * FROM tabela1 ")
        dados_lidos = cursor.fetchall()
        self.tela.tableWidget.setRowCount(len(dados_lidos))
        self.tela.tableWidget.setColumnCount(3)
        print("foi contado quantidade")

        for i in range(0, len(dados_lidos)):
            for j in range(0,3):
                self.tela.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
        banco.close()

    #
    # def printButtonPressed(self):
    #     valor = (self.input.text())
    #     resultado = int(valor) + 8
    #     print('Ole o olá')
    #     print("Agora sim o resultado : ",resultado)


app = QtWidgets.QApplication(sys.argv)
window = Ui()
window.show()
app.exec_()




