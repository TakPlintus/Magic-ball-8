from tkinter import *
from random import choice

window = Tk()
window.title('Magic ball 8 v1.1')
window.resizable(False, False)
window.iconbitmap('Data/icon.ico')
c = Canvas(width=600, height=500, bg='darkgrey', highlightthickness=0)
c.pack()

future = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом',
          'Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да', 'Черти говорят - НЕТ!',
          'Да', 'Пока неясно, попробуй снова', 'Спроси позже', 'Не стоит', 'Сейчас нельзя предсказать', 'Спроси опять',
          'Даже не думай', 'Мой ответ - нет', 'По моим данным - нет', 'Перспективы не очень хорошие',
          'Весьма сомнительно', 'POGCHAMP']
COLORS = ['midnight blue', 'red3', 'lime green']
frames_cnt = 36
frames = [PhotoImage(file='Data/space.gif', format='gif -index %i' % i) for i in range(frames_cnt)]


def update(ind):
    frame = frames[ind]
    ind += 1
    if ind == frames_cnt:
        ind = 0
    c.itemconfig(label, image=frame)
    window.after(10, update, ind)


label = c.create_image(250, 250, image=frames[0])
window.after(0, update, 0)


def show_future():
    c.itemconfig(future_text, text=choice(future))
    c.itemconfig(triangle, fill=choice(COLORS))


oval = c.create_oval(225, 69, 375, 220,
                     fill='grey26', outline='grey26', tag='ball')
c.create_oval(245, 79, 355, 190,
              fill='black', outline='gray67', width=2, tag='ball')
triangle = c.create_polygon(260, 167, 300, 85, 340, 167,
                            fill='midnight blue', tag='ball')
c.create_text(300, 135, text='Magic!', fill='white', font=('Segoe Print', 0), tag='ball')
c.create_polygon((200, 340), (240, 280), (360, 280), (400, 340),
                 fill='midnight blue')

c.create_line(-5, 450, 605, 450,
              fill='midnight blue', width=4)
c.create_line(-5, 410, 605, 410,
              fill='midnight blue', width=4)
future_text = c.create_text(30, 430,
                            text='Задайте вопрос и нажмите START', fill='yellow', font=('Segoe Print', 20), anchor=W)

c.create_line(-5, 480, 120, 480,
              fill='midnight blue', width=4)
c.create_line(119, 480, 140, 450,
              fill='midnight blue', width=4)
c.create_text(6, 465,
              text='by TakPlintus', fill='yellow', font=('Segoe Print', 0), anchor=W)

Button(window,
       text='START',
       bg='grey26',
       fg='yellow',
       width=10,
       font=('Times New Roman', 0),
       activebackground='midnight blue',
       activeforeground='white',
       command=show_future
       ).place(x=250, y=290)


def shake(event, direction):  # какой-то bread
    while True:
        window.after(10, c.move('ball', 0, direction))
        window.after(10, c.move(future_text, +2, 0))
        if c.coords(oval)[1] < 40:
            window.after(10, shake(event, +1))
        if c.coords(oval)[1] > 100:
            window.after(10, shake(event, -1))
        if c.coords(future_text)[0] > 610:
            c.move(future_text, -1000, 0)
        c.update()


shake(0, -1)

window.mainloop()
