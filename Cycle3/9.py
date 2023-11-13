import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

print("**********************************")
print("SJC22MCA-2034")
print("J SIDDHARTH")
print("BATCH: 2022-2024")
print("**********************************")

# Load Iris dataset from CSV
iris_df = pd.read_csv('iris.csv')

# Valid combinations of train_size and test_size
valid_combinations = [
    (0.6, 0.4),
    (0.7, 0.3),
    (0.8, 0.2)
]

k_values = [3, 5, 7]

# Assuming the target column is "variety"
X = iris_df.iloc[:, :-1]
y = iris_df['variety']

for train_size, test_size in valid_combinations:
    X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                        train_size=train_size,
                                                        test_size=test_size,
                                                        random_state=42)
    print(f"\nTrain size: {train_size}, Test size: {test_size}")

    for k in k_values:
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(X_train, y_train)
        accuracy = metrics.accuracy_score(y_test, knn.predict(X_test))
        print(f"  k={k}, Accuracy: {accuracy:.2f}")

