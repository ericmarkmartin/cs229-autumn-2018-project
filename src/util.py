import vectorize
from sklearn.metrics import classification_report, confusion_matrix

TARGET_NAMES = ['PERIOD', 'QMARK', 'EXPOINT']
RANDOM_STATE = 229
DATA_PATH = '../data/processed/merged_tok.txt'


def get_vectors(fn, one_hot_y=False):
    X, y = fn(DATA_PATH, one_hot_y=False)
    train, dev, test = vectorize.train_dev_test_split(X, y, 0.05, 0.05)
    x_train, y_train = train
    x_dev, y_dev = dev
    x_test, y_test = test
    return (
        (x_train, y_train.ravel()),
        (x_dev, y_dev.ravel()),
        (x_test, y_test.ravel())
    )


def run_model(model, train, test):
    print('Training')
    model.fit(*train)
    print('Making Predictions')
    x_test, y_test = test
    y_pred = model.predict(x_test)
    report = classification_report(y_test, y_pred, target_names=TARGET_NAMES)
    print(report)
    confusion = confusion_matrix(y_test, y_pred)
    print(confusion)

