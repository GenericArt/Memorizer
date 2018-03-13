from tkinter import *



def multi_choise_screen(self, root):
	pass
	# create welcome frame
	game_frame = Frame(root)
	game_frame.grid(row=0, column=0, sticky=N+S+W+E)
	game_frame.grid_rowconfigure(1, weight=1)
	game_frame.grid_columnconfigure(0, weight=1)
	game_frame.isgridded = True

	# create all of the main containers
	top_frame = Frame(game_frame, bg='red', width=450, height=50, pady=3)
	center = Frame(game_frame, bg='gray2', width=50, height=40, padx=3, pady=3)
	btm_frame = Frame(game_frame, bg='white', width=450, height=45, pady=3)
	btm_frame2 = Frame(game_frame, bg='blue', width=450, height=60, pady=3)



	# layout all of the main containers
	top_frame.grid(row=0, sticky="ew")
	center.grid(row=1, sticky="nsew")
	btm_frame.grid(row=3, sticky="ew")
	btm_frame2.grid(row=4, sticky="ew")

	memBtn = Button(center, text='Verse Quest', width=10, height=5, command=self.setup_start_window)
	memBtn.grid(row=1, column=1)
