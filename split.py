#import pandas as pd
#import numpy as np

dataset = pd.read_csv('/home/arpitjp/Horrible/Original_Corpus.csv', header=None)
train, validate, test = np.split(dataset.sample(frac=1), [int(.7*len(dataset)), int(.85*len(dataset))])

train_en = train.iloc[:, :-1]
train_hi = train.iloc[:, 1:2]

validate_en = validate.iloc[:, :-1]
validate_hi = validate.iloc[:, 1:2]

test_en = test.iloc[:, :-1]
test_hi = test.iloc[:, 1:2]

train_en.to_csv("/home/arpitjp/Horrible/Split/train_en.tsv", sep="\t", index=False)
train_hi.to_csv("/home/arpitjp/Horrible/Split/train_hi.tsv", sep="\t", index=False)

validate_en.to_csv("/home/arpitjp/Horrible/Split/validate_en.tsv", sep="\t", index=False)
validate_hi.to_csv("/home/arpitjp/Horrible/Split/validate_hi.tsv", sep="\t", index=False)

test_en.to_csv("/home/arpitjp/Horrible/Split/test_en.tsv", sep="\t", index=False)
test_hi.to_csv("/home/arpitjp/Horrible/Split/test_hi.tsv", sep="\t", index=False)