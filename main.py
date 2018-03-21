import os, sys

from random import choice, shuffle
from tkinter import *
from tkinter import font, messagebox
from pprint import pprint

import core.database_manager as dbManager
import core.setup_defaults as setupDefaults

import guis.welcome_screen as welcomeScreen
import guis.game_screen as gameScreen
import guis.quiz_game_screen as quizScreen
import guis.moodverses_screen as moodScreen
import guis.moodverses_subscreen as moodSubScreen




class Memorizer(Frame):
    """docstring for Memorizer"""
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.dbPath = "core/main.db"


        # Create Database if not Exists
        if not os.path.isfile("core/main.db"):
            print("DB did not exist")
            setupDefaults.setup()

        # Select Language
        self.verseTable = ""
        self.decoyWordsTable = ""
        self.questionsTable = ""
        self.verseRowIDs = []
        self.questionRowIDs = []
        self.moodTypes = []
        self.languageSelection()

        # Setup master grid
        root.grid_rowconfigure(1,weight=1)
        root.grid_columnconfigure(0, weight=1)

        self.font = font.Font(family="helvetica", size=24)
        welcomeScreen.welcome_screen(self, root)


    def languageSelection(self):
        # Temp Variable
        langSel = "eng"

        if langSel == "kor":
            self.verseTable = "DefaultKorean"
            self.verseRowIDs = dbManager.getNumberOfRows(self.dbPath, self.verseTable)
        else:
            self.verseTable = "DefaultEnglish"
            self.questionsTable = "QuizQuestions"
            self.moodBoosterTable = "MoodVerses"
            self.verseRowIDs = dbManager.getNumberOfRows(self.dbPath, self.verseTable)
            self.questionRowIDs = dbManager.getNumberOfRows(self.dbPath, self.questionsTable)
            self.decoyWordsTable = "DecoyWords"
            self.moodTypes = dbManager.getDistinctValuesFromColumn(self.dbPath, "category", self.moodBoosterTable)


    def screenSwitcher(self, screenName):

        if screenName == "home":
            welcomeScreen.welcome_screen(self, root)
        elif screenName == "moodbooster":
            moodScreen.showMoodsScreen(self, root, self.moodTypes)
        elif screenName == "moodsubscreen":
            moodScreen.showMoodsScreen(self, root, self.moodTypes)


    def moodTypeSelection(self, mood):

        self.moodVersesDict = dbManager.getAllRowsContainingThis(self.dbPath, self.moodBoosterTable, "category", mood)
        moodSubScreen.show_subscreen(self, root, self.moodVersesDict)


    def onMoodVerseSelected(self, passedObj):
        w = passedObj.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        print('You selected item %d: "%s"' % (index, value))
        # pprint(self.moodVersesDict)
        self.verseLabel['text'] = self.moodVersesDict[value]['verse']



    def verseQuestStart(self):

        if not self.verseRowIDs:
            self.verseRowIDs = dbManager.getNumberOfRows(self.dbPath, self.verseTable)

        rowID = choice(self.verseRowIDs)

        selectedVerse = dbManager.getARow(self.dbPath, self.verseTable, rowID)
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
            self.verseRowIDs.remove(selectedVerse['row_id'])
            self.verseQuestStart()
        else:
            print("Sorry, please try again...")
            messagebox.showinfo("Incorrect", "Sorry, please try again!")


    def quizQuestionsStart(self):

        if not self.questionRowIDs:
            self.questionRowIDs = dbManager.getNumberOfRows(self.dbPath, self.questionsTable)

        rowID = choice(self.questionRowIDs)

        selectedQuestion = dbManager.getARow(self.dbPath, self.questionsTable, rowID)
        pprint(selectedQuestion)
        quizScreen.gameScreen(self, root, selectedQuestion)


    def quizCheckAnswer(self, userAnswerVar, selectedQuestion):

        userAnswer = userAnswerVar.get()
        correctAnswer = selectedQuestion['answer']

        if userAnswer == correctAnswer:
            print("Quiz Answer Correct!")
            self.quizQuestionsStart()
        else:
            print("Sorry, please try again...")
            messagebox.showinfo("Incorrect", "Sorry, please try again!")




if __name__ == '__main__':
    root = Tk()
    root.geometry("500x600")
    root.title("Memorizer")
    app = Memorizer(root)
    root.mainloop()