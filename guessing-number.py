import tkinter as tk
import random
import tkinter.font

number = random.randint(0,1000)
running = True
count = 0
number_max = 1000
number_min = 0


def BtClose(event):
    root.destroy()

def BtGuess(event):
    global number_max
    global number_min
    global running
    global count

    if running:
        guess_number = int(entry_guess.get())
        if guess_number == number:
            label_content('Congratulation!')
            count +=1
            running = False
            num_guess()

        elif guess_number < number:
            if guess_number> number_min:
                number_min = guess_number
                count +=1
                label_content('小了，请输入'+ str(number_min)+'到'+str(number_max)+'之间的任意整数：')
            else:
                count +=1
                label_content('您输入的数字不在范围内：')
        else:
            if guess_number<= number_max:
                number_max = guess_number
                count +=1
                label_content('大了，请输入'+ str(number_min)+'到'+str(number_max)+'之间的任意整数：')
            else:
                count +=1
                label_content('您输入的数字不在范围内：')
    else:
        label_content('您已经猜对了')

def num_guess():
    if count == 1:
        label_content('厉害！一次就答对')
    elif count<= 10:
        label_content('十次之内就答对了，厉害！您的尝试次数为：' +str(count))
    else:
        label_content('尝试次数超过了10次，继续努力！ 您的尝试次数为：' + str(count))

def label_content(content):
    label_message.config(label_message,text= content)

if __name__ == "__main__":
    root = tk.Tk(className='猜数字')
    ft = tkinter.font.Font(family='Times New Roman',size='16',weight='bold')
    root.geometry('400x90+600+300')
    #提示部分
    label_message = tk.Label(root,width='80',font= ft)
    label_message.pack(side = 'top')
    #输入部分
    entry_guess = tk.Entry(root,width='30')
    entry_guess.pack(side='left')
    entry_guess.bind('<Return>',BtGuess)
    #按钮部分
    bt_guess= tk.Button(root,text='Guess',width='5')
    bt_guess.bind('<Button-1>',BtGuess)
    bt_guess.place(x=285,y=47)

    bt_close = tk.Button(root,text='Quit',width='5')
    bt_close.bind('<Button-1>',BtClose)
    bt_close.place(x=340,y=47)
    label_content('请输入0-1000之间的任意整数： ')
    entry_guess.focus_set()
    root.mainloop()





















