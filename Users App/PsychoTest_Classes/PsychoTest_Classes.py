#Library for Psychometry Automated Analysis
#Made by @gilbear and @gilkzxc


import datetime
import requests
from PyInquirer import prompt, Separator

ChapterTypes = { "language": 23,"math": 20,"english": 22 } # a dictionary to set the diffrent types of Psychometry chapters
OnlineDB_GET_Response = requests.get("https://raw.githubusercontent.com/FXP-Pscyhometery/FXP-Psychometry-Analyser/master/DataBase.json")
cancelKeyWordOfRetrievers = "DON'T RETRIEVE ANY!"

def PyInquirer_prompt_wrapper_listReady(message,choices):
    question = [{'type':'list','name':'option','message':message,'choices':choices}]
    return prompt(question)["option"]

def chapterTypeGenerator():
     title = "Choose the type of this chapter:"
     options = ["language","math","english"]
     option = PyInquirer_prompt_wrapper_listReady(title,options)
     return option

def newInputChapterGenerator(onlineDataBase):
    print("\n"+"New chapter:"+"\n"+"-"*15)
    yearOfChapter = PyInquirer_prompt_wrapper_listReady("Choose the year of the test/pdf, the chapter is from. :",list(onlineDataBase.keys()))
    periodOfChapter = PyInquirer_prompt_wrapper_listReady("Choose the period of the test/pdf, the chapter is from. :",list(onlineDataBase[yearOfChapter].keys()))
    typeOfChapter = PyInquirer_prompt_wrapper_listReady("Choose the type of this chapter :",list(onlineDataBase[yearOfChapter][periodOfChapter].keys()))
    numberOfChapter = PyInquirer_prompt_wrapper_listReady("Choose the ID of the Chapter (For example math 1 or math 2):",list(onlineDataBase[yearOfChapter][periodOfChapter][typeOfChapter].keys()))
    tempChapter = PsychoTest_chapter(typeOfChapter, numberOfChapter, periodOfChapter, yearOfChapter)
    tempChapter.enterAnswers()
    print("This is the chapter you have entered: ")
    print(tempChapter)
        
    while PyInquirer_prompt_wrapper_listReady("Are all the answers that had been entered are correct? :",["yes","no"]) == "no":
        tempChapter.modifyAnswers()
        print("This is the chapter you have entered: ")
        print(tempChapter)
    return tempChapter
        


logo = """
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
 .mmmmmmd/.hmm+   +mms `dmmmmdhs-       -mmmmmdho`  -sdmNNmd`:dmd`   ymd-  -sdmNNmd` +md/    `mmh    :sdNNNdy/    ymmmy     :mmmd.  ymmmmmdy hmdmmmmmmd+ ommmdddy+` smds   .dmh`             
 .MMm////. .mMM/ oMMs  `MMN:/oNMM:      :MMh:/sMMN.:MMm/--/o` +MMd` sMM/ .dMMh+///o` oMM+    `MMN  `dMMh+//yMMm.  mMNMM+   `NMNMM.  mMM+///: ://oMMm///- yMMo:/hMMh  hMM+ `mMm.              
 .MMd       `hMMyMM+   `MMm   yMM+      :MMy  `NMM-:MMNs:`     +MMyoMM/  dMM+        oMMs::::/MMN  hMMo     oMMh  mMdyMN.  yMhdMM.  mMM-...`    -MMd     yMM:  oMMy  `hMM/dMm.               
 .MMMMMMM    `NMMMs    `MMMhhmMMy`      :MMmhhNMN+  -smMMMd+    +MMMM/  `MMM`        oMMMMMMMMMMN  NMM-     -MMN  mMd`mMd /MN`dMM.  mMMMMMM+    -MMd     yMMNmNMh/    `hMMMm`                
 .MMd....   -mMmsMMs   `MMN++/:`        :MMd++/-       `:mMMo    yMMo    mMMo        oMM+    `MMN  hMMs     sMMy  mMd -MMsNM: dMM.  mMM.        -MMd     yMMo:hMNo     `NMM.                 
 .MMd      /MMm. +MMd` `MMm             :MMy       /ho//+mMM/    sMM+    -mMMmsoosd. oMM+    `MMN  `hMMdsosdMMy`  mMd  oMMMs  dMM.  mMMsoooo    -MMd     yMM:  oMMh.    NMM`                 
 .hho     :hhy`   /hhs``yhs             -hh+       -shdddho-     /hh:      :shdddhs` /hh:    `hhy    -oydddy+.    shs   shy`  ohh.  shhhhhhy`   .hhs     +hh-   :hhs`   yhy`                 
://////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////-             
.------------------------------------------------------------------------------------------------------------------------------------------------------------------------------`             
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                
"""

class PsychoTest_chapter: #A class for a psychometry generic-type chapter
    
    def __init__(self, typeOfChapter, numberOfChapter, period, year, q_a = None): #Constructor
        self.typeOfChapter = typeOfChapter
        self.numberOfChapter = numberOfChapter
        self.period = period
        self.year = year
        if q_a == None:
            self.q_a = [0]*ChapterTypes[typeOfChapter]
        else:
            self.q_a = q_a

    def enterAnswers(self): # A function, that lets the user enter his answers to the chapter Object.
        print("Entered blank/new chapter state, enter answers now:")
        for i in range(len(self.q_a)):
            digit = input(f"Answer to question number {i+1}: ")
            if not digit.isdigit() or not int(digit) in range(1,5):
                print("Invalid input, please enter again!")
                digit = input(f"Answer to question number {i+1}: ")
            if not digit.isdigit() or not int(digit) in range(1,5):
                print("Again invalid input, restarting answers fill.....")
                return self.enterAnswers()
            self.q_a[i]= int(digit)
        print("Finished entering answers to this chapter!")

    def modifyAnswers(self): #Chapter answer modify
        print("Entered chapter modify state:")
        Times = input("How many q&a you want to modify?: ")
        if not Times.isdigit():
            print("Invalid input, please enter again!")
            Times = input("How many q&a you want to modify?: ")
        if not Times.isdigit():
            print("Again invalid input, restarting answers fill.....")
            return self.modifyAnswers()
        Times = int(Times)
        for i in range(Times):
            q= input("Enter number of question: ")
            if not q.isdigit() or not int(q) in range(1,len(self.q_a) + 1):
                print("Invalid input, please enter again!")
                q= input("Enter number of question: ")
            if not q.isdigit() or not int(q) in range(1,len(self.q_a) + 1):
                print("Again invalid input, restarting answers fill.....")
                return self.modifyAnswers()
            q = int(q)
            a= input("Enter number of answer: ")
            if not a.isdigit() or not int(a) in range(1,5):
                print("Invalid input, please enter again!")
                a= input("Enter number of answer: ")
            if not a.isdigit() or not int(a) in range(1,5):
                print("Again invalid input, restarting answers fill.....")
                return self.modifyAnswers()
            a = int(a)
            self.q_a[q-1]=a
        print("Finished modifying!")
    def __repr__(self): #Debuging form of repersantation of Chapter object
        return { self.year: { self.period:{ self.typeOfChapter:{ self.numberOfChapter: self.q_a } } } }
    def __str__(self): #User form of repersantation of Chapter object
        answer = f" Psychometry {self.typeOfChapter} chapter , Number: {self.numberOfChapter}, from the {self.period} {self.year} Edition: \nQuestions and Answers:\n"+"#"*40+"\n"
        
        for i in range(len(self.q_a)):
            answer += f"| Question number {i+1} | Answer number {self.q_a[i]} |\n"
        answer+= "#"*40
        return answer


    def compareWith_q_a_excluded(self, Chapter1): #When you want to check if an Chapter obj is the same of another, but not checking the q_a.
        if (Chapter1 == None) or (not isinstance(Chapter1,PsychoTest_chapter)):
            return False
        return (self.typeOfChapter==Chapter1.typeOfChapter) and (self.numberOfChapter==Chapter1.numberOfChapter) and (self.period==Chapter1.period) and (self.year==Chapter1.year)
    def is_q_a_Empty(self): # Returns True if the answers of the chapter obj is empty or if the chapter is new. Else, of course returns False.
        return self.q_a == [0]*ChapterTypes[self.typeOfChapter]
    def checkAnswers(self,DataBase): # Investigate given chapter with a given DataBase, and returns the analysis result.
        if DataBase == {}:
            return "Empty DataBase"
        if not self.year in DataBase:
            return "Year of chapter isn't in DataBase. Maybe cause you wrote it wrong?"
        if not self.period in DataBase[self.year]:
            return "Period of chapter isn't in DataBase. Maybe cause you wrote it wrong?"
        if not self.typeOfChapter in DataBase[self.year][self.period]:
            return "Type of chapter isn't in DataBase. Maybe cause you wrote it wrong?"
        if not self.numberOfChapter in DataBase[self.year][self.period][self.typeOfChapter]:
            return "ID number of chapter isn't in DataBase. Maybe cause you wrote it wrong?"
        if DataBase[self.year][self.period][self.typeOfChapter][self.numberOfChapter] == [0]*ChapterTypes[self.typeOfChapter]:
            return "Please contact Forum managment, the chapter's answers ( q_a ) at DataBase is empty."
        if self.is_q_a_Empty():
            print("For some reason, the chapter is empty, meaning it doesn't have your answers filled.")
            if PyInquirer_prompt_wrapper_listReady("Would you like to enter/reenter the answers? :",["yes","no"]) == "yes":
                self.enterAnswers()
            else:
                return "Tried to check an empty chapter."
        answer = {}
        answer["checkedAnswers"] = {}
        counterForCorrectAnswers = 0
        for i in range(len(self.q_a)):
            if self.q_a[i] == DataBase[self.year][self.period][self.typeOfChapter][self.numberOfChapter][i]:
                counterForCorrectAnswers += 1
                answer["checkedAnswers"][i] = ["V"]
            else:
                answer["checkedAnswers"][i] = ["X",DataBase[self.year][self.period][self.typeOfChapter][self.numberOfChapter][i]]
        answer["numberOfCorrectAnswers"] = f"{counterForCorrectAnswers}/{ChapterTypes[self.typeOfChapter]}"
        answer["successPercentage"] = f"{100*counterForCorrectAnswers/ChapterTypes[self.typeOfChapter]:.2f}%"
        strTitle = f" Psychometry {self.typeOfChapter} chapter , Number: {self.numberOfChapter}, from the {self.period} {self.year} Edition: \nQuestions and Answers:\n"+"#"*60+"\n"
        answer["__str__"] = {}
        answer["__str__"]["with_out_actual_correct_answers"] = strTitle
        answer["__str__"]["with_actual_correct_answers"] = strTitle
        answer["__str__"]["with_out_actual_correct_answers"] += f"| Question number | Your answer's number | Is it correct? (V for yes, and X for no) |\n"
        answer["__str__"]["with_actual_correct_answers"] += f"| Question number | Your answer's number | Is it correct? (V for yes, and X for no) | The actual correct answer's number (Filled only if you did a mistake!) |\n"
        for i in range(len(self.q_a)):
            answer["__str__"]["with_out_actual_correct_answers"] += f"| {i+1} | {self.q_a[i]} | {answer['checkedAnswers'][i][0]} |\n"
            tempStr = " "
            if len(answer["checkedAnswers"][i])>1:
                tempStr = answer["checkedAnswers"][i][1]
            answer["__str__"]["with_actual_correct_answers"] += f"| {i+1} | {self.q_a[i]} | {answer['checkedAnswers'][i][0]} | {tempStr} |\n"
        answer["__str__"]["with_out_actual_correct_answers"] += "#"*60 +f"\nNumber of chapter's correct answers: {answer['numberOfCorrectAnswers']}.\nChapter's success percentage: {answer['successPercentage']}.\n"+"#"*60
        answer["__str__"]["with_actual_correct_answers"] += "#"*60 +f"\nNumber of chapter's correct answers: {answer['numberOfCorrectAnswers']}.\nChapter's success percentage: {answer['successPercentage']}.\n"+"#"*60

        return answer

    def __eq__(self,otherChapter):
        if not isinstance(otherChapter,PsychoTest_chapter):
            return False
        return self.compareWith_q_a_excluded(otherChapter) and (self.q_a == otherChapter.q_a)
    def __hash__(self):
        return hash((self.year,self.period,self.typeOfChapter,self.numberOfChapter,str(self.q_a)))
    def addingToDataBase(self,DataBaseDict):#Transforms the object to Dict form and prepare it to be added. Only adds if not exist beforehand.
        if not self.year in DataBaseDict:
            DataBaseDict[self.year] = {}
        if not self.period in DataBaseDict[self.year]:
            DataBaseDict[self.year][self.period] = {}
        if not self.typeOfChapter in DataBaseDict[self.year][self.period]:
            DataBaseDict[self.year][self.period][self.typeOfChapter] = {}
        if self.numberOfChapter in DataBaseDict[self.year][self.period][self.typeOfChapter]:
            return False #Returns False if the chapter exists.
        DataBaseDict[self.year][self.period][self.typeOfChapter][self.numberOfChapter] = self.q_a
        return True #Return true if it added the chapter to DataBaseDict.






class PsychoTest_test:

    def __init__(self, nameOfTest=""):
        if nameOfTest == "":
            self.nameOfTest = self.newName()
        else:
            self.nameOfTest = nameOfTest
        self.chapters  = []
        self.creationOfTestObject_DateTime = str(datetime.datetime.now())
        self.test_results = {}
    def newName(self):
        nameOfNewTestObject = input("Enter a name of your choice for your test. : ")
        if nameOfNewTestObject == cancelKeyWordOfRetrievers:
            print("You little trouble maker, you have chosen a prohibited name from usage for a test.\nSorry. :)\nTherefore please type a valid new name.")
            return self.newName()
        return nameOfNewTestObject
    def addChapter(self,newChapter):
        if not isinstance(newChapter, PsychoTest_chapter):
            return "Not Added, you have not used an argument that is the correct type of Object or have entered None."
        if newChapter.is_q_a_Empty():
            newChapter.enterAnswers()
        if self.chapters != []:
            for i in self.chapters:
                if newChapter.compareWith_q_a_excluded(i):
                    print(f"You have this chapter already in this Test, that named {self.nameOfTest}.")
                    if PyInquirer_prompt_wrapper_listReady("Would you liked to replace the previous chapter? :",["yes","no"]) == "yes":
                        i.q_a = newChapter.q_a
                        return "Old Chapter was replaced."
                    elif PyInquirer_prompt_wrapper_listReady("Would you liked to modify the previous chapter's answers only? :",["yes","no"]) == "yes":
                        i.modifyAnswers()
                        return "Old Chapter was modified."
                    return "No changes."
        self.chapters.append(newChapter)
        return f"New chapter was added to {self.nameOfTest} test. The test which was created on {self.creationOfTestObject_DateTime}. "
    def check_test(self,onlineDataBase):
        if self.chapters == []:
            return f"No chapters in this test that is named {self.nameOfTest}, and  that was created at {self.creationOfTestObject_DateTime} to check."
        print(f"Checking Test that is named {self.nameOfTest}, and that was created at {self.creationOfTestObject_DateTime}:")
        if self.test_results != {}:
            for i in self.chapters:
                print(self.test_results[i.year][i.period][i.typeOfChapter][i.numberOfChapter]["Result"]["__str__"]["with_out_actual_correct_answers"])
            if PyInquirer_prompt_wrapper_listReady("Would you like to see the actual correct answers? :",["yes","no"]) == "yes":
                for i in self.chapters:
                    print(self.test_results[i.year][i.period][i.typeOfChapter][i.numberOfChapter]["Result"]["__str__"]["with_actual_correct_answers"])
            return f"Finished checking the test that is named {self.nameOfTest}, and that was created at {self.creationOfTestObject_DateTime}. "
        for i in self.chapters:
            chapterAnalysis = i.checkAnswers(onlineDataBase)
            if isinstance(chapterAnalysis,dict) and (chapterAnalysis != {}):
                print(chapterAnalysis["__str__"]["with_out_actual_correct_answers"])
                if i.addingToDataBase(self.test_results):
                    self.test_results[i.year][i.period][i.typeOfChapter][i.numberOfChapter] = {"q_a": i.q_a, "Result":chapterAnalysis}
                else:
                    print("Error: addingToDataBase() returned False, and test_result of {self.nameOfTest} is empty!!")
        if PyInquirer_prompt_wrapper_listReady("Would you like to see the actual correct answers? :",["yes","no"]) == "yes":
            for i in self.chapters:
                print(self.test_results[i.year][i.period][i.typeOfChapter][i.numberOfChapter]["Result"]["__str__"]["with_actual_correct_answers"])
        return f"Finished checking the test that is named {self.nameOfTest}, and that was created at {self.creationOfTestObject_DateTime}. "
    def __str__(self):
        answer = "#"*60+"\n"+f"""
        Test:
            Name of test: {self.nameOfTest}
            This test was created at {self.creationOfTestObject_DateTime} .
            \n"""
        if self.chapters == []:
            return answer+ "\nThis test is empty, there weren't any chapters added."
        if self.test_results == {}:
            return answer+"\nTest wasn't checked yet. Please go to Analyse Test or Check Test."
        answer += "#"*30+"\nChapters analysis conclusion:\n"
        for i in self.chapters:
            answer += "-"*20+"\n"
            answer += f" Psychometry {i.typeOfChapter} chapter , Number: {i.numberOfChapter}, from the {i.period} {i.year} Edition.\n"
            answer += f"Answerd correctly: {self.test_results[i.year][i.period][i.typeOfChapter][i.numberOfChapter]['Result']['numberOfCorrectAnswers']}\n"
            answer += f"Success rate at this chapter is {self.test_results[i.year][i.period][i.typeOfChapter][i.numberOfChapter]['Result']['successPercentage']}\n"
            answer += "-"*20+"\n"
        answer += "#"*30 +"\n"+"#"*60+"\n"
        return answer
        
    def intoDataBase(self,DB):
        if not isinstance(DB,dict):
            return False #No action was taken since parameter isn't a dictionary, so returns false for no action happend.
        if self.nameOfTest in DB:
            print("You already have a test with the same name.")
            if PyInquirer_prompt_wrapper_listReady("Do you wish to choose a different name for the new test? :",["yes","no"]) == "yes":
                self.nameOfTest = self.newName()
                DB[self.nameOfTest] = {self.creationOfTestObject_DateTime:self.test_results}
                return True
            elif PyInquirer_prompt_wrapper_listReady("Do you wish to add a new version with the same name, but different time of creation? :",["yes","no"]) == "yes":
                DB[self.nameOfTest][self.creationOfTestObject_DateTime] = self.test_results
                return True
        DB[self.nameOfTest] = {self.creationOfTestObject_DateTime:self.test_results}
        return True
    @classmethod
    def fromDataBase(cls,nameOfTest,creationOfTestObject_DateTime,DB):
        if not isinstance(DB,dict):
            return False #No action was taken since parameter isn't a dictionary, so returns false for no action happend.
        newTestObject = cls(nameOfTest)
        newTestObject.creationOfTestObject_DateTime = creationOfTestObject_DateTime
        newTestObject.test_results = DB[nameOfTest][creationOfTestObject_DateTime]
        for year in newTestObject.test_results:
            for period in newTestObject.test_results[year]:
                for typeOfChapter in newTestObject.test_results[year][period]:
                    for numberOfChapter in newTestObject.test_results[year][period][typeOfChapter]:
                        newTestObject.chapters.append(PsychoTest_chapter(typeOfChapter,numberOfChapter,period,year,newTestObject.test_results[year][period][typeOfChapter][numberOfChapter]["q_a"]))

        return newTestObject



                



    
                  
        
                    
                        


