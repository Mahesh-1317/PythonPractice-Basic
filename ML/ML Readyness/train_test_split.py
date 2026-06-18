from sklearn.model_selection import train_test_split, cross_val_score
import numpy as np

#   Simulation dataset: 500 student records
np.random.seed(42)
X = np.random.randn(500, 5)     # 5 features
Y = np.random.randint(0,2,500)  # Labels: pass(1)/fail(0)

#   80/20 Train-Test Split
X_train ,X_test,Y_train,Y_test = train_test_split(X, Y, test_size=0.2,random_state=42,stratify=Y)
print(f'Training samples: {len(X_train)} | Test samples: {len(X_test)}')

# 5-Fold Cross-Validation - more reliable than single split
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=50, random_state=42)
cv_scores = cross_val_score(model, X, Y, cv=5, scoring='accuracy')
print(f'CV Scores each fold: {cv_scores.round(3)}')
print(f'Mean: {cv_scores.mean():.4f} +- {cv_scores.std():.4f}')