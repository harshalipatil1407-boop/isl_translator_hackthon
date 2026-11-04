import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

print("Dataset load ho raha hai...")
# 1. Dataset read karein
df = pd.read_csv("dataset.csv", header=None)

# 2. Features (X) aur Labels (y) ko alag karein
# Aakhri column label (gesture name) hai, baaki 126 features hain
X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

# 3. Train aur Test data mein split karein
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Model training shuru ho rahi hai (Random Forest)...")
# 4. Random Forest Classifier train karein
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 5. Accuracy check karein
accuracy = model.score(X_test, y_test)
print(f"Model Training Complete! Accuracy: {accuracy * 100:.2f}%")

# 6. Model ko save karein
joblib.dump(model, "model.pkl")
print("Model successfully 'model.pkl' ke naam se save ho gaya hai!")