"""
@file
@brief Compute metrics in for a competition
"""
import os
import sys


if sys.version_info[0] == 2:
    FileNotFoundError = Exception


def main_codalab_wrapper(fct, metric_name, argv, truth_file="truth.txt", submission_file="answer.txt", output_file="scores.txt"):
    """
    adapt the tempate available at
    `evaluate.py <https://github.com/Tivix/competition-examples/blob/master/hello_world/competition/scoring_program/evaluate.py>`_
    """
    input_dir = argv[1]
    output_dir = argv[2]

    submit_dir = os.path.join(input_dir, 'res')
    truth_dir = os.path.join(input_dir, 'ref')

    if not os.path.isdir(submit_dir):
        raise FileNotFoundError(f"{submit_dir} doesn't exist")

    if os.path.isdir(submit_dir) and os.path.isdir(truth_dir):
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        private_codalab_wrapper(fct, metric_name,
                                fold1=truth_dir, f1=truth_file,
                                fold2=submit_dir, f2=submission_file,
                                output=os.path.join(output_dir, output_file))
    else:
        raise FileNotFoundError(
            f"{submit_dir} or {truth_dir} is not a folder")


def private_codalab_wrapper(fct, metric_name, fold1, fold2, f1="answer.txt", f2="answer.txt", output="scores.txt"):
    """
    Wraps the function following the guidelines
    `User_Building a Scoring Program for a Competition <https://github.com/codalab/codalab-competitions/wiki/User_Building-a-Scoring-Program-for-a-Competition>`_.
    It replicates the example available at
    `competition-examples/hello_world <https://github.com/Tivix/competition-examples/tree/master/hello_world/competition>`_.

    @param      fct             function to wrap
    @param      metric_name     metric name
    @param      fold1           folder which contains the data for folder containing the truth
    @param      fold2           folder which contains the data for folder containing the data
    @param      f1              filename for the truth
    @param      f2              filename for the produced answers
    @param      output          produces an output with the expected results
    @return                     metric
    """
    f1 = os.path.join(fold1, f1)
    f2 = os.path.join(fold2, f2)
    if not os.path.exists(f1):
        raise FileNotFoundError(f"unable to find '{f1}'")
    if not os.path.exists(f2):
        raise FileNotFoundError(f"unable to find '{f2}'")
    if f1 == f2:
        raise ValueError(
            f"answers and scores are the same file: '{f1}'")

    with open(f1, "r") as f:
        lines = f.readlines()
    answers = [float(_) for _ in lines if _]
    print("Reading answers:", f1, len(answers), "rows")
    print("First answers:", answers[:10])

    with open(f2, "r") as f:
        lines = f.readlines()
    scores = [float(_) for _ in lines if _]
    print("Reading scores:", f1, len(scores), "rows")
    print("First scores:", scores[:10])

    metric = fct(answers, scores)
    res = f"{metric_name}:{metric}"
    print("Results=", res)
    with open(output, "w") as f:
        f.write(res)
    print("Wrote", res, "in", output)
    return metric


def AUC(answers, scores):
    """
    Compute the `AUC <https://en.wikipedia.org/wiki/Area_under_the_curve_(pharmacokinetics)>`_.

    @param     answers      expected answers 0 (false), 1 (true)
    @param     scores       score obtained for class 1
    @return                 number
    """
    ab = list(zip(answers, scores))
    plus = [s for a, s in ab if a == 1]
    moins = [s for a, s in ab if a != 1]
    auc = 0
    for p in plus:
        for m in moins:
            if p > m:
                auc += 2
            elif p == m:
                auc += 1
    den = len(plus) * len(moins)
    if den == 0:
        return 1.0 if len(moins) == 0 else 0.0
    return auc * 1.0 / (len(plus) * len(moins) * 2)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        raise RuntimeError(f"bad arguments: {sys.argv}")
    main_codalab_wrapper(AUC, "AUC", sys.argv)
