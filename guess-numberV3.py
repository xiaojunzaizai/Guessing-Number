import tkinter as tk
import random
import tkinter.font

def set_range():
    global root1
    global min_entry 
    global max_entry

    root1 = tk.Tk(className='选择范围')
    ft = tkinter.font.Font(family='Times New Roman',size='16',weight='bold')
    root1.geometry('150x100+600+300')

    #label
    label_message1 = tk.Label(root1,width='2',font= ft)
    label_message1.config(label_message1,text= '从')

    #entry
    min_entry = tk.Entry(root1,width = '10')

    #label
    label_message2 = tk.Label(root1,width='2',font= ft)
    label_message2.config(label_message2,text= '到')

    #entry
    max_entry = tk.Entry(root1,width='10')

    #button
    yes_bt = tk.Button(root1,text='Yes',width = '5')

    #place
    label_message1.place(x=1,y=5)
    min_entry.place(x=25,y=5)
    label_message2.place(x=1,y=35)
    max_entry.place(x=25,y=35)
    yes_bt.place(x=55,y=70)
    yes_bt.bind('<Button-1>',BtC)
    root1.mainloop()

def BtC(event):
    global max_num
    global min_num
    max_num = int(max_entry.get())
    min_num = int(min_entry.get())
    root1.destroy()


def BtClose(event):
    root.destroy()

def BtGuess(event):
    global number_max
    global number_min
    global running
    global count

    if running:
        if entry_guess.get() =='':
            label_content('请输入数字')
        else:
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

def try_again(event):
    global number 
    global running 
    global count 
    global number_max 
    global number_min
    
    root.destroy()
    set_range()
    number = random.randint(min_num,max_num)
    running = True
    count = 0
    number_max = max_num
    number_min = min_num
    # entry_guess.delete(0,'end')
    # label_content('以重置，请开始('+str(min_num)+'-'+str(max_num)+'之间的整数'+')'+'：')

    guess()


def num_guess():
    if count == 1:
        label_content('厉害！一次就答对')
    elif count<= 10:
        label_content('十次之内就答对了，厉害！您的尝试次数为：' +str(count))
    else:
        label_content('尝试次数超过了10次，继续努力！ 您的尝试次数为：' + str(count))

def label_content(content):
    label_message.config(label_message,text= content)


def guess():
    global label_message
    global entry_guess
    global root

    root = tk.Tk(className='猜数字')
    ft = tkinter.font.Font(family='Times New Roman',size='16',weight='bold')
    root.geometry('400x90+600+300')
    #提示部分
    label_message = tk.Label(root,width='80',font= ft)
    label_message.pack(side = 'top')
    #输入部分
    entry_guess = tk.Entry(root,width='25')
    entry_guess.pack(side='left')
    entry_guess.bind('<Return>',BtGuess)
    #按钮部分
    bt_guess= tk.Button(root,text='Guess',width='5')
    bt_guess.bind('<Button-1>',BtGuess)
    bt_guess.place(x=240,y=47)

    bt_close = tk.Button(root,text='Quit',width='5')
    bt_close.bind('<Button-1>',BtClose)
    bt_close.place(x=340,y=47)

    bt_retry = tk.Button(root,text = 'Retry',width = '5')
    bt_retry.bind('<Button-1>',try_again)
    bt_retry.place(x = 290,y = 47)
    
    label_content('请输入'+str(min_num)+'-'+str(max_num)+'之间的任意整数： ')
    entry_guess.focus_set()
    root.mainloop()




set_range()


number = random.randint(min_num,max_num)
running = True
count = 0
number_max = max_num
number_min = min_num

guess()


# if __name__ == "__main__":
#     root = tk.Tk(className='猜数字')
#     ft = tkinter.font.Font(family='Times New Roman',size='16',weight='bold')
#     root.geometry('400x90+600+300')
#     #提示部分
#     label_message = tk.Label(root,width='80',font= ft)
#     label_message.pack(side = 'top')
#     #输入部分
#     entry_guess = tk.Entry(root,width='25')
#     entry_guess.pack(side='left')
#     entry_guess.bind('<Return>',BtGuess)
#     #按钮部分
#     bt_guess= tk.Button(root,text='Guess',width='5')
#     bt_guess.bind('<Button-1>',BtGuess)
#     bt_guess.place(x=240,y=47)

#     bt_close = tk.Button(root,text='Quit',width='5')
#     bt_close.bind('<Button-1>',BtClose)
#     bt_close.place(x=340,y=47)

#     bt_retry = tk.Button(root,text = 'Retry',width = '5')
#     bt_retry.bind('<Button-1>',try_again)
#     bt_retry.place(x = 290,y = 47)
    
#     label_content('请输入'+str(min_num)+'-'+str(max_num)+'之间的任意整数： ')
#     entry_guess.focus_set()
#     root.mainloop()





















