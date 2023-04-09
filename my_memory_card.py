from PyQt5.QtCore import Qt
from PyQt5.QtCore import QApplication, Qwidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton
from random import shuffle

app = QApplication([])

window = QWidget() 
window.setWindowTitle('Memo Card')

RadioGroup = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QradioButton('Смурфы')
rbtn_3 = QRadioButton('Чулымцы')
rbtn_4 = QRadioButton('Алеуты')
layout_ans1 = QHBoxLayout()
layout_ans2 = QHBoxLayout()
layout_ans3 = QHBoxLayout()

layout_ans2.addwidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)  

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question, aligment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget((RadioGroupBox))

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)

window.setLayout(layout_card)
window.show()
app.exec()

def ask(question, right_answer, wrong1, wrong2, wrong3):
    btn_OK = QPushButton('Ответить')
    lb_Question = QLabel('Самый сложный вопрос в мире!')

    RadioGroupBox = QGroupBox('Варианты ответов')
    rbtn_1 = QRadioButton('Энцы')
    rbtn_2 = QradioButton('Смурфы')
    rbtn_3 = QRadioButton('Чулымцы')
    rbtn_4 = QRadioButton('Алеуты')
    layout_ans1 = QHBoxLayout()
    layout_ans2 = QHBoxLayout()
    layout_ans3 = QHBoxLayout()

    layout_ans2.addwidget(rbtn_1)
    layout_ans2.addWidget(rbtn_2)
    layout_ans3.addWidget(rbtn_3)
    layout_ans3.addWidget(rbtn_4)
    layout_ans1.addLayout(layout_ans2)
    layout_ans1.addLayout(layout_ans3)

    RadioGroupBox.setLayout(layout_ans1)  

    layout_line1 = QHBoxLayout()
    layout_line2 = QHBoxLayout()
    layout_line3 = QHBoxLayout()

    layout_line1.addWidget(lb_Question, aligment=(Qt.AlignHCenter | Qt.AlignVCenter))
    layout_line2.addWidget((RadioGroupBox))

    layout_line3.addStretch(1)
    layout_line3.addWidget(btn_OK, stretch=2)
    layout_line3.addStretch(1)
 
    window.setLayout(layout_card)
    window.show()
    app.exec()

    AnsGroupBox = QGroupox('Результат теста')
    lbResult = QLabel('прав ты или нет?')
    lb_Correct = QLabel('ответ будет тут!')

    layout_line1 = QHBoxLayout(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
    layout_line2.addWidget(RadioGroupBox)
    layout_line2.addWidget(AnsGroupBox)
    AnsGroupBox.hide()

    layout_line3.addStretch(1)
    layout_line3.addWidget(btn_OK, stretch=2)
    layout_line3.addStretch(1)

    layout_card = QVBoxLayout()

    layout_card.addLayout(lauout_line1, stretch=1)
    layout_card.addLayout(layout_line2, stretch=2)
    layout_card.addStretch(1)
    layout_card.addLayout(layout_line3, stretch=1)
    layout_card.addStretch(1)
    layout_card.setSpacing(5)

class Questions():
    'содержит вопрос, правильный ответ и три неправильных'
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

app = QApplication([])

btn_OK = QPushButton('Ответить')
lb_Question = QLabel('Самый сложный вопрос в мире!')

RadioGroupBox = QGroupBox('Варианты ответов')

rbtn_1 = QRadioButton('Вариант 1')
rbtn_1 = QRadioButton('Вариант 2')
rbtn_1 = QRadioButton('Вариант 3')
rbtn_1 = QRadioButton('Вариант 4')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QHBoxLayout()
layout_ans3 = QHBoxLayout()
layout_ans2.addWidget(rbtn1)
layout_ans2.addWidget(rbtn2)
layout_ans2.addWidget(rbtn3)
layout_ans2.addWidget(rbtn4)

RadioGroupBox.setLayout(layout_ans1)  

AnsGroupBox = QGroupBox('Результат теста')
lb_Result = QLabel('прав ты или нет')
lb_Correct = QLabel('ответ будет тут!')

lauout_res = QVBoxLayout()
layout_res.addWidget(lb_Resuit, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

questions_list = []
question_list.append(
    Question('Государственный язык Бразилии','Португальский','Английский','Испанский','Бразльский'))
question_list.append(
    Question('Какого цвета нет на флаге?','Зелёный','Белый','Красный','Синий'))

def ask(q:Question):
    '''Функция записывает значения вопроса и ответов в соответствующие виджеты, при этом варианты ответов распределяются случайным образом'''
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)

def show_correct(res):
    '''показетель результат - установим ответ в надпись 'результат' и покажем нужную панель'''

def next_question():
    '''задает случайный вопрос из списка'''
    wind.total += 1
    print('Статистика\n-Всего вопрос: ', window.total, '\n-Правильных ответов: ', windows.score)
    cur_question = randint(0, len(questions_list) - 1)

    q = questions_list[cur_question]
    ask(q)

def click_OK():
    '''определяет,надо ли показывать другой вопрос либо проверить ответ на этот'''
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()
