from random import shuffle
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('trainer.ui', self)
        self.pushButton.clicked.connect(self.check_word)
        self.pushButton_2.clicked.connect(self.start_void)
        self.started = False
        self.max_lenn = 15
        self.radio_buttons = [
            self.radioButton,
            self.radioButton_2,
            self.radioButton_3,
            self.radioButton_4,
            self.radioButton_5,
            self.radioButton_6,
            self.radioButton_7,
            self.radioButton_8,
            self.radioButton_9,
            self.radioButton_10,
            self.radioButton_11,
            self.radioButton_12,
            self.radioButton_13,
            self.radioButton_14,
            self.radioButton_15
        ]
        self.labels = [
            self.label,
            self.label_2,
            self.label_3,
            self.label_4,
            self.label_5,
            self.label_6,
            self.label_7,
            self.label_8,
            self.label_9,
            self.label_10,
            self.label_11,
            self.label_12,
            self.label_13,
            self.label_14,
            self.label_15
        ]
        self.write_word("вероисповедание")

    def start_void(self):
        self.started = True
        with open("бд.txt", encoding="utf-8") as f:
            reader = f.read().strip().split()
            self.total_len = len(reader)
            shuffle(reader)
        self.reader = reader
        self.current_ind = 0
        self.write_word(self.reader[self.current_ind].lower())

    def write_verdict(self, words):
        self.label_18.setText(words)

    def check_word(self):
        if not self.started:
            self.write_verdict('Нажмите "Начать"')
            return
        for i, button in enumerate(self.radio_buttons):
            if button.isChecked():
                try:
                    if self.reader[self.current_ind][i].isupper():
                        self.write_verdict("Правильно!")
                    else:
                        self.write_verdict(f"Неправильно! Правильно - {self.reader[self.current_ind]}")
                        text = self.plainTextEdit.toPlainText()
                        text += self.reader[self.current_ind] + '\n'
                        self.plainTextEdit.setPlainText(text)
                        parsing = self.label_17.text().split(' ')
                        parsing[-1] = str(int(parsing[-1]) + 1)
                        self.label_17.setText(' '.join(parsing))
                    self.current_ind += 1
                    if self.current_ind == self.total_len:
                        self.write_verdict('Конец')
                        self.write_word('Конец')
                    else:
                        self.write_word(self.reader[self.current_ind].lower())
                    self.progressBar.setValue(int(self.current_ind / self.total_len * 100))
                except:
                    self.write_verdict("Вы делаете что-то не так!")
                    pass

    def write_word(self, word):
        lenn = len(word)
        for i in range(self.max_lenn):
            if i < lenn:
                self.labels[i].setText(word[i])
            else:
                self.labels[i].setText(' ')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
