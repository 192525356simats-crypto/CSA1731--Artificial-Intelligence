% Facts: studies(Student, SubjectCode)
studies(kiran, cs101).
studies(kiran, cs102).
studies(anita, cs101).
studies(vijay, cs103).

% Facts: teaches(Teacher, SubjectCode)
teaches(prof_sharma, cs101).
teaches(prof_nair, cs102).
teaches(prof_kumar, cs103).

% Rule: Find which teacher teaches a specific student
student_teacher(Student, Teacher) :-
    studies(Student, SubCode),
    teaches(Teacher, SubCode).
