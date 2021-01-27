import random
import pyinputplus as pyip

#? Prompts the user to enter the number of quizzes they would like to generate
print('How many quizzes would you like to generate?')
quizzesToCreate = pyip.inputNum('Enter a number: ')

#? Quiz Data, keys are the states, and values are their capitals
capitals = {
    'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
    'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
    'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
    'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
    'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
    'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
    'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
    'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
    'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 
    'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 
    'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
    'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
    'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
    'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'WestVirginia': 'Charleston', 
    'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'
   }

#? Generates a random quiz the specified amount of times
for quizNum in range(quizzesToCreate):
    #? Create quiz and answer key files
    quizFile = open(f'students/capitalsQuiz{quizNum + 1}.txt', 'w')
    answerKeyFile = open(f'admin/capitalsquiz_answers{quizNum + 1}.txt', 'w')

    #? Write out the header for the quiz
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write(f'State Capitals Quiz (Form {quizNum + 1})'.rjust(20, ' '))
    quizFile.write('\n\n')

    #? Shuffle the order of the states
    states = list(capitals.keys())
    random.shuffle(states)

    #? Loop through all 50 states, making a question for each
    for quesNumb, state in enumerate(states):
        correctAnswer = capitals[state]
        wrongAnswers = list(capitals.values())
        #* deletes the correct answer from the wrong answer list
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        #? Write the question and the answer options to the quiz file or answer key file
        quizFile.write(f'\n\n{quesNumb + 1}. What is the capital of {state}?\n')
        for answerChoiceNumb, answerChoice in enumerate(answerOptions):
            quizFile.write(f'{"ABCD"[answerChoiceNumb]}. {answerChoice}'.rjust(len(answerChoice) + 7, ' '))
            quizFile.write('\n')

        
        answerKeyFile.write(f"{quesNumb + 1}.{'ABCD'[answerOptions.index(correctAnswer)]}\n")
    quizFile.close()
    answerKeyFile.close()
