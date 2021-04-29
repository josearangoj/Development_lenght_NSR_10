import sys
from qt_gui import *
import Functions as fn

class MiFormulario(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.btn_calculate.clicked.connect(self.main_execution)

    def main_execution(self):

        """****************************"PROBLEM CONSTANTS"******************************"""
        fc = float(self.ui.txt_fc.text())  # Concrete Compressive Strength [MPa]
        fy = float(self.ui.txt_fy.text())  # Specified yield strength for rebar reinforcement [MPa]
        sep = float(self.ui.txt_sep.text())  # Spacing of the rebars [m]
        rec = float(self.ui.txt_clear_dist.text()) # Clear cover to face of bar [m]
        hreb = float(self.ui.txt_h_rebar.text()) # Spacing between upside and downside rebars [m]
        confLd = bool(self.ui.radBtn_confined_yes.isChecked())  # Confinement bars along development length? [True or False]
        liwe = bool(self.ui.radBtn_liwe_yes.isChecked())  # Lightweight concrete? [True or False]
        epoxic = bool(self.ui.radBtn_epoxic_yes.isChecked()) # Epoxic coated bars? [True or False]
        "****************************************************************************"

        """****************************+***"EXECUTION"********************************"""
        ld_table = fn.ld_table(liwe, epoxic, hreb, sep, rec, fc, fy, confLd)
        self.ui.result_table.setText(str(ld_table))
        "****************************************************************************"


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    application = MiFormulario()
    application.show()
    sys.exit(app.exec_())
