#Import Graphics from the graphics library
from graphics import *
import math
import random


#We create a clicked function to use later to deal with mouse clicks-------------------------------------------------
def clicked(click, rect):

    #if no mouse click was detected we return false
    if not click:
        return False

    #Gets points 1 and 2 of the corners of the rectangle 
    point1 = rect.getP1()
    point2 = rect.getP2()

    #If the x coordinate is > first point and less than second point and the Y coordinate is > first point and less than second point return true
    return (point1.getX() < click.getX() < point2.getX()) and (point1.getY() < click.getY() < point2.getY())


#boundary for the chips------------------------------------------------
def boundary(click, x1, x2):

    #if no mouse click was detected we return false
    if not click:
        return False

    ##If the x coordinate is > first point and less than second point and the Y coordinate is > first point and less than second point return true
    return (x1< click.getX() < x2) and (100 < click.getY() < 139)


#Define board() function---------------------------------------------------------
def board():

    #Create a graphics window with correct format 
    win = GraphWin('Game Board', 500, 700, autoflush=False)
    win.setBackground('light grey')

    #Put the TrinkoTitle gif at the top, matching it with the picture
    TrinkoImage = Image(Point(250,50), "LetsPlay.gif")
    TrinkoImage.draw(win)

    #Create the white rectangle at the bottom with dimensions 500 x 100 
    rectangle_white = Rectangle(Point(0,600), Point(500,700))
    rectangle_white.setFill('white')
    rectangle_white.draw(win)

    #Create 2 lines, one at the top and one at the bottom going across the window with width set to 3
    Aline = Line(Point(0,100), Point(500,100))
    Aline.setWidth(3)
    Aline.draw(win)
    Bline = Line(Point(0,600), Point(500,600))
    Bline.setWidth(3)
    Bline.draw(win)

    #We create our chip text count on the bottom left of the screen
    chips = Text(Point(90,650), "Chips: 0")
    chips.setSize(24)
    chips.draw(win)

    #Here we create the score score count on the bottom right of the screen
    score = Text(Point(420,650), "Score: 0")
    score.setSize(24)
    score.draw(win)

    #Then we return the window, chips and score 
    return(win, chips, score)

()

#Creates the bins by taking the graphic window as a parameter so that it can create it in the graphic window--------------------------------
def bins(graphwindow):

    #number list that will be added to the bottom inside the bins
    number_list = ['40','0','60','100','20', '0','80']

    #make for loop to create the bins at the top and bottom 
    for i in range(0,9):

        #Creates bin at top by only changing the x coordinat, abiding by correct formatting  
        bins = Line(Point(5 + (70 * i), 100), Point(5 + (70 * i),139))
        start = bins.getP1()
        bins.setWidth(3)
        bins.draw(graphwindow)

        #Creates bin at bottom by only changing the x coordinate, abiding by correct formatting
        bottom_bins = Line(Point(5 + (70 * i), 560), Point(5 + (70 * i), 599))
        bottom_bins.setWidth(3)
        bottom_bins.draw(graphwindow)

    #for loop is used to put each of the numbers in the list in between the appropriate bins 
    for k in range(0,len(number_list)):

        #Changes the x coordinate and calls Text() function and indexes the list to the approriate coordinate
        points = Point(40 + (70 * k), 580)
        score = Text(points, number_list[k])
        score.draw(graphwindow)
()

#Now we define our pins() function, taking graphic window as a parameter----------------------------------------------------------------- 
def pins(win):

    #Create empty list to store the pin circles
    PinCircle = []

    #Create two centers: Center for 7 pin circles and 6 pin circles
    center = Point(40, 180)
    center2 = Point(75, 220)

    #We create a nested for loop for the 7 pin circles
    for row in range(0,5):
        
        #We get the centers of the first coordinate of the 7 pin circle
        dx = center.getX()
        dy = center.getY()

        #Then we change the dy based on what row is once the second for loop is done iterating
        dy_change = dy + (80 * row)

        #This for loop puts a set of 7 circles in one row 
        for i in range (0,7):

            #we change the dx by the approriate amount 
            dx_change = dx + (70 * i)

            #get new center points for the circle and create the circle around those center points
            new_center = Point(dx_change,dy_change)
            seven_pin = Circle(new_center ,5)
            seven_pin.setFill('black')
            seven_pin.draw(win)

            #Then we append all that to a list
            PinCircle.append(seven_pin)
            
    #repeats the same actions as we did to the 7 pin circles
    for row2 in range(0,5):

        #we use the second center point offset by 35
        Dx = center2.getX()
        Dy = center2.getY()
        Dy_change = Dy + (80 * row2)

        #Main difference is we change the range from 0 to 6  
        for k in range (0,6):
            Dx_change = Dx + (70 * k)
            new_center2 = Point(Dx_change, Dy_change)
            six_pin = Circle(new_center2,5)
            six_pin.setFill('black')
            six_pin.draw(win)
            PinCircle.append(six_pin)

    #Then we return the PinCircles
    return(PinCircle)

#Controls the game------------------------
def control():

    #Here we design our game control window
    win = GraphWin('Game Control', 500, 200)
    win.setBackground('light grey')

    #import the TrinkoTitle image
    image = Image(Point(250,50), 'TrinkoTitle.gif')
    image.draw(win)

    #Create a play rectangle
    play = Rectangle(Point(130,130),Point(240,160))
    play.setFill('green')

    #get the center of that rectangle
    p1 = play.getCenter()

    #put the play text at the center with correct formatting
    play_txt = Text(p1,'PLAY')
    play_txt.setSize(21)
    play_txt.setTextColor('white')
    play.draw(win)
    play_txt.draw(win)

    #create a exit rectangle
    exit_rec = Rectangle(Point(280,130),Point(390,160))
    exit_rec.setFill('red')

    #get the center of the exit rectangle 
    p2 = exit_rec.getCenter()

    #put text at the center of the rectangle with correct foratting
    exit_rec_txt = Text(p2,'EXIT')
    exit_rec_txt.setSize(21)
    exit_rec_txt.setTextColor('white')
    exit_rec.draw(win)
    exit_rec_txt.draw(win)

    #get mouse click
    click = win.checkMouse()

    #while exit is not clicked, keep running the code
    while (clicked(click, exit_rec) == False):

        #Otherwise if play is clicked
        if (clicked(click, play)):

            #close window
            win.close()

            #return true, this will allow us to control the game in the main() function
            return True

        #otherwise keep checking for mouse clicks
        else:
        
            click = win.checkMouse()
        
    else:

        #if exit is clicked, close the window 
        win.close()

        #return false, which in the main will close the whole program
        return False

   

#checks if the chip has collided with a wall or not--------------------------------------
def hitwall(center):

    #checks if the chip has hit a wall or not
    if center.getX() == 16 or center.getX() == 484:

        #returns true if it has
        return True

    #else false
    return False
        
#checks for if the chip is within a bin or not------------------------
def whichbin(center, x1, x2):

    #checks to see which bin the chip has landed in 
    x = center.getX()
    y = center.getY()

    #returns true if it is within a certain x value range of the bin
    if (x1 < x < x2) and (566 < y < 600):
        return True

    #else it returns false
    else:
        return False

#checks to see if the chip has collided with a pin or not---------------------------
def collison(center, pin):

    ###important code which checks for collison with a pin

    #First we get the center of the pin
    p2 = pin.getCenter()

    #we get the x and y coordinates of the chip's center which was passed into the function
    x = center.getX()
    y = center.getY()

    #Then we get the x and y coordinates of the pin's center
    x1 = p2.getX()
    y1 = p2.getY()

    #We apply the distance formula and if thats less than the combined radii
    if math.sqrt((x - x1)**2 + (y-y1)**2) <= (20):

        #we return true that the chip has collided
        return True

    #else we return false
    return False
    
#drop the chip function-------------------------------------------------------
#takes in 5 arguments
def drop(num, win, pin, score, tokens):


    #Here we draw the final results rectangle background with the same dimensions
    result_bk = Rectangle(Point(145,280),Point(345,380))
    result_bk.setFill('white')

    #Then we draw the final results rectangle that is gold
    result_rect = Rectangle(Point(150,285),Point(340,375))
    result_rect.setFill('gold')

    #Then we draw text on the rectangle to guide the user
    result_direct = Text(Point(245,353), 'Click to continue')
    result_direct.setStyle('italic')

    #we initialize points to 0 
    points = 0

    #We set our tokens string to however many chips the user won
    tokens.setText('Chips: ' + str(num))

    #here we just initalize a circle 
    chip = Circle(Point(0,0), 15)
    
    #we make a list of tuples that has the borders for the bin, to set as our boundaries
    bin_boundary = [(6,74), (76,144), (146,214), (216,284), (286,354), (356,424), (426, 494), (496, 566)]

    #Then we have a list of integers which corresponds to each bin
    bin_points = [40, 0, 60, 100, 20, 0, 80]

    #we have i set to 1 for our for loop
    i = 1

    #Then we set num to count so we can change the count later without affecting num
    count = num
    
    #while the loop is less than the amount chips + 1
    while (i < num + 1):

        #we get a mouse click
        m = win.getMouse()

        #while one of the bins hasn't been clicked
        while (boundary(m,6,74) or boundary(m,76,144) or boundary(m,146,214) or boundary(m,216,284) or boundary(m,286,354) or boundary(m,356,424) or boundary(m,426,494) or boundary(m,496,566)) == False:

            #we keep getting a mouse click
            m = win.getMouse()

        #if the bin has been clicked
        else:

            #we reduce count by 1
            count -= 1

            #set the tokens to what our count is now, minus the dropped chip
            tokens.setText('Chips: ' + str(count))

            #this undraw is so that chip resets everytime there is a mouse click
            chip.undraw()

            #we get the x and y coordinates of the mouse click to check where the mouse click was
            x = m.getX()
            y = m.getY()

            #if the chip was clicked within one of the boundaries
            if (boundary(m,6,74) or boundary(m,76,144) or boundary(m,146,214) or boundary(m,216,284) or boundary(m,286,354) or boundary(m,356,424) or boundary(m,426,494) or boundary(m,496,566)) == True:

                #we draw a chip within that area with center of where the mouse click was
                chip = Circle(Point(x,y), 15)

                #we set the color to gold, draw it and get the center of the chip
                chip.setFill('gold')
                chip.draw(win)
                center = chip.getCenter()

                #while the center of the chio or the chip itself is within the upper and lower limits (y-axis boundaries) 
                while center.getY() > 100 and center.getY() < 580:

                    #initalize dx and dy
                    dx,dy = 0, 0

                    #move chip that amount which does nothing but will everytime the loop repeats
                    chip.move(dx,dy)

                    #change dx and dy by the specified amount
                    dx = dx * 0.8
                    dy = dy + 4

                    #get the center of the chip again to check where it is at
                    center = chip.getCenter()

                    #for loop to iterate through all the pins to check which pin was hit
                    for k in range(0,len(pin)):

                        #get the center of the pin
                        pin_center = pin[k].getCenter()

                        #pass it onto our collison and hitwall function to see it collided
                        if collison(center,pin[k]) or hitwall(center) == True:

                            #if so the dx, dy are set to 2 and 5 after the collison, to make sure the chip does something once it hits the pin
                            dx = 2
                            dy = 5

                            #if the chip hits the pin from the left
                            if center.getX() < pin_center.getX():

                                #dx is negated so that the chip switched directions
                                dx = -6

                                #dy is set to 5 * .4, to get the right amount of bounce
                                dy = -5 * .4

                                #The pin is set to red for the moment
                                pin[k].setFill('red')

                                #chip moves that amount 
                                chip.move(dx, dy)

                            #if the chip hits the pin from the right
                            elif center.getX() > pin_center.getX():

                                #dx remains positive
                                dx = 6

                                #dy changes to add a little bounce 
                                dy = -5 * .4

                                #the pins color is temporary changes to red
                                pin[k].setFill('red')

                                #chip moves the specified amount
                                chip.move(dx,dy)
                        else:

                            #otherwise the color is changed back to black
                            pin[k].setFill('black')

                    #chip moves a certain amount and the animation is updated
                    chip.move(dx,dy)
                    update(30)
                
                #for loop to check which bin the chip has landed in 
                for x in range(0, len(bin_boundary)):

                    #a and b are set to the boundary values of the tuples in the list
                    a = bin_boundary[x][0]
                    b = bin_boundary[x][1]

                    #those borders are passed into the which bin function
                    if whichbin(center, a, b) == True:

                        #if the chip is within those boundaries, the points are incremented 
                        points += bin_points[x]

                        #score text changes
                        score.setText('Score: ' + str(points))
                        
        #keeps track of while loop iterations     
        i += 1
            
    else:

        #We set the texts of both rectangles
        result_txt = Text(Point(245,316), 'Congratulations!\nYour final score is: ' + str(points))
        result_txt.setStyle('bold')

        #Here we draw all our results rectangles that display the points of the user after the while loop terminates
        result_bk.draw(win)
        result_rect.draw(win)
        result_txt.draw(win)
        result_direct.draw(win)

        #we wait for a mouseclick then we close the window
        m = win.getMouse()
        win.close()

        #we return those points for our creative function
        return points
       
    
#We create our makeQuiz function which will create the window--------------------------------------------------
def makeQuiz():

    #We make two lists, one for rectangles and the other for text lists
    txt_lst = []
    rect_lst = []

    #We create the Trivia Time window 400 by 400 window
    win = GraphWin('Trivia Time', 400, 400)
    win.setBackground('light grey')

    #restructure the coordinate sysstem to easily navigate through it 
    win.setCoords(0,0,400,400)

    
    #We get the TriviaTime.gif 
    TrinkoImage = Image(Point(200,360), 'TriviaTime.gif')
    TrinkoImage.draw(win)


    #Then our black rectangle at the bottom 
    bottom = Rectangle(Point(0,0),Point(400,40))
    bottom.setFill('black')
    bottom.draw(win)
   
    #We create a for loop to append the rectangles and and texts to the list of rectangles and texts
    for i in range(0,4):

        #Here we create the rectangles
        rect = Rectangle(Point(0,45 + (40 * i)),Point(400,85 + (40 * i)))
        rect.setFill('gold')
        rect.draw(win)
        rect_lst.append(rect)

        #Here we create the text messages
        rect_txt = Text(Point(200,65 + (40 * i)), '')
        rect_txt.draw(win)
        txt_lst.append(rect_txt)
        

    #We create our question and append it to the text list 
    question = Text(Point(200,270), "")
    question.setStyle('bold')
    question.draw(win)
    txt_lst.append(question)

    #We create our question counter and append that to the list as well
    Question_txt = Text(Point(60,22), 'Question #1')
    Question_txt.setFill('white')
    Question_txt.setStyle('bold')
    txt_lst.append(Question_txt)

    #Then we create our points counter and also append that to our text list
    Correct_txt = Text(Point(330,22), 'Correct: 0')
    Correct_txt.setFill('white')
    Correct_txt.setStyle('bold')
    Correct_txt.draw(win)
    txt_lst.append(Correct_txt)
    Question_txt.draw(win)

    return (win, rect_lst, txt_lst)


#Then we create our pickQs() function to randomly pick questions-----------------------------------------------------------------------
def pickQs():

    #We open up our textfile for reading with correct formatting
    infile = open('questions.txt', 'r', encoding = 'utf8')

    #We intalize our variables
    main_list = []
    question_list = []
    question_dict = {}
    keys_list = []

    #We read line for line and then split the line using commas
    for line in infile:

        #We append the line into our main list
        main_list.append(line.split(','))

    #Then we randomly choose 5 of those questions using random.sample() which allows for no duplicate questions in the list
    question_list = random.sample(list(main_list),5)

    #Then we use a for loop to iterate through the loop 
    for i in range(0, len(question_list)):

        #We create a dictionary with correct formatting for each question and append it to our list
        question_dict[question_list[i][0]] = (question_list[i][1],question_list[i][2], question_list[i][3], question_list[i][4], question_list[i][5].replace('\n',''))

        #We then also append each key to the list of keys
        keys_list.append(question_list[i][0])

    #Once we are done with the file, we close our file
    infile.close()

    #Then we return our dictionary and list of keys to use in the takeQuiz() function
    return (question_dict, keys_list)


#Here we define our takeQuiz function--------------------------------------------------------------------- 
def takeQuiz():

    #We call the makeQuiz and PickQs function and set the returned values to variables
    win, rect_lst, txt_lst = makeQuiz()
    question_dict, keys_list = pickQs()

    #We intitalize a temporary list of later use
    temp = []

    #Here we create the background to our results rectangle
    correct_bk = Rectangle(Point(100,190),Point(300,290))
    correct_bk.setFill('white')

    #Then we draw another rectangle within that background and make it gold
    correct_rect = Rectangle(Point(105,195),Point(295,285))
    correct_rect.setFill('gold')

    #We set the texts inside those rectangle
    correct_txt = Text(Point(200,260), 'You are correct!')
    correct_txt.setStyle('bold')
    correct_direct = Text(Point(200,230), 'Click to continue')
    correct_direct.setStyle('italic')

    #Then we create our wrong results rectangle background
    wrong_bk = Rectangle(Point(100,190), Point(300,290))
    wrong_bk.setFill('white')

    #We create a rectangle that is red within that rectangle
    wrong_rect = Rectangle(Point(105,195),Point(295,285))
    wrong_rect.setFill('red')

    #Then we set the texts for the wrong results rectangle
    wrong_txt = Text(Point(200,260), 'Sorry, that is incorrect')
    wrong_txt.setStyle('bold')
    wrong_direct = Text(Point(200,230), 'Click to continue')
    wrong_direct.setStyle('italic')

    #These will serve as our counters of correct answers and number of questions
    score = 0
    count = 0

    #We create a for loop that iterates 5 times for each question
    for unit in range(0,len(keys_list)):

        #When the for loop iterates the count variable increases
        count += 1

        #Then we set that text to the string on the bottom left
        txt_lst[5].setText('Question #' + str(count))

        #We get the question from the key list and set that to the variable question
        question = keys_list[unit]
        
        #Then we split that question using spaces to turn it to a list
        temp = question.split(' ')

        #intalize a temporary string
        temp_str = ''

        #value is set to the tuple of values
        value = question_dict[question]

        #Then letter or answer is taken from that tuple
        letter = value[4]
        
        #We create a for loop that formats the string with '\n' for every 5 lines
        for k in range(1,len(temp)):
            if len(temp) > 5:
                if k % 5 == 0:
                    temp[k] = '\n' + temp[k]
                    
        #Then we turn it back into a big string using another for loop          
        for item in temp:
            temp_str += item + ' '

        #Finally we set the question string to the question text in the window
        txt_lst[4].setText(temp_str)
        
        #We set the texts from the tuples to our rectangle 
        for i in range(0,4):

            #The first rectangle is the bottom rectangle since it was appended that way in the for loop
            #We set the strings in the rectangles by going backwards
            txt_lst[3-i].setText(value[i])
            

        #use get mouse to detect mouse clicks
        click = win.getMouse()
        
        #while there is no click in the gold rectangles do nothing and continue to detect clicks
        while (clicked(click, rect_lst[0]) or clicked(click, rect_lst[1]) or clicked(click, rect_lst[2]) or clicked(click, rect_lst[3])) == False:
            
            click = win.getMouse()
            
        #once there is a click inside the gold rectangles
        else:
            
            #Here there are a series of if and elif statements to check for a particular rectangle
            if question_dict[keys_list[unit]][4] == 'A':
                
                #if the letter value is 'A' and if the first rectangle (which is actually the last one in the rectangle list) was clicked
                if clicked(click,rect_lst[3]) == True:

                    #We draw our results rectangles if the click was detected in the "first" rectangle and the answer was A
                    correct_bk.draw(win)
                    correct_rect.draw(win)
                    correct_txt.draw(win)
                    correct_direct.draw(win)

                    #Then we increase our score and set the text on the bottom right to that score
                    score += 1
                    txt_lst[6].setText('Correct: ' + str(score))

                    #While the results box is not clicked we keep on getting the mouse click
                    while clicked(click, correct_bk) == False:

                        click = win.getMouse()
                        
                    else:
        
                        #once it is clicked we undraw that box
                        correct_bk.undraw()
                        correct_rect.undraw()
                        correct_txt.undraw()
                        correct_direct.undraw()
                        
                        
                #Here we check whether any of the other 3 boxes were clicked 
                elif (clicked(click,rect_lst[0]) or clicked(click,rect_lst[1]) or clicked(click,rect_lst[2])) == True:
                    
                    #If they are clicked then we draw the results box that says its wrong
                    wrong_bk.draw(win)
                    wrong_rect.draw(win)
                    wrong_txt.draw(win)
                    wrong_direct.draw(win)

                    #We use a similar logic except for the wrong results box. If it is not clicked we keep on getting mouse click
                    while clicked(click, wrong_bk) == False:

                        click = win.getMouse()

                    else:
                        
                        #Otherwise the undraw our wrong results box
                        wrong_bk.undraw()
                        wrong_rect.undraw()
                        wrong_txt.undraw()
                        wrong_direct.undraw()
            
            
            #Then we repeat the process for if the answer is B           
            elif question_dict[keys_list[unit]][4] == 'B':
                
                #and the second rectangle is clicked  
                if clicked(click,rect_lst[2]) == True:

                    #draw the results box
                    correct_bk.draw(win)
                    correct_rect.draw(win)
                    correct_txt.draw(win)
                    correct_direct.draw(win)

                    #change score
                    score += 1
                    txt_lst[6].setText('Correct: ' + str(score))
                    
                    #check for mouse click
                    while clicked(click, correct_bk) == False:

                        click = win.getMouse()
                        
                    else: 

                        #undraw once mouse click
                        correct_bk.undraw()
                        correct_rect.undraw()
                        correct_txt.undraw()
                        correct_direct.undraw()
                        
                #check for clicks on the other 3          
                elif (clicked(click,rect_lst[1]) or clicked(click,rect_lst[0]) or clicked(click,rect_lst[3])) == True:

                    #wrong results rectangle is drawn
                    wrong_bk.draw(win)
                    wrong_rect.draw(win)
                    wrong_txt.draw(win)
                    wrong_direct.draw(win)

                    #Checks for clicks again
                    while clicked(click, wrong_bk) == False:

                        click = win.getMouse()
                        
                    else:

                        #Then wrong results rectangles are undrawn
                        wrong_bk.undraw()
                        wrong_rect.undraw()
                        wrong_txt.undraw()
                        wrong_direct.undraw()
            
            #We repeat same process for if the answer is C
            elif question_dict[keys_list[unit]][4] == 'C':

                #Checks click
                if clicked(click,rect_lst[1]) == True:

                    #draws the correct results
                    correct_bk.draw(win)
                    correct_rect.draw(win)
                    correct_txt.draw(win)
                    correct_direct.draw(win)
                    score += 1
                    txt_lst[6].setText('Correct: ' + str(score))
                    
                    #if click on correct result
                    while clicked(click, correct_bk) == False:

                        click = win.getMouse()
                        
                    else: 

                        #undraw
                        correct_bk.undraw()
                        correct_rect.undraw()
                        correct_txt.undraw()
                        correct_direct.undraw()
                 
                #checks for clicks in the other rectangles
                elif (clicked(click,rect_lst[0]) or clicked(click,rect_lst[2]) or clicked(click,rect_lst[3])) == True:

                    #draws wrong results rectangle
                    wrong_bk.draw(win)
                    wrong_rect.draw(win)
                    wrong_txt.draw(win)
                    wrong_direct.draw(win)

                    #checks click
                    while clicked(click, wrong_bk) == False:

                        click = win.getMouse()
                        
                    else:

                        #undraws rectangles
                        wrong_bk.undraw()
                        wrong_rect.undraw()
                        wrong_txt.undraw()
                        wrong_direct.undraw()
            
            #Checks if the answer is D     
            elif question_dict[keys_list[unit]][4] == 'D':

                #if clicked on the last rectangle
                if clicked(click,rect_lst[0]) == True:

                    #draws the correct rectangles
                    correct_bk.draw(win)
                    correct_rect.draw(win)
                    correct_txt.draw(win)
                    correct_direct.draw(win)
                    score += 1
                    txt_lst[6].setText('Correct: ' + str(score))
                    
                    #checks click again
                    while clicked(click, correct_bk) == False:

                        click = win.getMouse()
                        
                    else: 

                        #undraws
                        correct_bk.undraw()
                        correct_rect.undraw()
                        correct_txt.undraw()
                        correct_direct.undraw()

                #checks for clicks in the other rectangles
                elif (clicked(click,rect_lst[1]) or clicked(click,rect_lst[2]) or clicked(click,rect_lst[3])) == True:

                    #draws
                    wrong_bk.draw(win)
                    wrong_rect.draw(win)
                    wrong_txt.draw(win)
                    wrong_direct.draw(win)

                    #checks clicks
                    while clicked(click, wrong_bk) == False:

                        click = win.getMouse()
                        
                    else:

                        #undaws the rectangles
                        wrong_bk.undraw()
                        wrong_rect.undraw()
                        wrong_txt.undraw()
                        wrong_direct.undraw()

    #Here we draw the final results rectangle background with the same dimensions
    result_bk = Rectangle(Point(100,190),Point(300,290))
    result_bk.setFill('white')
    result_bk.draw(win)

    #Then we draw the final results rectangle that is gold
    result_rect = Rectangle(Point(105,195),Point(295,285))
    result_rect.setFill('gold')
    result_rect.draw(win)

    #We set the texts of both rectangles
    result_txt = Text(Point(200,260), 'Your final score is: ' + str(score))
    result_txt.setStyle('bold')
    result_txt.draw(win)
    result_direct = Text(Point(200,230), 'Click to continue')
    result_direct.setStyle('italic')
    result_direct.draw(win)

    #We check for mouse click
    click = win.getMouse()

    #if not within results rectangle, we keep checking
    while clicked(click,result_bk) == False:
        
        click = win.getMouse()
        
    else:

        #other wise we close the window and return the score
        win.close()
        
    return score
   


#Here we begin to create our creative feature function---------------------
def player():

    #draw a window that allows the user to click 1 or 2 players (1 being the normal version and 2 being the creative version)
    win = GraphWin('Single or Multiplayer', 500, 300)
    win.setBackground('light blue')
    image = Image(Point(250,50), 'LetsPlay.gif')
    image.draw(win)

    #Instructions for the user to let them choose which mode they want to play
    message = Text(Point(255, 120), 'Choose the Number of players! ')
    message.setSize(15)
    message.setStyle('bold')
    message.setFace('courier')
    message.draw(win)

    #rectangle for the user to click if they choose 1 player
    one = Rectangle(Point(110,170),Point(230,210))
    one.setFill('light green')
    one.draw(win)

    #text for the 1 player rectangle
    one_txt = Text(Point(170,190), '1 Player (Normal)')
    one_txt.setSize(10)
    one_txt.draw(win)

    #rectangle for the user to click if they choose 2 players
    two = Rectangle(Point(260,170),Point(380,210))
    two.setFill('light green')
    two.draw(win)

    #text for the 2 player rectangle
    two_txt = Text(Point(320,190), '2 Players')
    two_txt.draw(win)
    
    #back rectangle allows the user the option to go back
    back = Rectangle(Point(0,270),Point(110,300))
    back.setFill('light pink')
    back.draw(win)
    
    #text for the back rectangle
    back_txt = Text(Point(50, 287), '<---- BACK')
    back_txt.setStyle('bold')
    back_txt.draw(win)

    #check for mouseclick
    mouse = win.checkMouse()

    #while the back rectangle is not clicked
    while (clicked(mouse,back)) == False:

        #if the user chooses to click 1 player
        if (clicked(mouse,one)) == True:

            #normal game mode starts and we return 1 to see what button was clicked
            win.close()

            return 1

        #if the second game mode is clicked then we return 2 and the window is closed
        elif (clicked(mouse,two)) == True:

            win.close()

            return 2
            
        else:
        
            mouse = win.checkMouse()
        
    else:

        #if the back rectangle is clicked, we return 0 and the window closes
        win.close()

        return 0



#creates the single player function------------------------
def singleplayer():

    #creates graphics window for single player
    win = GraphWin('Singleplayer', 500,100)
    win.setBackground('light blue')

    #shows which mode the user is in 
    message = Text(Point(250,25), 'Mode: Singleplayer (Normal)')
    message.setSize(14)
    message.setFace('courier')
    message.setStyle('bold')
    message.draw(win)

    #more message
    msg = Text(Point(250,60), 'Good luck!')
    msg.setSize(14)
    msg.setFace('courier')
    msg.setStyle('bold')
    msg.draw(win)

    #if the user decides to change their mind and go back
    back = Rectangle(Point(0,75),Point(100,100))
    back.setFill('light pink')
    back.draw(win)

    #back text in the rectangle
    back_txt = Text(Point(45, 89), '<---- BACK')
    back_txt.setStyle('bold')
    back_txt.draw(win)

    #continue rectangle to continue to the game
    cont = Rectangle(Point(395,75), Point(500,100))
    cont.setFill('light pink')
    cont.draw(win)

    #continue text
    cont_txt = Text(Point(448,89), 'Continue --->')
    cont_txt.setStyle('bold')
    cont_txt.draw(win)


    #if clicked function does not work, check the corner points of that rectangle to make sure that y coordinate of the second
    #corner point is higher than the right. Otherwise the corner points are actually flipped for each other

    #check for mouse click
    click = win.checkMouse()

    #while the back button is not clicked
    while(clicked(click,back) == False):

        #check if the continue button is clicked
        if (clicked(click, cont) == True):

            #if so the windo closes and we return 3
            win.close()

            return 3

        else:

            #otherwise we keep checking for mouse clicks
            click = win.checkMouse()

    else:

        #if the back button is clicked, we return 4 and close the window
        win.close()

        return 4


#creates the multiplayer window which has some intresting feature 
def multiplayer():

    #create entry lst where we can append those entry lists to
    entry_lst = []
    win = GraphWin('Singleplayer', 500,300)
    win.setBackground('light green')

    #Tells the user that they are in multiplayer mode
    message = Text(Point(250,25), 'Mode: Multiplayer')
    message.setSize(14)
    message.setFace('courier')
    message.setStyle('bold')
    message.draw(win)

    #Gives a little message to the user
    msg = Text(Point(250,50), 'May the smartest player win!')
    msg.setSize(14)
    msg.setFace('courier')
    msg.setStyle('bold')
    msg.draw(win)

    #lets the user go back if they change their mind
    back = Rectangle(Point(0,275),Point(100,300))
    back.setFill('light pink')
    back.draw(win)

    #text for the back button
    back_txt = Text(Point(45, 289), '<---- BACK')
    back_txt.setStyle('bold')
    back_txt.draw(win)

    #directs the user
    direct = Text(Point(250, 80), 'Enter player names: ')
    direct.setSize(12)
    direct.setFace('courier')
    direct.setStyle('bold')
    direct.draw(win)

    #shows user where to put their name
    name1 = Text(Point(250, 130), 'Player 1: ')
    name1.setFace('courier')
    name1.setStyle('bold')
    name1.draw(win)

    #shows the second user where to put their name
    name2 = Text(Point(250,200), 'Player 2: ')
    name2.setFace('courier')
    name2.setStyle('bold')
    name2.draw(win)
    
    #entry box for player 1
    player1 = Entry(Point(250,160), 10)
    player1.setFill('white')
    player1.draw(win)

    #append that to our entry list
    entry_lst.append(player1)

    #entry box for player 2
    player2 = Entry(Point(250,230), 10)
    player2.setFill('white')
    player2.draw(win)

    #append the second thing to our entry list
    entry_lst.append(player2)

    #continue box for the user to continue
    cont = Rectangle(Point(395,275), Point(500,300))
    cont.setFill('light pink')
    cont.draw(win)

    #text to continue
    cont_txt = Text(Point(448,289), 'Continue --->')
    cont_txt.setStyle('bold')
    cont_txt.draw(win)

    #checks for mouseclick
    click = win.checkMouse()

    #while the back button is not clicked 
    while(clicked(click,back) == False):

        #if the continue button is clicked
        if (clicked(click, cont) == True):

            #close window and return a number and an entry list
            win.close()

            return (5, entry_lst)

        else:

            #else check for mouse click
            click = win.checkMouse()

    else:

        #close the window and return the entry list
        win.close()

        return (6, entry_lst)


#prompt function guides the user to the next screen and checks if the user is ready or not with a mouse click
def prompt(mystring):

    #creates graphic window that is light green
    win = GraphWin('User Guide', 500, 100)
    win.setBackground('light green')

    #takes a string and formats it so the correct user is aware and ready 
    message = Text(Point(250, 50), "It is " + mystring + "'s turn right now")
    message.setFace('courier')
    message.setStyle('bold')
    message.setSize(16)
    message.draw(win)

    #waits for mouse click then closes
    win.getMouse()
    win.close()

#Creates the result window which displays the winner 
def result(score_lst, entry_lst):

    #initalize text list to use it later
    txt_lst = []
    
    #create graphisc window
    win = GraphWin('Results', 500, 300)

    #create header reactangle
    top = Rectangle(Point(0,0),Point(500,50))
    top.setFill('gold')
    top.draw(win)

    #create a light green background for the top of the window
    first = Rectangle(Point(0,50), Point(500,175))
    first.setFill('light green')
    first.draw(win)

    #creates the light blue rectangle for the bottom of the window
    second = Rectangle(Point(0,175),Point(500,300))
    second.setFill('light blue')
    second.draw(win)

    #all these lines are to create a frame affect around the boundaries
    aline = Line(Point(0,50),Point(500,50))
    aline.setWidth(3)
    aline.draw(win)

    bline = Line(Point(0,175), Point(500,175))
    bline.setWidth(3)
    bline.draw(win)

    cline = Line(Point(0,2), Point(500,2))
    cline.setWidth(3)
    cline.draw(win)

    dline = Line(Point(498,0), Point(498,300))
    dline.setWidth(3)
    dline.draw(win)

    eline = Line(Point(2,0), Point(2,300))
    eline.setWidth(3)
    eline.draw(win)

    fline = Line(Point(0,298),Point(500,298))
    fline.setWidth(3)
    fline.draw(win)

    #At the top of the rectangle it has the results header
    title = Text(Point(250, 30), 'RESULTS')
    title.setTextColor('black')
    title.setSize(26)
    title.setFace('courier')
    title.setStyle('bold')
    title.draw(win)

    #waits for the user to click in order to display the results
    win.getMouse()

    #after mouse click it displays the winner at the top of the rectangle
    message = Text(Point(250,70), 'The winner of Trivia Trinko gameplay is...')
    message.setSize(13)
    message.setFace('courier')
    message.setStyle('bold')

    #append it to a text list
    txt_lst.append(message)
    

    #displays empty string where the winners name will be inserted
    winner = Text(Point(250, 140), '')
    winner.setSize(20)
    winner.setStyle('bold')
    winner.setFace('courier')

    #append it to the text list
    txt_lst.append(winner)

    #two circles that look like chips on either side of the name
    circle1 = Circle(Point(50,140),15)
    circle1.setFill('gold')

    circle2 = Circle(Point(450,140), 15)
    circle2.setFill('gold')

    #fun message for the loser 
    msg = Text(Point(250, 195), 'The loser and the dumber of the two players is...')
    msg.setSize(13)
    msg.setFace('courier')
    msg.setStyle('bold')
    txt_lst.append(msg)

    #sets the text for the loser
    loser = Text(Point(250, 255), '')
    loser.setSize(20)
    loser.setStyle('bold')
    loser.setFace('courier')


    #two more circles that look like chips on both sides of the name
    circle3 = Circle(Point(50,255),15)
    circle3.setFill('gold')
    
    circle4 = Circle(Point(450,255), 15)
    circle4.setFill('gold')

    
    tie = Text(Point(250,70), 'Everyone is a winner!')
    tie.setSize(13)
    tie.setFace('courier')
    tie.setStyle('bold')
    
    tie2 = Text(Point(250,195), 'Everyone is a winner!')
    tie2.setSize(13)
    tie2.setFace('courier')
    tie2.setStyle('bold')

    #if the first user wins
    if score_lst[0] > score_lst[1]:

        #we draw the message for the winner
        message.draw(win)
        circle2.draw(win)
        circle1.draw(win)
        loser.draw(win)
        circle4.draw(win)
        circle3.draw(win)
        winner.draw(win)
        msg.draw(win)

        #winner text is set with the winners name
        winner.setText(entry_lst[0].getText() + ' (' + str(score_lst[0]) + ')')
        loser.setText(entry_lst[1].getText() + ' (' + str(score_lst[1]) + ')')

    #else if the second user wins
    elif score_lst[1] > score_lst[0]:

        #draw the message for the loser
        message.draw(win)
        winner.draw(win)
        msg.draw(win)
        circle2.draw(win)
        circle1.draw(win)
        loser.draw(win)
        circle4.draw(win)
        circle3.draw(win)
         
        #winner text is set with the second users name
        winner.setText(entry_lst[1].getText()+ ' (' + str(score_lst[1]) + ')')
        loser.setText(entry_lst[0].getText() + ' (' + str(score_lst[0]) + ')')


    else:

        #This is incase everyone gets the same score at which case we draw the tie message
        tie.draw(win)
        winner.draw(win)
        loser.draw(win)
        circle2.draw(win)
        circle1.draw(win)
        tie2.draw(win)
        circle4.draw(win)
        circle3.draw(win)

        #Here it doesn't matter whose name is displayed in what box
        winner.setText(entry_lst[1].getText()+ ' (' + str(score_lst[0]) + ')')
        loser.setText(entry_lst[0].getText() + ' (' + str(score_lst[0]) + ')')

        
    #allows the user to exit and return back to the control after the click
    win.getMouse()
    win.close()
    
    
    

#Here we connect everything with this main function
def main():
    
    #controls the main window. As long as the switch is True, the game is running
    switch = True

    #game runs when the switch is true
    while switch == True:

        #decide gives us the players decision from the control window
        decide = control()

        #if the player clicks play, we continue
        if decide == True:

            #we initalize our score_lst and so it resets each time function goes back to control
            score_lst = []

            #we call on the player function
            play = player()

            #then we use a similar method to connect our multiplayer and singleplayer function
            play_switch  = True
            
            #if the play switch is true, we run the next few steps
            while play_switch == True:

                #if the player chooses to play, we take the returned value which is set to be 1
                if play == 1:

                    #we call on the singleplayer function
                    single = singleplayer()

                    #if the player chooses to continue, the returned value will be 3 so we continue
                    if single == 3:
                        
                        x = takeQuiz()

                        #sets the return values of board (window and exit rectangle) to grid and Exit variables
                        grid, chips, score = board()

                        #we call the bins() function and give our graphic window as a parameter 
                        bins(grid)

                        #We set the returned list of pin circles to a variable
                        Pin_list = pins(grid)

                        drop(x, grid, Pin_list, score, chips)

                    #else if he clicks the back function
                    elif single == 4:

                        #Play switch is set to False and that brings us back to the original control function
                        play_switch = False

                    #else the play switch changes to false after the function ends and brings us back to the control function
                    play_switch = False

                #otherwise if the second button is clicked
                elif play == 2:

                    #we call the multiplayer function
                    (multi, entry_lst) = multiplayer()

                    #if the continue function is clicked
                    if multi == 5:
                            
                        #runs the quiz funtion twice for both players
                        #for loop that runs twice for both players
                        #mouse click already in prompt function which allows the program to wait for user
                        for i in range(0,2):

                            #we get the text from the entry boxes
                            text = entry_lst[i].getText()

                            #get text from entry lst and pass that as a paremeter for the prompt() function
                            prompt(text)

                            #call the takequiz function 
                            x = takeQuiz()

                            #sets the return values of board (window and exit rectangle) to grid and Exit variables
                            grid, chips, score = board()

                            #we call the bins() function and give our graphic window as a parameter 
                            bins(grid)

                            #We set the returned list of pin circles to a variable
                            Pin_list = pins(grid)

                            #pass all the values into our drop function and return points
                            points = drop(x, grid, Pin_list, score, chips)

                            #then we append the points to our score list
                            score_lst.append(points)

                        #Then we call our results function 
                        result(score_lst, entry_lst)
                        

                    #otherwise if the back button is clicked, brings user back to control
                    elif multi == 6:

                        #by switching the play switch to false and not running the while loop
                        play_switch = False

                    #else affter the function runs, the play switch is set to false so that user is brought back to control
                    play_switch = False

                #other wise if the user chose to go back from the player() function, goes back to control
                elif play == 0:

                    play_switch = False
        
        #if the exit function is clicked, switch becomes false, executing the entire program
        else:

            #and if the user chooses to exit the function, the main switch is set to false exiting the entire program
            switch = False




main()

