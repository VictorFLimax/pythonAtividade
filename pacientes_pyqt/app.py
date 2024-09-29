import sys

from PyQt5.QtWidgets import QApplication

from views import ListagemPaciente

app = QApplication(sys.argv)

listagem_paciente = ListagemPaciente()
listagem_paciente.show()

app.exit(app.exec_())
