import sqlite3, os

from random import choice
from tkinter import *
from tkinter import font

import core.database_manager as dbManager
import core.setup_defaults as setupDefaults

import guis.game_screen as gameScreen
import guis.welcome_screen as welcomeScreen



class Memorizer(Frame):
	"""docstring for Memorizer"""
	def __init__(self, master = None):
		Frame.__init__(self, master)
		self.master = master

		if not os.path.isfile("core/main.db"):
			print("DB did not exist")
			setupDefaults.setup()

			


		root.grid_rowconfigure(1, weight=1)
		root.grid_columnconfigure(0, weight=1)


		self.font = font.Font(family="helvetica", size=24)

		welcomeScreen.welcome_screen(self, root)

		# self.setup_start_window()



	def screenSwitcher(self):
				pass		



	def setup_start_window(self):
		print("Running Init Window")

		




	def verseQuestWindow(self):
		
		print("Verse Quest Windows Called")

		gameScreen.multi_choise_screen(self, root)








if __name__ == '__main__':
	root = Tk()
	root.geometry("500x600")
	root.title("Memorizer")
	app = Memorizer(root)
	root.mainloop()