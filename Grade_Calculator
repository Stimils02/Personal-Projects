#This program is a grade calculator which allows the user to enter their raw scores
#for 7 components and the program will compute and display the final weighted numerical grade


from graphics import *

def make():

    #Creates a window--------------------------------------------------------------------------------------------
    
    win = GraphWin('CS177 Grade Calc', 400, 400)

    #This creates a formatted title with italicized descriptions with the relative font
    title = Text(Point(200,30), 'Grade Calculator')
    title.draw(win)
    title.setSize(16)
    instruct = Text(Point(200,52), 'Enter your category percentages from BrightSpace')
    instruct.draw(win)
    instruct.setSize(8)
    instruct.setStyle('italic')

    #Creates a Red Rectangle with an Exit inside of it with the correct format-------------------------------------------------------
    Exit = Rectangle(Point(149,340), Point(229, 380))
    txt_exit = Text(Point(189,360), 'EXIT')
    txt_exit.setFill('white')
    txt_exit.setStyle('bold')
    txt_exit.setSize(16)
    Exit.setFill('red')
    Exit.draw(win)
    txt_exit.draw(win)


    
    #Here we create an efficent method to formatting the labels and aligning them correctly so it appears as presented-----------------------------
    Labels = ['Participation', 'Homework     ', 'Lab Preps    ', 'Labs         ', 'Projects     ', 'Exams        ', 'Final Project']
    entry_list =[]

    #for loop goes from 0 to len of label list and performs the same function with only the y coordinate changing by a given amount 
    for i in range(0, len(Labels)):
        
        P = Point(130, 85 + (30 * i))
        txt_label = Text(P,Labels[i])
        txt_label.setFace('courier')
        txt_label.setSize(10)
        txt_label.draw(win)

        
        colon = Text(Point(220, 85 +(30 * i)), ':')
        colon.setStyle('bold')
        colon.draw(win)

    #This for loop creates 7 entry boxes with the default text being set to 0
    for k in range(0, 7):

        P2 = Point(295, 85 + (30 * k))
        entry = Entry(P2, 6)
        entry.setFill('white')
        entry.setText('0')
        entry.draw(win)
        entry_list.append(entry)
        
    #Finally we set the last bit of formatting by creating a black line, colons and the entry box for semester score--------------------------
        
    aline = Line(Point(86,285), Point(330,285))
    aline.draw(win)

    #Semester score is presented with style courier and bolded
    sem = Text(Point(135, 300), 'Semester Score')
    sem.setFace('courier')
    sem.setStyle('bold')
    sem.draw(win)

    
    #Colon is formatted here in a relative coordinate
    colon2 = Text(Point(220, 300), ':')
    colon2.setStyle('bold')
    colon2.draw(win)

    #We create the entry box for semster score 
    sem_entry = Entry(Point(295, 300), 6)
    sem_entry.setFill('white')
    sem_entry.draw(win)
    sem_entry.setText('0')

    #returns the grid, red rectangel, list of seven entries and semster entry box
    return(win, Exit, entry_list, sem_entry)

()


#Clicked function----------------------------------------------------------------------
def clicked(click, rect):

    #Checks whether or not a click is detected 
    if not click:
        return False

    #Set point 1 and point 2 to the two corners of the rectangle    
    point1 = rect.getP1()
    point2 = rect.getP2()

    #If the x coordinate is > first point and less than second point and the Y coordinate is > first point and less than second point return true
    return (point1.getX() < click.getX() < point2.getX()) and (point1.getY() < click.getY() < point2.getY())


()


#Calculate function with entry boxes as input-------------------------------------------------------
def calculate(entries):

    #Create two lists. First list will contain the list of float values once you check if they are a float or not
    final_list = []

    #Second list contains the test_list which will get the texts from the entry boxes and append it to test list
    test_list = []

    #we set default score to 9 or any number that isn't 0 so that the if statement can run
    score = 9

    #Then append everything from entry box to test list
    for element in entries:
        test_list.append(element.getText())

    #For each item in test list we try to convert it to a float. If it works then it is appended to final list. If not then score is set to 0
    for item in test_list:
        try:
            float(item)
            final_list.append(item)
        except:
            score = 0

    #Now assuming score is not 0, we apply the formula and set score to the output for the formula 
    if score != 0:
        score = round(((float(final_list[0])*.05) + (float(final_list[1]) * .1) + (float(final_list[2]) * .05) + (float(final_list[3]) * .2) + (float(final_list[4]) *.25) + (float(final_list[5]) * .25) + (float(final_list[6])*.1)),2) 

    #Then finally we return the score to be used in the main function
    return(score)
     

()


#We call the main()----------------------------------------------------------
def main():


    #We take what we returned from make and set it to 4 variables in the right order
    grid, Exit, entry_list, score = make()

    #Then we set click1 to whether or not its clicked on the grid or not
    click1 = grid.checkMouse()

    #While the user does not click on exit (calling on the clicked function by inputting click1 and exit into clicked function) 
    while (clicked(click1, Exit) == False):

        #Then we call the calculate function with our entry list
        x = calculate(entry_list)

        #Set the score to the output of x
        score.setText(x)

        #wait for a mouse click to see if its in the rectangle or the person wants to do it again
        click1 = grid.checkMouse()
        
    #if exit is clicked we close the window ultimately ending our program
    else:
        grid.close()
        

()
main()

