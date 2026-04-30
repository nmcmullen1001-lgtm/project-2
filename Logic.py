import csv
from PyQt6.QtWidgets import QMainWindow
from GUI import *

class Logic(QMainWindow, Ui_mainWindow):
    def __init__(self):
        """
        This function hides the scores and their labels, creates the self.check variable, and guides what happens when
        a button is pressed!

        :param self.check: This is a variable that will be used later to decide calculations

        There will be an extra '(' in the params  after the first ')' due to being told unpaired symbol
        :param self.radio_1.clicked.connect(lambda : self.radio1()(): Calls the radio1 def
        :param self.radio_2.clicked.connect(lambda : self.radio2()(): Calls the radio2 def
        :param self.radio_3.clicked.connect(lambda : self.radio3()(): Calls the radio3 def
        :param self.radio_4.clicked.connect(lambda : self.radio4()(): Calls the radio4 def
        :param self.Submit.clicked.connect(lambda : self.submit()():  Calls the submit def
        """
        super().__init__()
        self.setupUi(self)

        self.check: int = 0

        self.lab1.hide()
        self.lab2.hide()
        self.lab3.hide()
        self.lab4.hide()

        self.Score_1.hide()
        self.Score_2.hide()
        self.Score_3.hide()
        self.Score_4.hide()


        self.radio_1.clicked.connect(lambda : self.radio1())
        self.radio_2.clicked.connect(lambda : self.radio2())
        self.radio_3.clicked.connect(lambda : self.radio3())
        self.radio_4.clicked.connect(lambda : self.radio4())
        self.Submit.clicked.connect(lambda : self.submit())

    def radio1(self):
        """
        This function changes the self.check value, shows the first score box, hides the rest,
        clears the inputs in score box 1, and sets the text for scores 2 - 4 as N/A.
        """

        self.lab1.show()
        self.lab2.hide()
        self.lab3.hide()
        self.lab4.hide()

        self.Score_1.show()
        self.Score_2.hide()
        self.Score_3.hide()
        self.Score_4.hide()

        self.check: int = 1


        self.Score_1.setText('')
        self.Score_2.setText('N/A')
        self.Score_3.setText('N/A')
        self.Score_4.setText('N/A')

    def radio2(self):
        """
         This function changes the self.check value, shows the first two score boxes, hides the rest,
        clears the inputs in both scores 1 and 2, and sets the text for scores 3 and 4 as N/A.
        """

        self.lab1.show()
        self.lab2.show()
        self.lab3.hide()
        self.lab4.hide()

        self.Score_1.show()
        self.Score_2.show()
        self.Score_3.hide()
        self.Score_4.hide()

        self.check: int = 2

        self.Score_1.setText('')
        self.Score_2.setText('')
        self.Score_3.setText('N/A')
        self.Score_4.setText('N/A')

    def radio3(self):
        """
        This function changes the self.check value, shows three score boxes, hides the fourth,
        clears the inputs in score boxes 1 - 3, and sets the text for score 4 as N/A
        """
        self.lab1.show()
        self.lab2.show()
        self.lab3.show()
        self.lab4.hide()

        self.Score_1.show()
        self.Score_2.show()
        self.Score_3.show()
        self.Score_4.hide()

        self.check:int = 3

        self.Score_1.setText('')
        self.Score_2.setText('')
        self.Score_3.setText('')
        self.Score_4.setText('N/A')

    def radio4(self):
        """
         This function changes the self.check value, shows all score boxes,
            and clears all the inputs in the score boxes
        """

        self.lab1.show()
        self.lab2.show()
        self.lab3.show()
        self.lab4.show()

        self.Score_1.show()
        self.Score_2.show()
        self.Score_3.show()
        self.Score_4.show()

        self.check:int = 4

        self.Score_1.setText('')
        self.Score_2.setText('')
        self.Score_3.setText('')
        self.Score_4.setText('')


    def submit(self):
        """
        This function converts the data in the student name box into a variable as a string,
        checks if there is nothing the SyntaxError is raised, it then gets checked by the .isalpha(), if it returns
        true nothing happens however if it returns false it raises the SyntaxError to prevent numbers in the name box
        After this it runs through an if elif else loop based on the self.check variable, if no button is pressed it
        raises a timeout error and tells you that you must press a button, if it doesn't raise the exception it does
        calculations based off of the self.check, getting the overall MAD of the score boxes
        that show up and putting it into a variable. After these calculations are done the Avg is checked in a function
        to get a letter grade, after getting the letter grade it puts the name, all four scores, either as a number or
        as N/A, and the average based off of the number of scores you chose with the radio buttons. After all this is
        done it changes the text in the label used for errors / updates to say
        "(name) your score is (percent)% which is a(n) (grade)", finally it unchecks the radio button, clears all boxes,
         sets the focus onto the name, and hides the scores again.

        :raises ValueError: if converting s1 - s4 as an int doesn't work or if the number of s1 - 4 is
        less than 0 or more than 100 if s2 - 4 are currently strings it ignores those.
        :raises SyntaxError: if the name box is empty or if there is a number in the name box this error will occur
        :raises TimeoutError: If there is no radio button selected this error will be raised.

        """

        try:

            name: str = str(self.Student_name.text()).strip()
            if name.isalpha():
                pass
            else:
                raise SyntaxError

            if name == '':
                raise SyntaxError




            if self.check == 1:
                s1: float = float(self.Score_1.text())
                s2: str = str(self.Score_2.text())
                s3: str = str(self.Score_3.text())
                s4: str  = str(self.Score_4.text())
                if s1 < 0:
                    raise ValueError
                elif s1 > 100:
                    raise ValueError
                avg: float = s1 / 1

            elif self.check == 2:
                s1: float = float(self.Score_1.text())
                s2: float = float(self.Score_2.text())
                s3: str = str(self.Score_3.text())
                s4: str = str(self.Score_4.text())

                if s1 < 0:
                    raise ValueError
                elif s1 > 100:
                    raise ValueError

                if s2 < 0:
                    raise ValueError
                elif s2 > 100:
                    raise ValueError
                add: float = s1 + s2
                avg: float = add / 2

            elif self.check == 3:
                s1: float = float(self.Score_1.text())
                s2: float = float(self.Score_2.text())
                s3: float = float(self.Score_3.text())
                s4: str = str(self.Score_4.text())
                if s1 < 0:
                    raise ValueError
                elif s1 > 100:
                    raise ValueError
                if s2 < 0:
                    raise ValueError
                elif s2 > 100:
                    raise ValueError
                if s3 < 0:
                    raise ValueError
                elif s3 > 100:
                    raise ValueError
                add: float = s1 + s2 + s3
                avg: float = add / 3

            elif self.check == 4:
                s1: float = float(self.Score_1.text())
                s2: float = float(self.Score_2.text())
                s3: float = float(self.Score_3.text())
                s4: float = float(self.Score_4.text())

                if s1 < 0:
                    raise ValueError
                elif s1 > 100:
                    raise ValueError
                elif s2 < 0:
                    raise ValueError
                elif s2 > 100:
                    raise ValueError
                elif s3 < 0:
                    raise ValueError
                elif s3 > 100:
                    raise ValueError
                elif s4 < 0:
                    raise ValueError
                elif s4 > 100:
                    raise ValueError
                add: float = s1 + s2 + s3 + s4
                avg: float = add / 4
            else:
                raise TimeoutError

            if avg >= 90.00:
                grade = 'A'
            elif avg >= 80.00:
                grade = 'B'
            elif avg >= 70.00:
                grade = 'C'
            elif avg >= 60.00:
                grade = 'D'
            elif avg < 60.00:
                grade = 'F'
            e:str = f'{avg:.2f}%'
            with open('GPA.csv', 'a', newline='') as GPA:
                content = csv.writer(GPA)
                content.writerow([name, s1, s2, s3, s4, e, grade])



            txt:str = f' {name} your score is {avg:.2f} % which is a(n) {grade}'

            self.error.setText(txt)

            self.Score_1.setText('')
            self.Score_2.setText('')
            self.Score_3.setText('')
            self.Score_4.setText('')
            self.Student_name.setText('')

            self.lab1.hide()
            self.lab2.hide()
            self.lab3.hide()
            self.lab4.hide()

            self.Score_1.hide()
            self.Score_2.hide()
            self.Score_3.hide()
            self.Score_4.hide()

            if self.buttons.checkedButton() is not None:
                self.buttons.setExclusive(False)
                self.buttons.checkedButton().setChecked(False)
                self.buttons.setExclusive(True)
        except TimeoutError:
            self.error.setText('You must select one of the four options!')
        except ValueError:
            self.error.setText('Make sure every score is within range: 0-100')
        except SyntaxError:
            self.error.setText('You need a name!')

        self.Student_name.setFocus()