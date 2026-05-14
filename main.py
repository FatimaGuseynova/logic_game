from tkinter import *
import pygame

window = Tk()
window.title('Logic quiz')

label = Label(text='''
    Добро пожаловать в логическую викторину!
    В игре всего 5 заданий, каждый из которых
    оценивается на 1 балл. В конце викторины
    Вы сможете получить ответы на все вопросы
    и свой конечный счет
    У вас есть всего одна попытка, чтобы ответить на вопрос.
    Удачи!''', font="Arial 24", fg='#316879')
label.config(bd=30)
label.pack()
def sound():
    pygame.init()
    pygame.mixer.music.load('najatie-na-kompyuternuyu-knopku1.wav')
    pygame.mixer.music.play(0)
    window.destroy()
but = Button(window, text="Начать викторину", width=40, height=2, command=sound, fg='#4B4B4B')
but.pack(side='bottom')
x = (window.winfo_screenwidth() - window.winfo_reqwidth()) / 4
y = (window.winfo_screenheight() - window.winfo_reqheight()) / 5
window.wm_geometry("+%d+%d" % (x, y))
window.geometry('800x450')
window.mainloop()

# 1 window
window = Tk()
window.title('Logic quiz')
label = Label(text='''Телефон вместе с чехлом стоит 110 долларов. Телефон дороже чехла на 100 долларов.
    Сколько стоит чехол на телефон?''', font="Arial 21", fg='#316879')
label.config(bd=30)
label.pack()

label1 = Label(text="Первый вопрос", font="Arial 19", width=80, height=2, fg='#316879')
label1.config(bg='#ced7d8')
label1.pack()

global score
score = 0


def close_window():
    pygame.init()
    pygame.mixer.music.load('ES_Multimedia 781 - SFX Producer.mp3')
    pygame.mixer.music.play(0)
    but['state'] = 'disabled'
    but1['state'] = 'disabled'
    but2['state'] = 'disabled'
    but3['state'] = 'disabled'
    global score
    score += 1
    scoreLabel.config(text='''
    Ваши баллы: ''' + str(score), fg='#4B4B4B', font='Arial 17')
    label = Label(text='''
    Верно
    ''', font="Arial 19", fg='#7fe7dc')
    label.pack()
    def sound():
        pygame.init()
        pygame.mixer.music.load('najatie-na-kompyuternuyu-knopku1.wav')
        pygame.mixer.music.play(0)
        window.destroy()
    buttun = Button(window, text="Перейти к следующему вопросу", width=40, height=2, command=sound,
                    fg='#4B4B4B')
    buttun.pack(pady=5, padx=100)


def close_window1():
    pygame.init()
    pygame.mixer.music.load('ES_MM Error 23 - SFX Producer.mp3')
    pygame.mixer.music.play(0)
    but['state'] = 'disabled'
    but1['state'] = 'disabled'
    but2['state'] = 'disabled'
    but3['state'] = 'disabled'
    label = Label(text='''Неверно''', font="Arial 19", fg='#f47a60')
    label.config(bd=30)
    label.pack()
    scoreLabel.config(text='''
    Ваши баллы: ''' + str(score), fg='#4B4B4B', font='Arial 17')
    def sound():
        pygame.init()
        pygame.mixer.music.load('najatie-na-kompyuternuyu-knopku1.wav')
        pygame.mixer.music.play(0)
        window.destroy()
    buttun = Button(window, text="Перейти к следующему вопросу", width=40, height=2, command=sound,
                    fg='#4B4B4B')
    buttun.pack(pady=5, padx=100)


scoreLabel = Label(window, text='''
    Ваши баллы: ''' + str(score), fg='#4B4B4B', font='Arial 17')
scoreLabel.pack()
label.config(bd=50)

but = Button(window, text="10", width=40, height=2, command=close_window1, fg='#4B4B4B')
but.pack(side='bottom')
but1 = Button(window, text="5", width=40, height=2, command=close_window, fg='#4B4B4B')
but1.pack(side='bottom')
but2 = Button(window, text="100", width=40, height=2, command=close_window1, fg='#4B4B4B')
but2.pack(side='bottom')
but3 = Button(window, text="200", width=40, height=2, command=close_window1, fg='#4B4B4B')
but3.pack(side='bottom')

x = (window.winfo_screenwidth() - window.winfo_reqwidth()) / 10
y = (window.winfo_screenheight() - window.winfo_reqheight()) / 15
window.wm_geometry("+%d+%d" % (x, y))
window.geometry('950x650')
window.mainloop()

# 2 window
window = Tk()
window.title('Logic quiz')
label = Label(text='''Запишите восемь восьмерок таким образом, чтобы в сумме получилась тысяча.
    Какой вариант верный? ''', font="Arial 21", fg='#316879')
label.config(bd=30)
label.pack()

label1 = Label(text="Второй вопрос", font="Arial 19", width=80, height=2, fg='#316879')
label1.config(bg="#ced7d8")
label1.pack()


def close_window():
    pygame.init()
    pygame.mixer.music.load('ES_Multimedia 781 - SFX Producer.mp3')
    pygame.mixer.music.play(0)
    but['state'] = 'disabled'
    but1['state'] = 'disabled'
    but2['state'] = 'disabled'
    but3['state'] = 'disabled'
    global score
    score += 1
    scoreLabel.config(text='''
    Ваши баллы: ''' + str(score), fg='#4B4B4B', font='Arial 17')
    label = Label(text='Верно', font="Arial 19", fg='#7fe7dc')
    label.config(bd=30)
    label.pack()
    def sound():
        pygame.init()
        pygame.mixer.music.load('najatie-na-kompyuternuyu-knopku1.wav')
        pygame.mixer.music.play(0)
        window.destroy()
    buttun = Button(window, text="Перейти к следующему вопросу", width=40, height=2, command=sound,
                    fg='#4B4B4B')
    buttun.pack(pady=5, padx=100)


def close_window1():
    pygame.init()
    pygame.mixer.music.load('ES_MM Error 23 - SFX Producer.mp3')
    pygame.mixer.music.play(0)
    but['state'] = 'disabled'
    but1['state'] = 'disabled'
    but2['state'] = 'disabled'
    but3['state'] = 'disabled'
    label = Label(text='Неверно', font="Arial 19", fg='#f47a60')
    label.config(bd=30)
    label.pack()
    scoreLabel.config(text='''
    Ваши баллы: ''' + str(score), fg='#4B4B4B', font='Arial 17')
    def sound():
        pygame.init()
        pygame.mixer.music.load('najatie-na-kompyuternuyu-knopku1.wav')
        pygame.mixer.music.play(0)
        window.destroy()
    buttun = Button(window, text="Перейти к следующему вопросу", width=40, height=2, command=sound,
                    fg='#4B4B4B')
    buttun.pack(pady=5, padx=100)


scoreLabel = Label(window, text='''
    Ваши баллы: ''' + str(score), fg='#4B4B4B', font='Arial 17')
scoreLabel.pack()
label.config(bd=30)

but = Button(window, text="888 + 88 + 8 + 8 + 8 + 8", width=40, height=2, command=close_window1, fg='#4B4B4B')
but.pack(side='bottom')
but1 = Button(window, text="88 + 88 + 888 + 8", width=40, height=2, command=close_window1, fg='#4B4B4B')
but1.pack(side='bottom')
but2 = Button(window, text="888 + 88 + 8 + 8 + 8", width=40, height=2, command=close_window, fg='#4B4B4B')
but2.pack(side='bottom')
but3 = Button(window, text="888 + 88 + 8 - 8 + 8 + 8", width=40, height=2, command=close_window1, fg='#4B4B4B')
but3.pack(side='bottom')

x = (window.winfo_screenwidth() - window.winfo_reqwidth()) / 10
y = (window.winfo_screenheight() - window.winfo_reqheight()) / 15
window.wm_geometry("+%d+%d" % (x, y))
window.geometry('950x650')
window.mainloop()

# 3 window
window = Tk()
window.title('Logic quiz')
label = Label(text='''Суммарный возраст членов семьи из 4 человек равняется 68, а 4 года назад равнялся 53.
    Сколько лет младшему члену семьи? ''', font="Arial 21", fg='#316879')
label.config(bd=30)
label.pack()

label1 = Label(text="Третий вопрос", font="Arial 19", width=80, height=2, fg='#316879')
label1.config(bg="#ced7d8")
label1.pack()


def close_window():
    pygame.init()
    pygame.mixer.music.load('ES_Multimedia 781 - SFX Producer.mp3')
    pygame.mixer.music.play(0)
    but['state'] = 'disabled'
    but1['state'] = 'disabled'
    but2['state'] = 'disabled'
    but3['state'] = 'disabled'
    global score
    score += 1
    scoreLabel.config(text='''
    Ваши баллы: ''' + str(score), fg='#4B4B4B', font='Arial 17')
    label = Label(text='Верно', font="Arial 19", fg='#7fe7dc')
    label.config(bd=30)
    label.pack()
    def sound():
        pygame.init()
        pygame.mixer.music.load('najatie-na-kompyuternuyu-knopku1.wav')
        pygame.mixer.music.play(0)
        window.destroy()
    buttun = Button(window, text="Перейти к следующему вопросу", width=40, height=2, command=sound,
                    fg='#4B4B4B')
    buttun.pack(pady=5, padx=100)


def close_window1():
    pygame.init()
    pygame.mixer.music.load('ES_MM Error 23 - SFX Producer.mp3')
    pygame.mixer.music.play(0)
    but['state'] = 'disabled'
    but1['state'] = 'disabled'
    but2['state'] = 'disabled'
    but3['state'] = 'disabled'
    scoreLabel.config(text='''
    Ваши баллы: ''' + str(score), fg='#4B4B4B', font='Arial 17')
    label = Label(text='Неверно', font="Arial 19", fg='#f47a60')
    label.config(bd=30)
    label.pack()
    def sound():
        pygame.init()
        pygame.mixer.music.load('najatie-na-kompyuternuyu-knopku1.wav')
        pygame.mixer.music.play(0)
        window.destroy()
    buttun = Button(window, text="Перейти к следующему вопросу", width=40, height=2, command=sound,
                    fg='#4B4B4B')
    buttun.pack(pady=5, padx=100)


scoreLabel = Label(window, text='''
    Ваши баллы: ''' + str(score), fg='#4B4B4B', font='Arial 17')
scoreLabel.pack()
label.config(bd=30)

but = Button(window, text="2", width=40, height=2, command=close_window1, fg='#4B4B4B')
but.pack(side='bottom')
but1 = Button(window, text="3", width=40, height=2, command=close_window, fg='#4B4B4B')
but1.pack(side='bottom')
but2 = Button(window, text="4", width=40, height=2, command=close_window1, fg='#4B4B4B')
but2.pack(side='bottom')
but3 = Button(window, text="6", width=40, height=2, command=close_window1, fg='#4B4B4B')
but3.pack(side='bottom')

x = (window.winfo_screenwidth() - window.winfo_reqwidth()) / 10
y = (window.winfo_screenheight() - window.winfo_reqheight()) / 15
window.wm_geometry("+%d+%d" % (x, y))
window.geometry('950x650')
window.mainloop()

# 4 window
window = Tk()
window.title('Logic quiz')
label = Label(text='''Министры иностранных дел России, США и Китая обсудили за закрытыми дверями проекты соглашения о
    полном разоружении, представленные каждой из стран. Отвечая затем на вопрос журналистов:
    "Чей именно проект был принят?", министры дали такие ответы:

    Россия — "Проект не наш, проект не США";
    США — "Проект не России, проект Китая";
    Китай — "Проект не наш, проект России".
    Один из них (самый откровенный) оба раза говорил правду; второй (самый скрытный) оба раза говорил
    неправду, третий (осторожный) один раз сказал правду, а другой раз — неправду.

    Определите, представителями каких стран являются откровенный, скрытный и осторожный министры ''',
              font="Arial 19", fg='#316879')
label.config(bd=30)
label.pack()

label1 = Label(text="Четвертый вопрос", font="Arial 19", width=80, height=2, fg='#316879')
label1.config(bg="#ced7d8")
label1.pack()


def close_window():
    pygame.init()
    pygame.mixer.music.load('ES_Multimedia 781 - SFX Producer.mp3')
    pygame.mixer.music.play(0)
    but['state'] = 'disabled'
    but1['state'] = 'disabled'
    but2['state'] = 'disabled'
    but3['state'] = 'disabled'
    global score
    score += 1
    scoreLabel.config(text='''
    Ваши баллы: ''' + str(score), fg='#4B4B4B', font='Arial 17')
    label = Label(text='Верно', font="Arial 19", fg='#7fe7dc')
    label.config(bd=30)
    label.pack()
    def sound():
        pygame.init()
        pygame.mixer.music.load('najatie-na-kompyuternuyu-knopku1.wav')
        pygame.mixer.music.play(0)
        window.destroy()
    buttun = Button(window, text="Перейти к следующему вопросу", width=40, height=2, command=sound,
                    fg='#4B4B4B')
    buttun.pack(pady=5, padx=100)


def close_window1():
    pygame.init()
    pygame.mixer.music.load('ES_MM Error 23 - SFX Producer.mp3')
    pygame.mixer.music.play(0)
    but['state'] = 'disabled'
    but1['state'] = 'disabled'
    but2['state'] = 'disabled'
    but3['state'] = 'disabled'
    scoreLabel.config(text='''
    Ваши баллы: ''' + str(score), fg='#4B4B4B', font='Arial 17')
    label = Label(text='Неверно', font="Arial 19", fg='#f47a60')
    label.config(bd=30)
    label.pack()
    def sound():
        pygame.init()
        pygame.mixer.music.load('najatie-na-kompyuternuyu-knopku1.wav')
        pygame.mixer.music.play(0)
        window.destroy()
    buttun = Button(window, text="Перейти к следующему вопросу", width=40, height=2, command=sound, fg='#4B4B4B')
    buttun.pack(pady=5, padx=100)


scoreLabel = Label(window, text='''
    Ваши баллы: ''' + str(score), fg='#4B4B4B', font='Arial 17')
scoreLabel.pack()
label.config(bd=20)

but = Button(window, text="Китай, США, Россия", width=40, height=2, command=close_window, fg='#4B4B4B')
but.pack(side='bottom')
but1 = Button(window, text="Китай, Россия, США", width=40, height=2, command=close_window1, fg='#4B4B4B')
but1.pack(side='bottom')
but2 = Button(window, text="Россия, США, Китай", width=40, height=2, command=close_window1, fg='#4B4B4B')
but2.pack(side='bottom')
but3 = Button(window, text="США, Китай, Россия", width=40, height=2, command=close_window1, fg='#4B4B4B')
but3.pack(side='bottom')

x = (window.winfo_screenwidth() - window.winfo_reqwidth()) / 10
y = (window.winfo_screenheight() - window.winfo_reqheight()) / 15
window.wm_geometry("+%d+%d" % (x, y))
window.geometry('950x650')
window.mainloop()

# 5 window
window = Tk()
window.title('Logic quiz')
label = Label(text='''Двоих программистов вывезли на кладбище бандиты из девяностых. Бандиты тайно выбрали 2 целых
    положительных числа, оба больше единицы, а их сумма меньше 100. Первому программисту бандит сказал
    произведение этих чисел, а второму — их сумму. После этого у программистов состоялся такой разговор.

    Первый: Я понятия не имею, какая у тебя сумма.

    Второй: Ха-ха, это для меня не новость! Я и так знал, что ты не знал этого.

    Первый: Ага! Теперь я понял, чему равна твоя сумма!

    Второй: Отлично — теперь и я тоже знаю твоё произведение!
    Какие это числа? ''', font="Arial 18", fg='#316879')
label.config(bd=30)
label.pack()

label1 = Label(text="Пятый вопрос", font="Arial 19", width=80, height=2, fg='#316879')
label1.config(bg="#ced7d8")
label1.pack()


def close_window():
    pygame.init()
    pygame.mixer.music.load('ES_Multimedia 781 - SFX Producer.mp3')
    pygame.mixer.music.play(0)
    but['state'] = 'disabled'
    but1['state'] = 'disabled'
    but2['state'] = 'disabled'
    but3['state'] = 'disabled'
    global score
    score += 1
    scoreLabel.config(text='''Ваши баллы: ''' + str(score), fg='#4B4B4B', font='Arial 17')
    label = Label(text='Верно', font="Arial 19", fg='#7fe7dc')
    label.config(bd=30)
    label.pack()
    def sound():
        pygame.init()
        pygame.mixer.music.load('najatie-na-kompyuternuyu-knopku1.wav')
        pygame.mixer.music.play(0)
        window.destroy()
    buttun = Button(window, text="Перейти к следующему вопросу", width=40, height=2, command=sound,
                    fg='#4B4B4B')
    buttun.pack(pady=5, padx=100)


def close_window1():
    pygame.init()
    pygame.mixer.music.load('ES_MM Error 23 - SFX Producer.mp3')
    pygame.mixer.music.play(0)
    but['state'] = 'disabled'
    but1['state'] = 'disabled'
    but2['state'] = 'disabled'
    but3['state'] = 'disabled'
    scoreLabel.config(text='''Ваши баллы: ''' + str(score), fg='#4B4B4B', font='Arial 17')
    label = Label(text='Неверно', font="Arial 19", fg='#f47a60')
    label.config(bd=30)
    label.pack()
    def sound():
        pygame.init()
        pygame.mixer.music.load('najatie-na-kompyuternuyu-knopku1.wav')
        pygame.mixer.music.play(0)
        window.destroy()
    buttun = Button(window, text="Перейти к следующему вопросу", width=40, height=2, command=sound,
                    fg='#4B4B4B')
    buttun.pack(pady=5, padx=100)

scoreLabel = Label(window, text='''Ваши баллы: ''' + str(score), fg='#4B4B4B', font='Arial 17')
scoreLabel.pack()
label.config(bd=30)

but = Button(window, text="4 и 7", width=40, height=2, command=close_window1, fg='#4B4B4B')
but.pack(side='bottom')
but1 = Button(window, text="5 и 12", width=40, height=2, command=close_window1, fg='#4B4B4B')
but1.pack(side='bottom')
but2 = Button(window, text="2 и 9", width=40, height=2, command=close_window1, fg='#4B4B4B')
but2.pack(side='bottom')
but3 = Button(window, text="4 и 13", width=40, height=2, command=close_window, fg='#4B4B4B')
but3.pack(side='bottom')

x = (window.winfo_screenwidth() - window.winfo_reqwidth()) / 10
y = (window.winfo_screenheight() - window.winfo_reqheight()) / 15
window.wm_geometry("+%d+%d" % (x, y))
window.geometry('950x650')
window.mainloop()

# explanation for  questions
window = Tk()
window.title('Logic quiz')
label = Label(text='''Если нужны объяснения, нажмите на вопрос, который вызвал у вас затруднения''', font="Arial 21",
              fg='#316879')
label.config(bd=30)
label.pack()
scoreLabel = Label(text="Ваш конечный балл: " + str(score), font="Arial 19", width=70, height=2, fg='#4B4B4B')
scoreLabel.config(bg='#93D554')
scoreLabel.pack()


def close_window4():
    pygame.init()
    pygame.mixer.music.load('najatie-na-kompyuternuyu-knopku1.wav')
    pygame.mixer.music.play(0)
    window = Tk()
    window.title('Logic quiz')
    button['state'] = 'disabled'
    label = Label(window, text='''Пусть стоимость телефона т($); стоимость чехла - ч($). И далее всё по условию:
        ч + т = 110$;
        т - ч = 100$. Вычитая одно уравнение (второе) из первого сразу находится решение.
        ч + т - (ч - т) = 2 * ч = 110$ - 100$ = 10$;
        Тогда стоимость чехла равна:
        ч = 10$/2 = 5$.''', font="Arial 21", fg='#316879')
    label.config(bd=30)
    label.pack()


def close_window3():
    pygame.init()
    pygame.mixer.music.load('najatie-na-kompyuternuyu-knopku1.wav')
    pygame.mixer.music.play(0)
    window = Tk()
    window.title('Logic quiz')
    but3['state'] = 'disabled'
    label = Label(window,
                  text='''В 1 сумма равна 992; 2- 1072; 3- 1000; в 4 равна 1000, но нужна сумма из-за этого подходит 3 вариант''',
                  font="Arial 21", fg='#316879')
    label.config(bd=30)
    label.pack()


def close_window2():
    pygame.init()
    pygame.mixer.music.load('najatie-na-kompyuternuyu-knopku1.wav')
    pygame.mixer.music.play(0)
    window = Tk()
    window.title('Logic quiz')
    but2['state'] = 'disabled'
    label = Label(window, text='''В начале нужно выяснить сколько было членов семьи 4 года назад для этого нужно
        64-4*4=52, что меньше, чем дано в условии следовательно 4 года назад было 3 члена семьи
        68-4*3=56
        56- общий возраст членов семьи 4 года назад + возраст нового члена семьи. Новому члену семьи 56-53=3 года''',
                  font="Arial 21", fg='#316879')
    label.config(bd=30)
    label.pack()


def close_window2a():
    pygame.init()
    pygame.mixer.music.load('najatie-na-kompyuternuyu-knopku1.wav')
    pygame.mixer.music.play(0)
    window = Tk()
    window.title('Logic quiz')
    but2a['state'] = 'disabled'
    label = Label(window, text='''1) Предположим, что Россия оба раза говорила правду и выходит, что был принят проект
        Китая, но тогда получается, что и США оба раза сказали правду,  а это противоречит условию
        2) Предположим, что Россия оба раза говорила неправду, получается полное противоречие, т.к. в этом случае был
        принят проект и России и США
        3) Предположим, что Россия в 1-ом случае сказала неправду, а во втором правду, тогда получится, что принят проект
        России, а не США, тогда США оба раза сказали неправду, а Китай - оба раза правду, следовательно:
        Россия-осторожный министр; США-скрытный министр; Китай-откровенный министр  Ответ: Китай, США, Россия''',
                  font="Arial 21", fg='#316879')
    label.config(bd=30)
    label.pack()


def close_window2b():
    pygame.init()
    pygame.mixer.music.load('najatie-na-kompyuternuyu-knopku1.wav')
    pygame.mixer.music.play(0)
    but2b['state'] = 'disabled'
    from tkscrolledframe import ScrolledFrame
    root = Tk()
    root.geometry('1250x750')
    root.title('Logic quiz')
    frame_top = Frame(root, width=400, height=250)
    frame_top.pack(side="top", expand=1, fill="both")
    sf = ScrolledFrame(frame_top, width=380, height=240)
    sf.pack(side="top", expand=1, fill="both")
    sf.bind_arrow_keys(frame_top)
    sf.bind_scroll_wheel(frame_top)
    frame = sf.display_widget(Frame)
    l = Label(frame, text='''Для решения нам понадобится вспомнить, что такое простые числа и в чём их особенность. Простое число — то, которое может делиться нацело только на себя и на единицу.

        Например, число 5 — простое, потому что делится только на 5 и на 1. А число 6 — не простое, потому что кроме 6 и 1 оно ещё делится на 2 и 3 без остатка.

        Семь тоже будет простым числом, а восемь — нет, потому что кроме 8 и 1 оно делится также на 2 и 4.

        Если перемножить два простых числа, то полученное произведение больше никак нельзя получить другим способом (кроме умножения этого же числа на единицу).

        Поясним на примере. Возьмём два простых числа 5 и 7 и перемножим их — получится 35. Больше число 35 получить никак не получится, кроме как умножить 35 на 1.

        Это значит, что если произведение можно разложить на два простых множителя, то других вариантов разложения (кроме числа и единицы) у него не будет.

        Это нам пригодится при решении задач — и если число можно разложить на 2 простых, то и их сумму тоже легко сразу посчитать.

        Ещё пример:

        54 = 2 × 27

        54 = 3 × 18

        54 = 6 × 9, а это значит, что число 54 нельзя получить перемножением двух простых чисел и нельзя сразу сказать, чему однозначно равна сумма множителей.

        И ещё:

        21 = 3 × 7

        Оба числа простые, поэтому произведение 21 можно получить только из них, а значит, легко посчитать сумму — она будет равна 3 + 7 = 10.

        Теперь переведём их диалог на язык математики и логики и обозначим числа как n и m:

        Первый: Я понял, что одно из чисел точно не простое, потому что иначе я сразу бы разложил число на произведение двух простых и легко получил сумму.
        А раз так, то это одно из чисел m или n можно получить перемножением двух других чисел.
        Поэтому общее произведение состоит не менее чем из трёх множителей, причём как минимум один из них отличается от остальных — поэтому получается
        несколько вариантов возможных сумм, и я не знаю, какая из них правильная (пометим это как Правило 1).

        Второй: Сумму, которая у меня есть, нельзя получить из двух простых чисел, поэтому и твоё произведение тоже нельзя разложить на два простых множителя.
        Это значит, что у меня нечётная сумма, потому что, по гипотезе Гольдбаха, в нашем случае можно получить любое чётное число, сложив два простых.
        А раз это не два простых числа, значит, и сумма будет нечётная. А ещё эта сумма точно не равна сумме двух и простого числа, потому что два — тоже простое, ха!
        Поэтому есть несколько вариантов суммы m и n, которые подходят под твои условия, но я не могу пока определить, какие именно (пометим это как Правило 2).

        Первый: Из всех множителей моего произведения я могу составить только один вариант пары, сумма которой подойдёт под твоё ограничение — не будет разбиваться
        на сумму двух простых или сумму чисел одного множителя (Правило 3).

        Второй: Ах вот как! Из всех вариантов пар, на которые можно разбить сумму и подходящих под твои условия, есть только одна,
        которая позволила бы тебе определить это (Правило 4). Теперь и мне понятно, что это за числа!

        Теперь подберём варианты суммы, которая была у второго. Ограничения такие:
        нечётная;
        не равна сумме двойки и простого числа.
        1 — не подходит, потому что оба числа больше единицы.
        2, 4, 6, 8… — нет, потому что чётные.
        3 — нет, потому что это сумма двойки и простого числа.
        5 — нет, по той же причине (2 + 3).
        7 — тоже нет (2 + 5).
        9 — тоже нет (2 + 7, а 7 — простое число).
        11 — подходит
        13 — нет, потому что 13 = 2 + 11 (11 — простое число).
        15 — нет, потому что 15 = 2 + 13 (13 — тоже простое число).
        17 — подходит.
        19 — нет, потому что 19 = 2 + 17 (17 — простое число).

        Способ подбора суммы понятен, дальше можно продолжать по тому же алгоритму.
        Мы же выберем те, которые нам уже подошли, и на их примере покажем, что нужно делать дальше, чтобы получить правильный ответ.
        Наши числа, которые нам подходят уже сейчас: 11 и 17. Начнём с 11.

        Сумма = 11.

        Найдём все слагаемые, которые могут давать эту сумму:

        2 + 9
        3 + 8
        4 + 7
        5 + 6

        Для каждого из них запишем произведение и проверим, выполняется ли Правило 3, которое сказал первый программист.

        Смотрим на произведение 2 × 9 = 18 и как ещё его можно получить.

        18 = 2 × 9 → Да (Правило 3 выполняется).

        18 = 3 × 6 → Нет (Правило 3 не работает, потому что 3 + 6 = 9, а 9 можно получить из простых чисел 2 и 7).

        Смотрим на произведение 3 × 8 = 24.

        24 = 2 × 12 → Нет (чётная сумма, Правило 2 не работает).

        24 = 3 × 8 → Да (выполняется Правило 3).

        24 = 6 × 4 → Нет (чётная сумма).

        Смотрим на произведение 4 × 7 = 28.

        28 = 2 × 14 → Нет (чётная сумма).

        28 = 4 × 7 → Да (выполняется Правило 3).

        Смотрим на произведение 5 × 6 = 30.

        30 = 2 × 15 → Да.

        30 = 3 × 10 → Нет (Правило 3 не работает, потому что 3 + 10 = 13, а 13 можно получить суммой простых чисел 2 и 11).

        30 = 5 × 6 → Да.

        Тут мы вообще не можем выбрать одну пару, потому что Правило 3 выполняется 2 раза, а значит, этот вариант отбрасываем.

        Получается, что для суммы 11 могут быть три варианта произведений, для которых выполняется Правило 3: 2 и 9, 3 и 8, 4 и 7. Но тогда

        Правило 4 не выполняется, потому что нужно, чтобы для одной суммы была только одна пара, которая подходит под правило 3. Продолжаем искать.

        Сумма = 17.

        Найдём все слагаемые, которые могут давать эту сумму:

        2 + 15
        3 + 14
        4 + 13
        5 + 12
        6 + 11
        7 + 10
        8 + 9

        Для каждого из них запишем произведение и проверим, выполняется ли Правило 3, которое сказал первый программист.

        Смотрим на произведение 2 × 15 = 30 и как ещё его можно получить.

        30 = 2 × 15 → Да.

        30 = 3 × 10 → Нет (Правило 3 не работает, потому что 3 + 10 = 13, а 13 можно получить суммой простых чисел 2 и 11).

        30 = 5 × 6 → Да.

        Тут мы вообще не можем выбрать одну пару, потому что Правило 3 выполняется 2 раза, а значит, этот вариант отбрасываем.

        Смотрим на произведение 3 × 14 = 42 и как ещё его можно получить:

        42 = 2 × 21 → Да.

        42 = 3 × 14 → Да.

        42 = 6 × 7 → Нет.

        Два раза выполняется Правило 3 — отбрасываем пару.

        Смотрим на произведение 4 × 13 = 52 и как ещё его можно получить.

        52 = 2 × 26 → Нет.

        52 = 4 × 13 → Да.

        Смотрим на произведение 5 × 12 = 60 и как ещё его можно получить.

        60 = 2 × 30 → Нет.

        60 = 3 × 20 → Да.

        60 = 5 × 12 → Да.

        60 = 6 × 10 → Нет.

        Два раза выполняется Правило 3 — отбрасываем пару.

        Смотрим на произведение 6 × 11 = 66 и как ещё его можно получить.

        66 = 2 × 33 → Да.

        66 = 3 × 22 → Нет.

        66 = 6 × 11 → Да.

        Два раза выполняется Правило 3 — отбрасываем пару.

        Смотрим на произведение 7 × 10 = 70 и как ещё его можно получить.

        70 = 2 × 35 → Да.

        70 = 5 × 14 → Нет.

        70 = 7 × 10 → Да.

        Два раза выполняется Правило 3 — отбрасываем пару.

        Смотрим на произведение 8 × 9 = 72 и как ещё его можно получить.

        72 = 2 × 36 → Нет.

        72 = 3 × 24 → Да.

        72 = 4 × 18 → Нет.

        72 = 6 × 12 → Нет.

        72 = 8 × 9 → Да.

        Два раза выполняется Правило 3 — отбрасываем пару.

        Получается, что для суммы 17 может быть только один вариант произведения, для которого выполняется Правило 3: это 4 и 13.

        А значит, что Правило 4 тоже выполняется и мы нашли нужные числа! ''', font="Arial 15")
    l.pack()
    root.mainloop()


button = Button(window, text="Вопрос про телефон и чехол", width=80, height=2, command=close_window4, fg='#4B4B4B')
button.pack(side='bottom')
but3 = Button(window, text="Вопрос про сумму восьмерок равная 1000", width=80, height=2, command=close_window3,
              fg='#4B4B4B')
but3.pack(side='bottom')
but2 = Button(window, text="Вопрос про суммарный возраст членов семьи, где нужно найти возраст младшего", width=80,
              height=2, command=close_window2, fg='#4B4B4B')
but2.pack(side='bottom')
but2a = Button(window, text="Вопрос про министров иностранных дел России, США и Китая", width=80, height=2,
               command=close_window2a, fg='#4B4B4B')
but2a.pack(side='bottom')
but2b = Button(window, text="Вопрос про программистов и выдуманные числа бандита",
               width=80, height=2, command=close_window2b, fg='#4B4B4B')
but2b.pack(side='bottom')

x = (window.winfo_screenwidth() - window.winfo_reqwidth()) / 10
y = (window.winfo_screenheight() - window.winfo_reqheight()) / 15
window.wm_geometry("+%d+%d" % (x, y))
window.geometry('950x650')
window.mainloop()

# end of the quiz
window = Tk()
window.title('Logic quiz')
label = Label(window, text='''
   Спасибо за участие в моей игре!
   Надеюсь вам понравилось!''', font='Arial 24', fg='#316879')
label.config(bd=30)
label.pack()
x = (window.winfo_screenwidth() - window.winfo_reqwidth()) / 4
y = (window.winfo_screenheight() - window.winfo_reqheight()) / 5
window.wm_geometry('+%d+%d' % (x, y))
window.geometry('400x300')
window.mainloop()