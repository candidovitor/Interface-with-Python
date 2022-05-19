from PyQt5 import uic,QtWidgets


def função_principal():
    linha1 = formulario.lineEdit.text()
    linha2 = formulario.lineEdit_2.text()
    linha3 = formulario.lineEdit_3.text()

    if formulario.radioButton.isChecked():
        print('Categoria Brinquedos e jogos foi selecionada')
    elif formulario.radioButton_2.isChecked():
        print('Categoria Casa, Jardim e Limpeza foi selecionada')
    elif formulario.radioButton_3.isChecked():
        print('Categoria Roupas, calçados e acessórios foi selecionada')
    elif formulario.radioButton_4.isChecked():
        print('Categoria Filmes, Séries e Música foi selecionada')
    elif formulario.radioButton_5.isChecked():
        print('Categoria Eletrônicos, Eletrodomésticos e informática foi selecionada')


    print('Código',linha1)
    print('Descrição', linha2)
    print('Preço', linha3)


app=QtWidgets.QApplication([])
formulario=uic.loadUi("formulario.ui")
formulario.pushButton.clicked.connect(função_principal)

formulario.show()
app.exec()