def check_answers(check_answer,answer):
    results = []
    count_correct = 0
    count_incorrect = 0
    for i in range(len(answer)):
        if check_answer[i] == answer[i]:
            results.append(True)
            count_correct += 1
        else:
            results.append(False)
            count_incorrect += 1

    if count_correct/len(answer) > 0.7:
        return "Congratulations, you passed the test! You scored " + str(len(answer)) + " out of " + str(len(answer))+"."
    else:
        return "Unfortunately, you did not pass. You scored " + str(len(answer)) + " out of " + str(len(answer)) + "."

print(check_answers([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]))