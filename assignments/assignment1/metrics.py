def binary_classification_metrics(prediction, ground_truth):
    '''
    Computes metrics for binary classification

    Arguments:
    prediction, np array of bool (num_samples) - model predictions
    ground_truth, np array of bool (num_samples) - true labels

    Returns:
    precision, recall, f1, accuracy - classification metrics
    '''
    precision = 0
    recall = 0
    accuracy = 0
    f1 = 0

    # TODO: implement metrics!
    # Some helpful links:
    # https://en.wikipedia.org/wiki/Precision_and_recall
    # https://en.wikipedia.org/wiki/F1_score
    rightClassified = 0
    truePositives = 0
    falsePositives = 0
    falseNegatives = 0
    for i in range(prediction.shape[0]):
        rightClassified = rightClassified + 1 if prediction[i] == ground_truth[i] else rightClassified
        truePositives = truePositives + 1 if (prediction[i] == ground_truth[i] and prediction[i] == True) else truePositives
        falsePositives = falsePositives + 1 if (prediction[i] == True and ground_truth[i] == False) else falsePositives
        falseNegatives = falseNegatives + 1 if (prediction[i] == False and ground_truth[i] == True) else falseNegatives

    accuracy = rightClassified * 100 / prediction.shape[0]
    recall = truePositives * 100 / (truePositives + falseNegatives)
    precision = truePositives * 100 / (truePositives + falsePositives)
    f1 = 2 * precision * recall / (precision + recall)

    return precision, recall, f1, accuracy


def multiclass_accuracy(prediction, ground_truth):
    '''
    Computes metrics for multiclass classification

    Arguments:
    prediction, np array of int (num_samples) - model predictions
    ground_truth, np array of int (num_samples) - true labels

    Returns:
    accuracy - ratio of accurate predictions to total samples
    '''
    # TODO: Implement computing accuracy
    accuracy = 0
    for idx, val in enumerate(prediction):
        if val == ground_truth[idx]:
            accuracy += 1
    return accuracy * 100 / prediction.shape[0]
