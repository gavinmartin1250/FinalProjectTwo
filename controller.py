from PyQt5.QtWidgets import *
from scorecard import *


QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)




class Controller(QMainWindow, Ui_MainWindow):
   def __init__(self, *args, **kwargs):
       '''
       Initializing the GUI and connecting the submit button
       '''
       super().__init__(*args, **kwargs)
       self.setupUi(self)
       self.score_button.clicked.connect(lambda: self.submit())


   def submit(self) -> None:
       '''
       gets values from GUI, ensures the correct input, and calculates scores
       '''
       try:
           hole_one = int(self.hole_one.text())
           hole_two = int(self.hole_two.text())
           hole_three = int(self.hole_three.text())
           hole_four = int(self.hole_four.text())
           hole_five = int(self.hole_five.text())
           hole_six = int(self.hole_six.text())
           hole_seven = int(self.hole_seven.text())
           hole_eight = int(self.hole_eight.text())
           hole_nine = int(self.hole_nine.text())
           hole_ten = int(self.hole_ten.text())
           hole_eleven = int(self.hole_11.text())
           hole_twelve = int(self.hole_twelve.text())
           hole_thirteen = int(self.hole_thirteen.text())
           hole_fourteen = int(self.hole_fourteen.text())
           hole_fifteen = int(self.hole_fifteen.text())
           hole_sixteen = int(self.hole_sixteen.text())
           hole_seventeen = int(self.hole_seventeen.text())
           hole_eighteen = int(self.hole_eighteen.text())
           self.invalid.setText('')


       except:
            self.invalid.setText('Invalid Inputs')
            self.plus_minus.setText('')
            self.total_score.setText('')
       else:
           total_score = hole_one + hole_two + hole_three + hole_four + hole_five + hole_six + hole_seven + hole_eight + hole_nine + hole_ten + hole_eleven + hole_twelve + hole_thirteen + hole_fourteen + hole_fifteen + hole_sixteen + hole_seventeen + hole_eighteen
           self.total_score.setText(f'{total_score}')
           if total_score > 72:
               self.plus_minus.setText(f'+{total_score - 72}')
           elif total_score < 72:
               self.plus_minus.setText(f'-{72 - total_score}')
           else:
               self.plus_minus.setText(f'0')

       fairway_counter = 0

       if self.fairway1.isChecked():
           fairway_counter += 1
       if self.fairway2.isChecked():
           fairway_counter += 1
       if self.fairway3.isChecked():
           fairway_counter += 1
       if self.fairway4.isChecked():
           fairway_counter += 1
       if self.fairway5.isChecked():
           fairway_counter += 1
       if self.fairway6.isChecked():
           fairway_counter += 1
       if self.fairway7.isChecked():
           fairway_counter += 1
       if self.fairway8.isChecked():
           fairway_counter += 1
       if self.fairway9.isChecked():
           fairway_counter += 1
       if self.fairway10.isChecked():
           fairway_counter += 1
       if self.fairway11.isChecked():
           fairway_counter += 1
       if self.fairway122.isChecked():
           fairway_counter += 1
       if self.fairway13.isChecked():
           fairway_counter += 1
       if self.fairway14.isChecked():
           fairway_counter += 1
       if self.fairway15.isChecked():
           fairway_counter += 1
       if self.fairway16.isChecked():
           fairway_counter += 1
       if self.fairway17.isChecked():
           fairway_counter += 1
       if self.fairway18.isChecked():
           fairway_counter += 1

       self.fairway_percentage.setText(f'{fairway_counter / 18 * 100:.0f}%')






