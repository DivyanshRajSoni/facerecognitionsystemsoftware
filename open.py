import threading
from transformers import AutoModelForCausalLM, AutoTokenizer
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class ChatBot:
    def __init__(self, root):
        self.root = root
        self.root.title("AI ChatBot")
        self.root.geometry("730x620+0+0")
        self.root.bind('<Return>', self.enter_func)
        self.root.wm_iconbitmap("facesc.ico")

        main_frame = Frame(self.root, bd=4, bg='powder blue', width=610)
        main_frame.pack()

        img_chat = Image.open('chat.jpg').resize((200, 70), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img_chat)

        Title_label = Label(main_frame, bd=3, relief=RAISED, anchor='nw', width=730, compound=LEFT,
                            image=self.photoimg, text='AI ChatBot', font=('arial', 30, 'bold'), fg='green', bg='white')
        Title_label.pack(side=TOP)

        self.scroll_y = ttk.Scrollbar(main_frame, orient=VERTICAL)
        self.text = Text(main_frame, width=65, height=20, bd=3, relief=RAISED, font=('arial', 14), yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.text.pack()

        btn_frame = Frame(self.root, bd=4, bg='white', width=730)
        btn_frame.pack()

        label_1 = Label(btn_frame, text="Type something", font=('arial', 14, 'bold'), fg='green', bg='white')
        label_1.grid(row=0, column=0, padx=5, sticky=W)

        self.entry = StringVar()
        self.entry1 = ttk.Entry(btn_frame, textvariable=self.entry, width=40, font=('times new roman', 16, 'bold'))
        self.entry1.grid(row=0, column=1, padx=5, sticky=W)

        self.send = Button(btn_frame, text="Send>>", command=self.send, font=('arial', 16, 'bold'), width=8, bg='green')
        self.send.grid(row=0, column=2, padx=5, sticky=W)

        self.clear_send = Button(btn_frame, text="Clear Data", command=self.clear, font=('arial', 15, 'bold'), width=8, bg='red', fg='white')
        self.clear_send.grid(row=1, column=0, padx=5, sticky=W)

        self.msg = ''
        self.label_11 = Label(btn_frame, text=self.msg, font=('arial', 14, 'bold'), fg='red', bg='white')
        self.label_11.grid(row=1, column=1, padx=5, sticky=W)

    def enter_func(self, event):
        self.send.invoke()
        self.entry.set('')

    def clear(self):
        self.text.delete('1.0', END)
        self.entry.set('')

    def send(self):
        user_input = self.entry.get()
        self.text.insert(END, '\n\t\t\t' + 'You: ' + user_input)
        self.text.yview(END)

        if user_input == '':
            self.msg = 'Please enter some input'
            self.label_11.config(text=self.msg, fg='red')
        else:
            self.msg = ''
            self.label_11.config(text=self.msg, fg='red')

            # Run the model inference in a separate thread
            threading.Thread(target=self.generate_response, args=(user_input,)).start()

    def generate_response(self, prompt):
        inputs = tokenizer.encode(prompt + tokenizer.eos_token, return_tensors='pt')
        outputs = model.generate(inputs, max_length=150, pad_token_id=tokenizer.eos_token_id)
        response = tokenizer.decode(outputs[:, inputs.shape[-1]:][0], skip_special_tokens=True)
        
        # Insert the response into the text widget in the main thread
        self.root.after(0, self.display_response, response)

    def display_response(self, response):
        self.text.insert(END, "\n\n" + "Bot: " + response)
        self.text.yview(END)
        self.entry.set('')  # Clear the entry after sending the message

if __name__ == '__main__':
    # Load the model and tokenizer once
    tokenizer = AutoTokenizer.from_pretrained("gpt2")
    model = AutoModelForCausalLM.from_pretrained("gpt2")

    root = Tk()
    obj = ChatBot(root)
    root.mainloop()


