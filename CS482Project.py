# Seth Ball
# This is a GUI to access a SQL database

# import statements
import mysql.connector
import time
from mysql.connector import Error
from tkinter import *

# connection to sql database
mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "",
	database = "project1"
	)

# Cursor connection
my_cursor = mydb.cursor()

# global variables 
global InsertString
InsertString = []
global DeleteString
DeleteString = []
global SingleInsertString
SingleInsertString = []
DisplayList = []
TempList = []

# Display will take the query presented and 
# show the table that the query creates
def Display(QUERY):
	my_cursor.execute(QUERY)
	for x in my_cursor:
		DisplayList.append(x)
	DisplayTable()

# Helper to display the table on a new window
def DisplayTable():
	row = 0
	tab = '	'
	temp = ''
	
	# store data in a temp list 
	for x in DisplayList:
		row = row +1
		for item in x:
			temp = temp + str(item) + tab
		
		TempList.append(temp)
		#print(temp)
		temp = ''
	
	# print the temp list on the screen
	for index in TempList:	
		TEXT.insert(END, index)
		TEXT.insert(END, '\n') 

def EraseText():
	QUERY = ''
	DisplayList.clear()
	InsertString.clear()
	TempList.clear()
	Query.delete(0,'end')	
	TEXT.delete(1.0,END)
	TEXT.update()


# InputEntry will take the string inputed in the add window and insert it into the database
def InputEntry():
	Check = Toplevel()
	Check.geometry("110x125")

	ErrorLabel = Label(Check, text = '')
	ErrorLabel.place(x = 10, y = 10)

	try :
		int(NAME.get())
		ErrorLabel.config(text = "Error: Incorect type in Name")
	except :
		InsertString.append(NAME.get())
		#print("name")
		NAME.delete(0,'end')
	
	try:
		int(PLAYERID.get())
		InsertString.append(PLAYERID.get())
		#print("playerid")
		PLAYERID.delete(0,'end')
	except:
		ErrorLabel.config(text = "Error: Incorect type in playerid")

	try:
		int(TEAMNAME.get()) 
		ErrorLabel.config(text = "Error: Incorect type in teamname")
	except:
		InsertString.append(TEAMNAME.get())
		#print("teamname")
		TEAMNAME.delete(0,'end')
		

	try :
		int(POSITION.get())
		ErrorLabel.config(text = "Error: Incorect type in position")
	except :
		InsertString.append(POSITION.get())
		#print("position")
		POSITION.delete(0,'end')

	try:
		int(TOUCHDOWNS.get())	
		InsertString.append(TOUCHDOWNS.get())
		#print("touchdowns")
		TOUCHDOWNS.delete(0,'end')
	except:
		ErrorLabel.config(text = "Error: Incorect type in touchdowns")

	try:
		int(TOTALYARDS.get())
		InsertString.append(TOTALYARDS.get())
		#print("totalyards")
		TOTALYARDS.delete(0,'end')
	except:
		ErrorLabel.config(text = "Error: Incorect type in totalyards")

	try:
		int(SALARY.get())
		InsertString.append(SALARY.get())
		#print("salary")
		SALARY.delete(0,'end')
	except:
		ErrorLabel.config(text = "Error: Incorect type in salary")

	#print(InsertString[0])
	#print(InsertString[1])
	#print(InsertString[2])
	#print(InsertString[3])
	#print(InsertString[4])
	#print(InsertString[5])
	#print(InsertString[6])	
	INPUT = "insert into Players values( \'"+ InsertString[0] + "\' , " + InsertString[1] + ", \'" + InsertString[2] + "\', \'" + InsertString[3] + "\', " + InsertString[4] + ", " + InsertString[5] + ", " + InsertString[6] + ");"
	CheckLabel = Label(Check, text = "Confirm Data Entry?")
	CheckLabel.place(x = 10, y= 10, width = 105, height = 30)
	CheckYes = Button(Check, text = "Yes", command = InsertConfirmed(INPUT))
	CheckYes.place(x = 10, y = 45, width = 105, height = 30)
	CheckNo = Button(Check, text = "No", command = Check.destroy)
	CheckNo.place(x = 10, y = 85, width = 105, height = 30)


# Helper funciton that will insert data into the database
def InsertConfirmed(INSERTED):
	starttime = time.time()
	my_cursor.execute(INSERTED)
	mydb.commit()
	end = time.time() - starttime
	#print(end)
	InsertString.clear()

# records the string that contains the mysql command for deleting and entry based on name and player id
def RemoveEntry():
	Del = Toplevel()
	Del.geometry("200x165")
	ErrorLabel = Label(Del, text = '')
	ErrorLabel.place(x = 10, y = 130)
	#if type(int(DELNAME.get())) == str:
	try :
		int(DELNAME.get())
		ErrorLabel.config(text = "Error: Incorect type in Name")
	except :
		DeleteString.append(DELNAME.get())
		DELNAME.delete(0,'end')

	try : 
		int(DELPLAYERID.get())
		DeleteString.append(DELPLAYERID.get())
		DELPLAYERID.delete(0,'end')
	except:
		ErrorLabel.config(text = "Error: Incorect type in playerID")

	DELETE = "DELETE FROM Players WHERE Name = \'" + DeleteString[0] + "\' and playerID = " + DeleteString[1] + ";"
	#print(DELETE)
	DelLabel = Label(Del, text = "Confirm Data Deletion?")
	DelLabel.place(x = 10, y= 10, width = 155, height = 30)
	DelYes = Button(Del, text = "Yes", command = DeleteConfirmed(DELETE))
	DelYes.place(x = 10, y = 45, width = 105, height = 30)
	DelNo = Button(Del, text = "No", command = Del.destroy)
	DelNo.place(x = 10, y = 85, width = 105, height = 30)
	DeleteString.clear()

# Helper function to delete and entry 
def DeleteConfirmed(Deleted):
	my_cursor.execute(Deleted)
	mydb.commit()
	DeleteString.clear()

# Recovers the table name to delete all entrys
def DeleteAll():
	DelAll = Toplevel()
	DelAll.geometry("110x125")
	DELETEALL = DELALLEntry.get()
	DelALLLabel = Label(DelAll, text = "Confirm Data Deletion?")
	DelALLLabel.place(x = 10, y= 10, width = 105, height = 30)
	DelALLYes = Button(DelAll, text = "Yes", command = DeleteAllConfirmed(DELETEALL))
	DelALLYes.place(x = 10, y = 45, width = 105, height = 30)
	DelALLNo = Button(DelAll, text = "No", command = DelAll.destroy)
	DelALLNo.place(x = 10, y = 85, width = 105, height = 30)
	DELALLEntry.delete(0,'end')

# Helper function to read and store the data in the file
def ReadFile():
	BulkInsertString = "LOAD DATA LOCAL INFILE \'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\" + Read_FileEntry.get() + "\' INTO TABLE PLAYERS FIELDS TERMINATED BY ', ' OPTIONALLY ENCLOSED BY '''' LINES TERMINATED BY '\n';"
	#print(BulkInsertString)
	my_cursor.execute(BulkInsertString)
	mydb.commit()
	Read_FileEntry.delete(0,'end')
	
# Helper function that excutes the command to truncate a table	
def DeleteAllConfirmed(TableName):
	DelKeys = "SET FOREIGN_KEY_CHECKS = 0;"
	my_cursor.execute(DelKeys)
	mydb.commit()
	DelAllTemp = "TRUNCATE TABLE " + TableName + ";"
	my_cursor.execute(DelAllTemp)
	mydb.commit()
	FixKeys = "SET FOREIGN_KEY_CHECKS = 1;"
	my_cursor.execute(FixKeys)
	mydb.commit()
	#print(DelAllTemp)

# function to read the file line by line
# and store the contents in a list
def SingleInsert():
	SingleFile = open(SingleInsertionEntry.get(), 'r')
	error = 0

	while(True):
		Line = SingleFile.readline()
		if not Line:
			break
		SingleInsertString.append(Line)

	starttime = time.time()

	for index in SingleInsertString:
		SingleInsertStringDB = "insert into Players values(" + index + ");"
		try	:
			my_cursor.execute(SingleInsertStringDB)
			mydb.commit()
		except:
			error = 1

	end = (time.time() - starttime)
	print(end)

	SingleFile.close()

	if error == 1:
		SingleInsertError()
	else:
		TimeTaken(end)

# Helper Function to print error message during single insertion 
def SingleInsertError():
	ErrorBox = Toplevel()
	ErrorBox.geometry('150x250')
	ErrorBoxLabel = Label(ErrorBox, text = "One or more data types are incorrect")
	ErrorBoxLabel.pack()

# Helper Funciton to print out the time taken to 
def TimeTaken(timetaken):
	TimeBox = Toplevel()
	TimeBox.geometry('150x300')
	TimeBoxLabel = Label(TimeBox, text = "Total time taken to insert: " + str(timetaken) + " seconds")
	TimeBoxLabel.pack()

####################################################### creation of root #######################################################

root = Tk()
root.title("Database: project1")
root.geometry("1275x700")
#create label widget
#label = Label(root, text = "Query:")
#put it on screen
#label.place(x = 10, y = 10 )

#################################################### Display Table Frame#######################################################

DisplayFrame = LabelFrame(root, text="Display a Query", padx = 10, pady = 10)
DisplayFrame.place(x = 10, y = 0)

# adding a text box to wirte queries
Query = Entry(DisplayFrame, width=40)
Query.pack()
Query.insert(0, "Enter query here.")

# create button widgets
DisplayBut = Button(DisplayFrame, text="Display Table", command=lambda: Display(Query.get()), width=25)
EraseTextBox = Button(DisplayFrame, text="Delete Text Box", command=EraseText, width=25)

# adding buttons to the window
DisplayBut.pack()
EraseTextBox.pack()

##################################################### Delete Frame ##################################################################
DeleteFrame = LabelFrame(root, text = "Delete Entry", padx = 10, pady = 10)
DeleteFrame.place(x = 300, y = 0)

# DELNAME
DELNAMELABEL = Label(DeleteFrame, text="Name:")
DELNAMELABEL.pack(padx = 5, pady = 5)#place(x = 100, y = 20)
DELNAME = Entry(DeleteFrame, width = 40)
DELNAME.pack(padx = 5, pady = 5)#place(x = 100, y = 40)

# DELPLAYERID
DELPLAYERIDLABEL = Label(DeleteFrame, text="playerID:")
DELPLAYERIDLABEL.pack(padx = 5, pady = 5)#place(x = 100, y = 60)
DELPLAYERID = Entry(DeleteFrame, width = 40)
DELPLAYERID.pack(padx = 5, pady = 5)#place(x = 100, y = 80)

# string to delete and entry
DeleteBut = Button(DeleteFrame, text="Delete", width = 10, command = RemoveEntry)
DeleteBut.pack(padx = 5, pady = 5)#place(x = 100, y = 100, width = 100, height = 30)

########################################################## Insert Frame #########################################################

InsertFrame = LabelFrame(root, text = "Insert Single Entry", padx = 10, pady = 10)
InsertFrame.place(x = 10, y = 180)

InsertBut = Button(InsertFrame, text="Insert Single Entry", width = 15, command = InputEntry)
InsertBut.pack()

# NAME
NAMELABEL = Label(InsertFrame, text="Name:")
NAMELABEL.pack(padx = 5, pady = 5)#place(x = 10, y = 20)
NAME = Entry(InsertFrame, width = 40)
NAME.pack(padx = 5, pady = 5)#place(x = 10, y = 40)

# PLAYERID
PLAYERIDLABEL = Label(InsertFrame, text="playerID:")
PLAYERIDLABEL.pack(padx = 5, pady = 5)#place(x = 10, y = 60)
PLAYERID = Entry(InsertFrame, width = 40)
PLAYERID.pack(padx = 5, pady = 5)#place(x = 10, y = 80)

# TEAMNAME
TEAMNAMELABEL = Label(InsertFrame, text="teamname:")
TEAMNAMELABEL.pack(padx = 5, pady = 5)#place(x = 10, y = 100)
TEAMNAME = Entry(InsertFrame, width = 40)
TEAMNAME.pack(padx = 5, pady = 5)#place(x = 10, y =120)

# POSITION
POSITIONLABEL = Label(InsertFrame, text="position:")
POSITIONLABEL.pack(padx = 5, pady = 5)#place(x = 10, y = 140)
POSITION = Entry(InsertFrame, width = 40)
POSITION.pack(padx = 5, pady = 5)#place(x = 10, y = 160)

# TOUCHDOWNS
TOUCHDOWNSLABEL = Label(InsertFrame, text="touchdowns:")
TOUCHDOWNSLABEL.pack(padx = 5, pady = 5)#place(x = 10, y = 180)
TOUCHDOWNS = Entry(InsertFrame, width = 40)
TOUCHDOWNS.pack(padx = 5, pady = 5)#place(x = 10, y = 200)

# TOTALYARDS
TOTALYARDSLABEL = Label(InsertFrame, text="totalyards:")
TOTALYARDSLABEL.pack(padx = 5, pady = 5)#place(x = 10, y = 220)
TOTALYARDS = Entry(InsertFrame, width = 40)
TOTALYARDS.pack(padx = 5, pady = 5)#place(x = 10, y = 240)

# SALARY
SALARYLABEL = Label(InsertFrame, text="salary:")
SALARYLABEL.pack(padx = 5, pady = 5)#place(x = 10, y = 260)
SALARY = Entry(InsertFrame, width = 40)
SALARY.pack(padx = 5, pady = 5)#place(x = 10, y = 280)

################################################################ Delete All Frame ########################################

DeleteALL = LabelFrame(root, text = "Delete All", padx = 10, pady = 10)
DeleteALL.place(x = 300, y = 220)

DELALLEntry = Entry(DeleteALL, width = 40)
DELALLEntry.pack(padx = 10, pady = 10)

DELALLBut = Button(DeleteALL, text = "Delete All", width = 10, command = DeleteAll)
DELALLBut.pack()

############################################################### Bulk Data Insertion ########################################

BulkInsert = LabelFrame(root, text = "Bulk Data Insertion", padx = 10, pady = 10)
BulkInsert.place(x = 300, y = 360)

Read_File_Label = Label(BulkInsert, text = "File name including extention:")
Read_File_Label.pack()

Read_FileEntry = Entry(BulkInsert, width = 40)
Read_FileEntry.pack(padx = 10, pady = 10)

BulkInsertBut = Button(BulkInsert, text = "Insert File", width = 10, command = ReadFile)
BulkInsertBut.pack()

################################################################ Single Insertion from file #######################################################

SingleInsertion = LabelFrame(root, text = "Single Data Insertion", padx = 10, pady = 10)
SingleInsertion.place(x = 300, y = 510)

SingleInsertionLabel = Label(SingleInsertion, text = "File name including extention:")
SingleInsertionLabel.pack()

SingleInsertionEntry = Entry(SingleInsertion, width = 40)
SingleInsertionEntry.pack()

SingleInsertionBut = Button(SingleInsertion, text = "Insert File", width = 10, command = SingleInsert)
SingleInsertionBut.pack()

################################################################ Close Button and Main Loop #####################################################

TEXT = Text(root, padx = 10, pady = 10 )
TEXT.place(x = 600, y = 10)

# close button
CloseBut = Button(root, text="Close", command = root.destroy)
CloseBut.place(x = 300, y=670, width = 100, height = 30)

root.mainloop()

print(mydb)

