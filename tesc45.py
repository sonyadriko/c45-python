from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import graphviz
import pandas as pd

# Load data
df = pd.read_excel('data20.xlsx')

# Encode categorical data
df_encoded = pd.get_dummies(df[['service']], prefix=['service'])
df = pd.concat([df, df_encoded], axis=1)

# Separate features and labels
X = df.drop(['no.', 'attack_cat', 'service'], axis=1)
y = df['attack_cat']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature scaling (if required)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Decision Tree model
model = DecisionTreeClassifier(criterion='entropy', random_state=42, min_samples_split=144)
model.fit(X_train_scaled, y_train)

# Visualize decision tree
best_attribute = 'sbytes'  # You can replace this with the attribute you want to visualize
dot_data = export_graphviz(model, out_file=None,
                           feature_names=X.columns,
                           class_names=y.unique(),
                           filled=True, rounded=True, special_characters=True)

graph = graphviz.Source(dot_data)
graph.render("decision_tree")

# View decision tree
graph.view("decision_tree")
