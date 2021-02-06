from utils import read_data
from utils import read_test
from model import RuleBasedModel
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--ID', type=int)
args = parser.parse_args()
print(args.ID)


def main(ID):

    train_file = 'train_data.txt'
    test_file = 'test_data.txt'
    variables = ['ID', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'class']


    print ("========= Reading train dataset =========")
    	# TO DO:
    # print("Here")
    train_dict = read_data(train_file)
    # print(train_dict[1:3])
	# use the read data function you created to read the train data
    print ("======== Done reading =========.\n")

    print ("========= Reading test data =========")
    	# TO-DO 
    test_dict = read_test(test_file)
	# Read the test  data
    print ("========= Done reading =========.\n")

    print ("==== Training classifier =====")
	# TO-DO
    model = RuleBasedModel()
    model.get_data(train_dict)
    model.get_test(test_dict)

	# Initialize the classifier you built in model.py and return the necessary values
    print ("======== Done training classifier ===========.\n")

    print ("========= Classifying test samples =======")
	# TO-DO 
    list_predict = model.predict(test_dict, test=True)
	# use your classifier to do predictions on all the test samples
    print ("========== Done classifying =======")
    accuracy, numCorrect, total_samples = model.calculate_accuracy(test_dict, test=True)
    	# TO-DO
	# Evalutate your classifier with the Accuracy function you implemented and return the necessary outputs
    print(f"Model's Accuracy {round(accuracy)} %, model correctly predicted {numCorrect} out of {total_samples}")
    if ID != None:
        print(ID)
        prediction_for_id = model.predict_with_ID(ID, test=True)
        print(f"The prediction of row with id:{ID} in the test set is class:{prediction_for_id}")
    print('================================================================')


    print ("finished.\n")

main(args.ID)
