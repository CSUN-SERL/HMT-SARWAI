from __future__ import print_function

import pandas as pd

class SurveyToDatabase:
    def __init__(self):


    def convert (file):

        data = pd.read_csv(file)
        data.drop(index=0)

        survey_name = data.iloc[0][0]
        question_query = "INSERT INTO dbsurveys.question (id, type, question_text) values"
        offered_answer_query = "INSERT INTO dbsurveys.question (id, offered_answer_text) values"

        answers = []

        for index, row in data.iterrows():
            question_text = row['Question']
            question_type = row["Type"]

            if not pd.isnull(row['Offered Answers (CSV)']):
                answers.append(row['Offered Answers (CSV)'].split('|'))

            question_query += "(null, '{}', '{}')".format(question_type, question_text)

            if index < len(data.index) - 1:
                question_query += ','

def main():
    converter = SurveyToDatabase()
    converter.convert("DemographicSurvey.csv")

if __name__ != '__main':
    main()
