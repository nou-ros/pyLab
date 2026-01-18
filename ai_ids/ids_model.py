import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

data = pd.read_csv("data/KDDTrain+.txt", header=None)

# features selection
data = data[[0, 1, 4, 5, 6, 22, 23, 41]]
data.columns = ["duration", "protocol", "src_bytes", 
                "dst_bytes", "flag", "count", "srv_count", "label"]

# convert attack type
data["label"] = data["label"].apply(lambda x: "normal" if x == "normal" else "attack")

# Encode categorical values
le = LabelEncoder()
data["protocol"] = le.fit_transform(data["protocol"])
data["label"] = le.fit_transform(data["label"])

# Split data
X = data.drop("label", axis=1)
y = data["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3
)

# Train model
# model = LogisticRegression(max_iter=1000, random_state=42, class_weight="balanced")
model = RandomForestClassifier(n_estimators=200, class_weight="balanced", random_state=42)
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Results
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred, target_names=["attack", "normal"]))