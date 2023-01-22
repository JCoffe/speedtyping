from tkinter import *
from tkinter import ttk
import random

text_bank = ["this is example text for testing the typing speed of the user it should be a few random paragraphs of text" ,
             "another text to test the writing speed maybe it is ove the average speed of forty words per minute who knows",
             "once upon a time in america there was a dog that went to different houses and looked for treasure especially",
             "the weather will be very nice tomorrow but next week we do not know if the sun will come out or if it will be cloudy",
             "under water there is a completly different world filled with amazing creatures and strange things definatly worth"]

#Starting text
test_text = "this is example text for testing the typing speed of the user it should be a few random paragraphs of text"

#Breaks the text up for comparing and counting
test_text_list = test_text.split()
correct_words_list = []
incorrect_words_list = []
result_list = []
for word in test_text_list:
    result_list.append("False")
timer_text = 0
word_number = 0
timer_running = False

#TODO Timer when user starts typing
def update_timer():
    global timer_text, timer_running
    if timer_running:
        timer_text = timer_text + 1
        timer_label.config(text=f"Time: {timer_text} seconds")
        timer_label.after(1000, update_timer)


#TODO Counter number of words / characters
#TODO Only count correct words
#TODO Display results

def words_entered(event=None):
    global word_number, timer_running, timer_text
# Gets the user input word, strips any spaces before the word, compares the spelling
    if word.get().strip() == test_text_list[word_number]:
        correct_words_list.append(word.get().strip())
    else:
        incorrect_words_list.append(test_text_list[word_number])
#If it is the first word, starts the timer, if its the last word, stops the timer and calculates result
    if word_number == 0:
        timer_running = True
        update_timer()
    elif word_number == len(test_text_list)-1:
        timer_running = False
        minute = timer_text/60
        wpm = int(len(correct_words_list)/minute)
        correct_wordperminute_label.config(text="You typed " + str(wpm) + " words per minute!")
        word_entry.config(state="disabled")


    word_number = word_number + 1
    word.set("")
    resulttext_label_correct.config(text=correct_words_list, background="green")
    resulttext_label_incorrect.config(text=incorrect_words_list, background="red")

#Resets and randomly chooses new text
def reset():
    global word_number, timer_text, correct_words_list, incorrect_words_list, test_text_list, timer_running
    timer_running = False
    word_number = 0
    timer_text = 0
    correct_words_list = []
    incorrect_words_list = []
    text = random.choice(text_bank)
    test_text_list = text.split()
    text_label.config(text=text)
    word_entry.config(state="enabled")
    resulttext_label_correct.config(text="")
    resulttext_label_incorrect.config(text="")
    timer_label.config(text="Time: 0 seconds")

#GUI
root = Tk()
root.title("Speedtype")
root.minsize(300, 400)

mainframe = ttk.Frame(root, padding="10 10 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

info_label = ttk.Label(mainframe, text="Welcome to try your typing speed!! \n\n  Can you beat the avarege speed of 40 words per minute? Start writing in the entry below, hit space after each word. Correctly spelled words will aprear in green, wrongly spelled words in red. Only green words will count. \n \n \n Text to write:", wraplength=250)
info_label.grid(row=0, column=0, pady=5, padx=20, sticky="N")

text_label = ttk.Label(mainframe, text=test_text, wraplength=200, background="white")
text_label.grid(row=1, column=0, pady=5, padx=20)

timer_label = ttk.Label(mainframe, text="Time: 0 seconds")
timer_label.grid(row=2, column=0, pady=5, padx=20)

timer_label.after(1000, update_timer)

word = StringVar()

word_entry = ttk.Entry(mainframe, textvariable=word)
word_entry.grid(row=3, column=0, pady=5, padx=20)
word_entry.bind("<space>", words_entered)

resulttext_label_correct = ttk.Label(mainframe, text="Correct words will appear here", wraplength=200, background="green")
resulttext_label_correct.grid(row=4, column=0, pady=10, padx=20)

resulttext_label_incorrect = ttk.Label(mainframe, text="Incorrect words will appear here", wraplength=200, background="red")
resulttext_label_incorrect.grid(row=5, column=0, pady=10, padx=20)

correct_wordperminute_label = ttk.Label(mainframe, text="Your result will appear here", wraplength=200)
correct_wordperminute_label.grid(row=6, column=0, pady=10, padx=20)


restart_button = ttk.Button(mainframe, text="Reset", command=reset)
restart_button.grid(row=7, column=0, padx=20)


root.mainloop()

