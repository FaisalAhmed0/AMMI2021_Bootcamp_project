# Model is a rule-based classifier
class RuleBasedModel():
    def __init__(self):
        self.train_data = None
        self.test_data = None
        self.accuracy = 0

    # Get the training data
    def get_data(self, data):
        self.train_data = data
        self.train_targets = []
        for row in self.train_data:
            self.train_targets.append(row['class'])

    # Get the test data
    def get_test(self, test_data):
        self.test_data = test_data
        self.test_targets = []
        for row in self.test_data:
            self.test_targets.append(row['class'])
        ###
    # Train the model
    

    def predict(self, data, test=True):
        clss = []
        predic_list = []
        if test:
            data = self.test_data
        else:
            data = self.train_data
        for row in data:
            clss.append(row['class'])
            if float(row['f1']) * float(row['f7'])>0.1:
                predic_list.append(1)

            elif (float(row['f11']) * float(row['f8'])<0.0225 and float(row['f6'])<0.75):
                predic_list.append(2)

            elif (float(row['f2']) * float(row['f5'])<0.28 and float(row['f8'])<0.25):
                predic_list.append(2)
            else:
                predic_list.append(1)
        return predic_list

    def predict_with_ID(self, id, test):
        record = None
        if test:
            for row in self.test_data:
                if int(row['ID']) == id:
                    record = row
                    break
        else:
            for row in self.test_data:
                if int(row['ID']) == id:
                    record = row
                    break

        if(float(row['f1'])<0.5):
            return 2
        else:
            return 1


    def calculate_accuracy(self, data, test):
        predictions = self.predict(data, test)
        correct_prediction = 0
        targets = None
        if test:
            targets = self.test_targets
        else:
            targets = self.train_targets
        for ind in range(len(predictions)):
            correct_prediction += (predictions[ind] == int(targets[ind]))
        total_prediction = len(predictions)
        accuracy = (correct_prediction / total_prediction) * 100
        return accuracy, correct_prediction, total_prediction

