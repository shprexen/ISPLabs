class Lesson:
    def __init__(self, lessonTime="-", subject="-", lessonType="-", employee="-", audience="-"):
        self.lessonTime = lessonTime
        self.subject = subject
        self.lessonType = lessonType
        self.employee = employee
        self.audience = audience


class Exam:
    def __init__(self, lessonTime="-", subject="-", lessonType="-", employee="-", audience="-", datetime="-"):
        self.lessonTime = lessonTime
        self.subject = subject
        self.lessonType = lessonType
        self.employee = employee
        self.audience = audience
        self.datetime = datetime


def get_schedule(schedule):
    if schedule:
        lessons = []
        if not 'schedule' in schedule[0].keys():
            for i in range(len(schedule)):
                if len(schedule[i]['employee']) != 0:
                    lesson = Lesson(schedule[i]['lessonTime'],
                                    schedule[i]['subject'],
                                    schedule[i]['lessonType'],
                                    schedule[i]['employee'][0]['fio'],
                                    schedule[i]['auditory'][0])
                else:
                    lesson = Lesson(schedule[i]['lessonTime'],
                                    schedule[i]['subject'],
                                    schedule[i]['lessonType'], )
                lessons.append(lesson)
        else:
            for i in range(len(schedule)):
                exam = Exam(schedule[i]['schedule'][0]['lessonTime'],
                              schedule[i]['schedule'][0]['subject'],
                              schedule[i]['schedule'][0]['lessonType'],
                              schedule[i]['schedule'][0]['employee'][0]['fio'],
                              schedule[i]['schedule'][0]['auditory'],
                              schedule[i]['weekDay'])
                lessons.append(exam)

        return lessons