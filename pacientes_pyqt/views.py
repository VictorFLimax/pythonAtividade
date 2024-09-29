from PyQt5.QtWidgets import QMainWindow, QDialog, QPushButton, QHBoxLayout, QWidget, QTableWidget, QVBoxLayout, QLabel, \
    QLineEdit, QComboBox, QDateEdit, QSpacerItem, QSizePolicy


class ListagemPaciente(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Listagem de pacientes')
        self.setGeometry(50, 50, 500, 400)

        self.botao_cadastrar = QPushButton('Cadastrar')
        self.botao_cadastrar.clicked.connect(self.cadastrar_paciente)

        self.botao_atualizar = QPushButton('Atualizar')

        layout_botoes = QHBoxLayout()
        layout_botoes.addWidget(self.botao_cadastrar)
        layout_botoes.addWidget(self.botao_atualizar)

        painel_botoes = QWidget(self)
        painel_botoes.setLayout(layout_botoes)

        self.tabela_pacientes = QTableWidget()
        self.tabela_pacientes.setColumnCount(4)
        self.tabela_pacientes.setHorizontalHeaderLabels(['Nome', 'Data de nascimento', 'Sexo', 'Carteira do SUS'])
        self.tabela_pacientes.setRowCount(0)

        layout_tabela = QVBoxLayout()
        layout_tabela.addWidget(self.tabela_pacientes)

        painel_tabela = QWidget(self)
        painel_tabela.setLayout(layout_tabela)

        layout_principal = QVBoxLayout()
        layout_principal.addWidget(painel_botoes)
        layout_principal.addWidget(painel_tabela)

        painel_principal = QWidget(self)
        painel_principal.setLayout(layout_principal)

        self.setCentralWidget(painel_principal)

    def cadastrar_paciente(self):
        cadastro = CadastroPaciente(self)
        cadastro.show()


class CadastroPaciente(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle('Cadastro de paciente')
        self.setGeometry(50, 50, 500, 400)

        self.rotulo_nome = QLabel('Nome')
        self.nome = QLineEdit(self)

        self.rotulo_sexo = QLabel('Sexo')
        self.sexo = QComboBox(self)

        self.rotulo_nascimento = QLabel('Data de nascimento')
        self.nascimento = QDateEdit(self)

        self.rotulo_carteira_sus = QLabel('Carteira do SUS')
        self.carteira_sus = QLineEdit(self)

        self.botao_salvar = QPushButton('Salvar')

        space = QSpacerItem(0, 0, QSizePolicy.Fixed, QSizePolicy.Expanding)

        layout_componentes = QVBoxLayout()
        layout_componentes.addWidget(self.rotulo_nome)
        layout_componentes.addWidget(self.nome)
        layout_componentes.addWidget(self.rotulo_sexo)
        layout_componentes.addWidget(self.sexo)
        layout_componentes.addWidget(self.rotulo_nascimento)
        layout_componentes.addWidget(self.nascimento)
        layout_componentes.addWidget(self.rotulo_carteira_sus)
        layout_componentes.addWidget(self.carteira_sus)
        layout_componentes.addWidget(self.botao_salvar)
        layout_componentes.addItem(space)

        self.setLayout(layout_componentes)
