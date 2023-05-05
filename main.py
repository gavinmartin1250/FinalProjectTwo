from controller import *

def main() -> None:
   '''
   Connecting files together
   '''
   app = QApplication([])
   window = Controller()
   window.show()
   app.exec_()


if __name__ == '__main__':
   main()
