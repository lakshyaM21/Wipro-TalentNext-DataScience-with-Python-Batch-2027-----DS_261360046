a_bunch_of_scores = [2, 3, 6, 6, 5]

the_absolute_highest = max(a_bunch_of_scores)

scores_without_highest = [
    single_score 
    for single_score in a_bunch_of_scores 
    if single_score != the_absolute_highest
]

the_runner_up_person_score = max(scores_without_highest)

print(the_runner_up_person_score)
