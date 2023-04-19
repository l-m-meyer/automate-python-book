#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.


import random, re


def start_quiz(data, quiz_topic, quiz_title, num_questions):
    # Generate quiz files.
    for quizNum in range(num_questions):
        quizFile, answerKeyFile = generate_quiz_files(quiz_topic, quiz_title, quizNum)
        get_questions_answers(data, quizFile, answerKeyFile)


def get_questions_answers(data, quizFile, answerKeyFile):
    # Shuffle the order of the subjects.
    subjects = list(data.keys())
    random.shuffle(subjects)

    # Loop through all subjects, making a question for each.
    for questionNum in range(len(data)):
        # Get right and wrong answers.
        correctAnswer = data[subjects[questionNum]]
        wrongAnswers = list(data.values())
        
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        quizFile, answerKeyFile = write_to_files(subjects, questionNum, quizFile, answerKeyFile, correctAnswer, answerOptions)

    quizFile.close()
    answerKeyFile.close()


def write_to_files(subjects, questionNum, quizFile, answerKeyFile, correctAnswer, answerOptions):
    # Write the question and answer options to the quiz file.
    quizFile.write(f'{questionNum + 1}. What is the {re.sub("s$", "", quiz_topic)} of {subjects[questionNum]}?\n')
    for i in range(4):
        quizFile.write(f"   {'ABCD'[i]}. {answerOptions[i]}\n")
        quizFile.write('\n')

    # Write the answer key to a file.
    answerKeyFile.write(f"{questionNum + 1}. {'ABCD'[answerOptions.index(correctAnswer)]}\n")

    return quizFile, answerKeyFile


def generate_quiz_files(quiz_topic, quiz_title, quizNum):
    # Create the quiz and answer key files.
    quizFile = open(f'{quiz_topic}quiz{quizNum + 1}.txt', 'w')
    answerKeyFile = open(f'{quiz_topic}quiz_answers{quizNum + 1}.txt', 'w')

    # Write out the header for the quiz.
    quizFile.write('Name:\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + f'{quiz_title} Quiz (Form{quizNum + 1})')
    quizFile.write('\n\n')

    return quizFile, answerKeyFile


if __name__ == '__main__':
    # The quiz data. Keys are states and values are their capitals.
    capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
   'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines',
   'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge',
   'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston',
   'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
   'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln',
   'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
   'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville',
   'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier',
   'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
   'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
    quiz_topic = 'capitals'
    quiz_title = 'State Capitals'
    num_questions = 35
    start_quiz(capitals, quiz_topic, quiz_title, num_questions)