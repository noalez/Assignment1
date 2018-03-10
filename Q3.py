def compare_subjects_within_student(subj1_all_students,
                                    subj2_all_students):
    """
    Compare the two subjects with their students and print out the "preferred"
    subject for each student. Single-subject students shouldn't be printed.

    Choice for the data structure of the function's arguments is up to you.
    """
    best_subject = {}
    names = subj1_all_students.keys()
    for name in names:
        if name != 'Subject':
            if str(subj2_all_students.get(name)) != 'None':
                subj2_all_students[name] = max(subj2_all_students[name])
                subj1_all_students[name] = max(subj1_all_students[name])
                if subj1_all_students[name]>subj2_all_students[name]:
                    best_subject[name] = subj1_all_students['Subject']
                elif subj1_all_students[name]<subj2_all_students[name]:
                    best_subject[name] = subj2_all_students['Subject']
                else:
                    best_subject[name] = str(subj1_all_students[name])+' in both'
    print(best_subject)

dict1 = {'Subject': 'Math', 'Amy': [90,80], 'Ben': [70,80], 'John': [55,65], 'Jane': [80,70], 'Alex': [100,90]}
dict2 = {'Subject': 'History', 'Amy': [95,80], 'Ben': [70,60], 'John': [60,95], 'Alex': [55,90]}
compare_subjects_within_student(dict1,dict2)