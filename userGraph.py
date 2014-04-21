import json

#overall data structure is a graph
#users are nodes
#matches are lines

#just a list of all user objects
class users:

    def __init__(self):
        self.userList = []
        self.matches = []

    def add_user(self,user):
        self.userList.append(user)

    def make_matches(self):
        #match everyone with everyone
        for i in range(len(self.userList)):
            user1=self.userList[i]
            for j in range(i,len(self.userList)):
                user2=self.userList[j]
                #relying on the fact that no two ppl have the same name
                if (user1.name!=user2.name):
                    #compare
                    self.matches.append(match(user1,user2))

    def print_matches(self):
        for match in self.matches:
            print match.user1.name,"&",match.user2.name,match.sumMatch
            
        

#each user has a few variables
#name: the name of the user
#answers: a list of their responses in order of the questions asked
#this list assumes all answers were in the proper order
#matches: a list of scores that show how similiar each answer is to one another
#
#each user needs to be compared with each other user
#to do so, iterate over the list of answers
#send the two strings into some comparison algorithm
#this might be home brew, or might be through an external API
#if they are the same, mark that answer as similiar
class user:

    def __init__(self,*name):
        self.name = name
        self.questions = []
        self.answers = []
        self.matches = []

    def set_name(self,name):
        self.name=name

    def add_answer(self,answer):
        self.answers.append(answer)
        
    def add_question(self,quesiton):
        self.questions.append(question)

    def compare_answers(self,answerIndex,user2):
        #compare the answers of this user to the answer of another user
        #the following is a hilariously useless example
        if (user2.answers[answerIndex]==self.answers[answerIndex]):
            #print user2.answers[answerIndex]," == ",self.answers[answerIndex]
            return 1
        else:
            #print user2.answers[answerIndex]," != ",self.answers[answerIndex]
            return 0

#each match is like a line in the graph connecting two users
#matches is a list of numbers the compare the users
#these lists correspond with the "answers" list in each user object
#the number (from 0 to 1) shows how similiar their answers were
class match:

    def __init__(self,user1,user2):
        self.matches=[]
        self.user1=user1
        self.user2=user2
        self.sumMatch=0
        num_answers=len(user1.answers)
        num_answers2=len(user2.answers)
        if (num_answers!=num_answers2):
            print "error-unequal length answer arrays:",num_answers,num_answers2
        else :
            for i in range(num_answers):
                matchness=user1.compare_answers(i,user2)
                self.sumMatch=self.sumMatch+matchness
                self.matches.append(matchness)
                #add match to each user so everyone knows how well matched they are with everyone else
                user1.matches.append(matchness)
                user2.matches.append(matchness)

if __name__ == '__main__':

    users = users()
    json_file=open('roomate_data.json','r')
    data=json.load(json_file)
    content = data['data']
    for post in content:
        #post is the giant string of all the questions/answers
        message = post['message']
        newUser = user()
        #split by new line
        lastStop=0
        for i in range(len(message)):
            if (message[i]=='\n'):
                line = (message[lastStop:i])
                lastStop=i+1
                #check for name
                for c in range(len(line)):
                    #split by colon
                    if (line[c]==':'):
                        question=line[0:c]
                        answer=line[c+1:len(line)]
                        if (question=='Name'):
                            newUser.add_question(question)
                            newUser.set_name(answer)
                        else:
                            newUser.add_question(question)
                            newUser.add_answer(answer)
        users.add_user(newUser)
    users.make_matches()
    users.print_matches()
