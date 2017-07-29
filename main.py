from csv import reader
# Load CSV File
def load_csv(filename):
	dataset = list()
	with open(filename, 'r') as file:
		csv_reader = reader(file)
		for row in csv_reader:
			if not row:
				continue
			dataset.append(row)
	return dataset
# Convert Possible Strings to Floats
def str_column_to_float(dataset, column):
	for row in dataset:
		try:
			row[column] = float(row[column].strip())
		except ValueError:
			continue

# PassengerId, Survived, Pclass, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked

filename = 'train.csv'
dataset = load_csv(filename)
for i in range(len(dataset[0])):
	str_column_to_float(dataset, i)
dataset.pop(0)
for x in range(len(dataset)):
    print dataset[x]
