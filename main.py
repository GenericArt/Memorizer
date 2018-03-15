import sqlite3, os, gettext, csv

from random import choice, shuffle
from tkinter import *
from tkinter import font

import core.database_manager as dbManager
import core.setup_defaults as setupDefaults

import guis.game_screen as gameScreen
import guis.welcome_screen as welcomeScreen


# gettext.bindtextdomain('myapplication', 'language')




class Memorizer(Frame):
	"""docstring for Memorizer"""
	def __init__(self, master = None):
		Frame.__init__(self, master)

		langSel = "kor"

		self.master = master
		self.dbPath = "core/main.db"

		self.defaultVerseTable = ""
		self.decoyWordsTable = ""
		if langSel == "kor":
			self.defaultVerseTable = "DefaultKorean"
		else:
			self.defaultVerseTable = "DefaultEnglish"

		if langSel == "kor":
			pass
		else:
			self.decoyWordsTable = "DecoyWords"

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
		
		selectedVerse = dbManager.getAVerse(self.dbPath)
		decoyWords1 = dbManager.getDecoyWords(self.dbPath)
		decoyWords2 = dbManager.getDecoyWords(self.dbPath)
		decoyWords3 = dbManager.getDecoyWords(self.dbPath)

		allAnswers = [selectedVerse[x] for x in ["answer1","answer2","answer3"]]

		while [x for y in decoyWords1 for x in allAnswers if y in x]:
			decoyWords1 = dbManager.getDecoyWords(self.dbPath)
		while [x for y in decoyWords1 for x in allAnswers if y in x]:
			decoyWords2 = dbManager.getDecoyWords(self.dbPath)
		while [x for y in decoyWords1 for x in allAnswers if y in x]:
			decoyWords3 = dbManager.getDecoyWords(self.dbPath)

		print(selectedVerse)
		print(allAnswers)

		decoyWords1.append(selectedVerse["answer1"])
		shuffle(decoyWords1)
		decoyWords2.append(selectedVerse["answer2"])
		shuffle(decoyWords2)
		decoyWords3.append(selectedVerse["answer3"])
		shuffle(decoyWords3)

		allDecoyWordDict = {"decoy1":decoyWords1, "decoy2":decoyWords2, "decoy3":decoyWords3}

		gameScreen.multi_choise_screen(self, root, selectedVerse, allDecoyWordDict)



	def verseCheckAnswer(self, userAnswers, selectedVerse):
		
		answerOne = userAnswers["answer1"].get()
		answerTwo = userAnswers["answer2"].get()
		answerThree = userAnswers["answer3"].get()


		if answerOne == selectedVerse["answer1"] and answerTwo == selectedVerse["answer2"] and answerThree == selectedVerse["answer3"]:
			print("Answer is Correct!!")
		else:
			print("Sorry, please try again...")







if __name__ == '__main__':
	root = Tk()
	root.geometry("500x600")
	root.title("Memorizer")
	app = Memorizer(root)
	root.mainloop()