import os, sys
import sqlite3 as lite

#dbFolder = '/Users/Manley/Documents/Python/AtoZee Inspection App/Databases/MasterComments.db'
#dbFil = '/Users/Manley/Documents/Python/AtoZee Inspection App/Databases/MasterComments.db'

class DBManager(object):
	"""
	docstring for DBManager

	Handles all Database Functions
	
	"""


	def getCategoryNames(self, dbFile, Column):

		allNames = []

		con = lite.connect(dbFile)

		with con:

			con.row_factory = lite.Row
			cur = con.cursor()
			#cur.execute("SELECT %s FROM CategoryList" % (Column))
			cur.execute("SELECT * FROM CategoryList")

			rows = cur.fetchall()

			for row in rows:
				thisDict = {row['Title']:row['CategoryID']}
				allNames.append(thisDict)

		con.close()
		return allNames




	def getSubcategoryNames(self, dbFile, catID):
		
		allNames = []

		con = lite.connect(dbFile)

		with con:

			con.row_factory = lite.Row
			cur = con.cursor()
			#cur.execute("SELECT %s FROM CategoryList" % (Column))
			cur.execute("SELECT * FROM SubCategoryList WHERE CategoryID = %s" % (catID))

			rows = cur.fetchall()

			for row in rows:
				thisDict = {row["Title"]:row["SubCategoryID"]}
				allNames.append(thisDict)

		con.close()

		return allNames



	def getSubCatComments(self, dbFile, subCatID):
		
		allComments = []

		con = lite.connect(dbFile)
		print "DB --- ", dbFile, "-----", subCatID
		with con:

			con.row_factory = lite.Row
			cur = con.cursor()
			#cur.execute("SELECT %s FROM CategoryList" % (Column))
			cur.execute("SELECT * FROM Comments WHERE SubCategoryID = %s" % (subCatID))

			rows = cur.fetchall()

			for row in rows:
				
				allComments.append(row["Comment"])

		con.close()

		return allComments


	def getSubCatMaterials(self, dbFile, subCatID):
		
		allMaterials = []

		con = lite.connect(dbFile)

		with con:

			con.row_factory = lite.Row
			cur = con.cursor()
			#cur.execute("SELECT %s FROM CategoryList" % (Column))
			cur.execute("SELECT * FROM Materials WHERE SubCategoryID = %s" % (subCatID))

			rows = cur.fetchall()

			for row in rows:
				
				allMaterials.append(row["Material"])

		con.close()

		return allMaterials



	def insertNewComment(self, dbFile, table, comment, catID, subCatID):
		

		con = lite.connect(dbFile)

		with con:

			con.row_factory = lite.Row
			cur = con.cursor()

			cur.execute("INSERT INTO %s (Comment, CategoryID, SubCategoryID)VALUES(\"%s\", %s, %s)" % ( table, comment, catID, subCatID))

			

		con.close()



	def deleteCommentFromRow(self, dbFile, comment, subCatID):
		

		con = lite.connect(dbFile)
		
		with con:

			con.row_factory = lite.Row
			cur = con.cursor()

			query = "DELETE FROM Comments WHERE Comment=\"%s\" AND SubCategoryID=%s" % (comment , subCatID)

			cur.execute(query)

		con.close()



	def updateCommentRow(self, dbFile, comment, oldComment, subCatID):
		
		con = lite.connect(dbFile)
		
		with con:

			con.row_factory = lite.Row
			cur = con.cursor()

			query = "UPDATE Comments SET Comment=\"%s\" WHERE Comment=\"%s\" AND SubCategoryID=%s" % (comment, oldComment, subCatID)

			cur.execute(query)


		con.close()


	def getRequestCatOrSubTitle(self, dbFile, table, column, theID):
		

		con = lite.connect(dbFile)
		
		with con:

			con.row_factory = lite.Row
			cur = con.cursor()

			query = "SELECT Title FROM %s WHERE %s=%s" % (table, column, theID)
			cur.execute(query)

			name = cur.fetchone()



		con.close()

		return name[0]



	def updateCatTitle(self, dbFile, table, name, catID):
		
		con = lite.connect(dbFile)
		
		with con:

			con.row_factory = lite.Row
			cur = con.cursor()

			query = "UPDATE %s SET Title=\"%s\" WHERE CategoryID=\"%s\"" % (table, name, catID)

			cur.execute(query)


		con.close()


	def updateSubCatTitle(self, dbFile, table, name, catID, subCatID):
		
		con = lite.connect(dbFile)
		
		with con:

			con.row_factory = lite.Row
			cur = con.cursor()

			query = "UPDATE %s SET Title=\"%s\" WHERE CategoryID=\"%s\" AND SubCategoryID=%s" % (table, name, catID, subCatID)

			cur.execute(query)


		con.close()


	def getMaxNumber(self, dbFile, table, column):
		

		con = lite.connect(dbFile)
		
		with con:

			con.row_factory = lite.Row
			cur = con.cursor()

			query = "SELECT MAX(%s) FROM %s" % (column, table)
			cur.execute(query)

			value = cur.fetchone()



		con.close()

		return value[0]


	def addNewCategoryTitle(self, dbFile, title, catID):
		

		con = lite.connect(dbFile)

		with con:

			con.row_factory = lite.Row
			cur = con.cursor()

			cur.execute("INSERT INTO CategoryList (Title, CategoryID)VALUES(\"%s\", %s)" % (title, catID))

			

		con.close()


	def addNewSubCategoryTitle(self, dbFile, title, catID, subCatID):
		

		con = lite.connect(dbFile)

		with con:

			con.row_factory = lite.Row
			cur = con.cursor()

			cur.execute("INSERT INTO SubCategoryList (Title, CategoryID, SubCategoryID)VALUES(\"%s\", %s, %s)" % ( title, catID, subCatID))

			

		con.close()



	def deleteAllCommentsFromSubCategory(self, dbFile, catID, subCatID):
		

		con = lite.connect(dbFile)

		with con:

			con.row_factory = lite.Row
			cur = con.cursor()

			query1 = "DELETE FROM Comments WHERE CategoryID=\"%s\" AND SubCategoryID=%s" % (catID, subCatID)
			query2 = "DELETE FROM SubCategoryList WHERE CategoryID=\"%s\" AND SubCategoryID=%s" % (catID, subCatID)

			cur.execute(query1)
			cur.execute(query2)
			

		con.close()





	def deleteAllCommentsFromCategory(self, dbFile, catID):
		

		con = lite.connect(dbFile)

		with con:

			con.row_factory = lite.Row
			cur = con.cursor()

			query1 = "DELETE FROM Comments WHERE CategoryID=\"%s\"" % (catID)
			query2 = "DELETE FROM SubCategoryList WHERE CategoryID=\"%s\"" % (catID)
			query3 = "DELETE FROM CategoryList WHERE CategoryID=\"%s\"" % (catID)

			cur.execute(query1)
			cur.execute(query2)
			cur.execute(query3)
			

		con.close()





	'''
	def deleteSubOrCatTitle(self, dbFile, table, title, column, ID):
		

		con = lite.connect(dbFile)
		
		with con:

			con.row_factory = lite.Row
			cur = con.cursor()

			query = "DELETE FROM %s WHERE Title=\"%s\" AND %s=%s" % (table, title, column, ID)

			cur.execute(query)

		con.close()
	'''








#DBManager().getCategoryNames(dbFolder, "Title")