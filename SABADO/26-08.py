# -*- coding: utf-8 -*-

################################################################################
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QDoubleValidator, QIntValidator
from PyQt5.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox, QLabel, QLineEdit, QWidget)
class ExemploLineEdit(QWidget):
    def __init__(self):
        super(ExemploLineEdit, self).__init__()
        self.setWindowTitle("Exemplo QLineEdit e QComboBox")
        self.criarGrupoSenha()
        self.criarGrupoValidacao()
        self.criarGrupoAlinhamento()
        self.criarGrupoMascara()
        self.criarGrupoEdicao()
        self.definirLayoutTela()
        self.definirEventos()