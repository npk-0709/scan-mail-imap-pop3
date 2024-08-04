"""
 * Author: NGUYEN PHU KHUONG (K.AUTO) 
 * Email: dev.phukhuong0709@hotmail.com
 * Github: npk-0709
 * TELE: @khuongdev79
"""

from ui import *
from class_read_imap import *
import threading


class APP(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)

        self.btnEvent.clicked.connect(lambda: threading.Thread(target=self.run).start())

    def run(self):
        self.btnEvent.setText("ĐANG CHẠY...")
        account = self.account.text()
        limit = self.count.value()
        readmail(account, limit)
        self.btnEvent.setText("Hoàn Thành")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = APP()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
