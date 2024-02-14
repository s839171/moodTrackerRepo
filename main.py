import guizero as gz
import matplotlib as mp
import numpy as np

# going to have a variable set to the mood value
# have an enter box that will be disabled until a new mood is selected.
# when enter box is clicked, disables the box again
# maybe have a function to rename entries
# haven't done any code for resources page other than showing widgets. Did attempt to change the shown current mood in function enterEntry.

currentMood = 0
currentPage = 1
entryList = []
moodList = []
whyList = []

# START OF GENERAL FUNCTIONS (incomplete)
# combining individual functions for changing page into one function
def changePage(new):
    global currentPage
    if currentPage == 1:
        moodQuestion.hide()
        moodBox.hide()
        whyQuestion.hide()
        whyAnswer.hide()
        enterAnswer.hide()
    if currentPage == 2:
        loggedMoodBox.hide()
        resourcesBox.hide()
        editResourcesBox.hide()
    if currentPage == 3:
        picture.hide()
    if currentPage == 4:
        userBox.hide()
        settingsSeparator.hide()
    if new == 1:
        homeButton.disable()
        resourcesButton.enable()
        trendsButton.enable()
        settingsButton.enable()
        #showing homePage
        moodQuestion.show()
        moodBox.show()
        whyQuestion.show()
        whyAnswer.show()
        enterAnswer.show()
        currentPage = 1
    elif new == 2:
        resourcesButton.disable()
        homeButton.enable()
        trendsButton.enable()
        settingsButton.enable()
        #showing resources page
        loggedMoodBox.show()
        resourcesBox.show()
        editResourcesBox.show()
        currentPage = 2
    elif new == 3:
        trendsButton.disable()
        homeButton.enable()
        resourcesButton.enable()
        settingsButton.enable()
        #showing trends page
        picture.show()
        currentPage = 3
    elif new == 4:
        settingsButton.disable()
        homeButton.enable()
        resourcesButton.enable()
        trendsButton.enable()
        #showing settings page
        userBox.show()
        settingsSeparator.show()
        currentPage = 4
# END OF GENERAL FUNCTIONS

# START OF HOMEPAGE FUNCTIONS
def changeMood(num):
    global currentMood
    currentMood = num
    enterAnswer.enable()

# not changing text for some reason
#def enterEntry():
#    global currentMood
#    enterAnswer.disable()
#    loggedMoodText2.value = currentMood

# END OF HOMEPAGE FUNCTIONS

app = gz.App(title="Mood Tracker")
app.bg = "#832C38"
app.text_color = "#F0A4A0"
# START OF GENERAL UI
titleBox = gz.Box(app, border=3, width="fill",height=50)
text = gz.Text(titleBox, text="App Title", height="fill", size=18)

bottomBox = gz.Box(app, border=3, width="fill", height=50, align="bottom")
pageSelection = gz.Box(bottomBox, layout="grid")

homeButton = gz.PushButton(pageSelection, text="Home", grid=[0, 0], command=changePage, args=[1])
homeButton.disable()
resourcesButton = gz.PushButton(pageSelection, text="Resources", grid=[1, 0], command=changePage, args=[2])
trendsButton = gz.PushButton(pageSelection, text="Trends", grid=[2, 0], command=changePage, args=[3])
settingsButton = gz.PushButton(pageSelection, text="Settings", grid=[3, 0], command=changePage, args=[4])
# END OF GENERAL UI

# START OF HOMEPAGE UI
moodQuestion = gz.Text(app, text="\nHow are you feeling?\n")
moodBox = gz.Box(app, border=3, layout="grid")
whyQuestion = gz.Text(app, text="\nWhy?\n")
whyAnswer = gz.TextBox(app, height=10, width=70, multiline="true")
enterAnswer = gz.PushButton(app, text="Enter")
enterAnswer.disable()

mood1 = gz.PushButton(moodBox, text="1", grid=[0, 0], command=changeMood, args=[1])
mood2 = gz.PushButton(moodBox, text="2", grid=[1, 0], command=changeMood, args=[2])
mood3 = gz.PushButton(moodBox,text="3", grid=[2, 0], command=changeMood, args=[3])
mood4 = gz.PushButton(moodBox, text="4", grid=[3, 0], command=changeMood, args=[4])
mood5 = gz.PushButton(moodBox, text="5", grid=[4, 0], command=changeMood, args=[5])
# END OF HOMEPAGE UI

# START OF RESOURCES UI
loggedMoodBox = gz.Box(app, width=175, height=50)
loggedMoodText1 = gz.Text(loggedMoodBox, text="Logged Mood: ", align="left")
loggedMoodText2 = gz.Text(loggedMoodBox, text="N/A", align="right")
resourcesBox = gz.Box(app, width=300, height=200, border=2)
helpfulResources = gz.Text(resourcesBox, text="Helpful Resources: ", align="top")
helpfulResourcesList = gz.ListBox(resourcesBox, align="bottom", height="fill", width=200, scrollbar=True)
editResourcesBox = gz.Box(app, width=300, height=45)
deleteResourcesButton = gz.PushButton(editResourcesBox, text="Delete", align="right")
editResourcesButton = gz.PushButton(editResourcesBox, text="Edit", align="right")

loggedMoodBox.hide()
resourcesBox.hide()
editResourcesBox.hide()
# END OF RESOURCES UI

# START OF SETTINGS UI
userBox = gz.Box(app, width=175, height=100)
usernameBox = gz.Box(userBox, align="bottom")
usernameChange = gz.PushButton(usernameBox, text="edit", align="right")
usernameLabel = gz.Text(usernameBox, text="Username", align="left", size=16)
settingsSeparator = gz.Box(app, width="fill", border=3, height=2)
userBox.hide()
settingsSeparator.hide()

# START OF TRENDS UI
picture = gz.Picture(app, image="exampletrendgraph.gif")
picture.hide()
# END OF TRENDS UI
app.display()