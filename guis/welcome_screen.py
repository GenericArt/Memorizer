from tkinter import *


def welcome_screen(self, root):

	wlc_frame = Frame(root)
	wlc_frame.grid(row=0, column=0, sticky=N+S+W+E)
	wlc_frame.grid_rowconfigure(1, weight=1)
	wlc_frame.grid_columnconfigure(0, weight=1)
	wlc_frame.isgridded = True

	# create all of the main containers
	top_frame = Frame(wlc_frame, width=450, height=180, pady=100)
	center_frame = Frame(wlc_frame, width=50, height=50, padx=3, pady=10)
	btm_frame = Frame(wlc_frame, width=450, height=45, pady=40)

	# define grid/row/columns behaviour
	top_frame.grid(row=0, sticky="nsew")
	center_frame.grid(row=1, sticky="nsew")
	btm_frame.grid(row=3, sticky="ew")

	center_frame.grid_columnconfigure(1, weight=1)
	center_frame.grid_columnconfigure(2, weight=1)
	center_frame.grid_columnconfigure(3, weight=1)

	top_frame.grid_columnconfigure(2, weight=1)
	top_frame.grid_rowconfigure(0, weight=1)

	btm_frame.grid_columnconfigure(2, weight=1)

	# create labels
	wlcLabelText = "Welcome! Please choose a game mode!"
	wlcLabelOptionText = "To change difficulty or add your own verses use the option button"
	
	wlcInstructLabel = Label(top_frame, text=wlcLabelText)
	wlcInstructLabel.grid(row=1, column=2, sticky=W+E)
	wlcInstructLabel.config(font=self.font)

	wlcOptionLabel = Label(top_frame, text=wlcLabelOptionText)
	wlcOptionLabel.grid(row=2, column=2, sticky=W+E)


	# create buttons
	vmemBtn = Button(center_frame, text='Verse Quest', width=12, height=2, 
						command=self.verseQuestWindow)
	vmemBtn.grid(row=1, column=1)

	storyBtn = Button(center_frame, text='Story Mode', width=12, height=2, command=None)
	storyBtn.grid(row=1, column=2)

	moodBtn = Button(center_frame, text='Mood Booster', width=12, height=2, command=None)
	moodBtn.grid(row=1, column=3)

	optBtn = Button(btm_frame, text='Options', width=12, height=2, command=None)
	optBtn.grid(row=1, column=2)


