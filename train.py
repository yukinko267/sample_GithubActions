from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

# データ
X, y = load_digits(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# モデル
model = MLPClassifier(hidden_layer_sizes=(64,), max_iter=10)

# 学習
model.fit(X_train, y_train)

# 評価
pred = model.predict(X_test)
acc = accuracy_score(y_test, pred)

print("Accuracy:", acc)