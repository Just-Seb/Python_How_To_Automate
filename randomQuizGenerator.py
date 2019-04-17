#! python3
# randomQuizGenerator.py - Creates quizzes with question and answers
# random order, along with the answer key.

import random
import os

os.chdir('C:\\Users\\seb7426\\python_text_adventure-master\\Generated Tests')

# The quiz data. Keys are provinces and values are their capitols.
capitals = {'Ontario': 'Toronto', 'British Colombia': 'Victoria', 'Quebec': 'Quebec City', 'Alberta': 'Edmonton', 'Nova Scotia': 'Halifax Regional Municipality', 'Saskatchewan': 'Regina', 'Manitoba': 'Winnipeg', 'New Brunswick': 'Fredericton', 'Newfoundland': 'St. John\'s', 'Prince Edward Island': 'Charlottetown'}

print("How mant tests do you want?")
numofTests = input()
numofTests = int(numofTests)
print("Where do you want these tests to be put?")
location = input()
location = str(location)
os.chdir(location)
# Generate 35 quiz files.
for quizNum in range(numofTests):
    # Create the quiz and answer key files.
    quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')
    answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')

    # Write out the header for the quiz.
    quizFile.write('Name:\nDate:\nPeriod:\n')
    quizFile.write((' ' * 20) + 'State Capitols Quiz (Form %s)' % (quizNum + 1))

    quizFile.write('\n\n')

    # Shuffle the order of the states.
    provinces = list(capitals.keys())
    random.shuffle(provinces)

    # Loop through all 10 provinces, making a question for each.
    for questionNum in range(10):
        # Get right and wrong answers.
        correctAnswer = capitals[provinces[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        # Write the question and answer options to the quiz file.
        quizFile.write('%s. What is the capitol of %s?\n' % (questionNum + 1, provinces[questionNum]))

        for i in range(4):
            quizFile.write(' %s. %s\n' % ('ABCD'[i],answerOptions[i]))

        quizFile.write('\n')

        # Write the answer key to a file.
        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerKeyFile.close()
