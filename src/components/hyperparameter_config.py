
#             : DecisionTreeClassifier(),
#             "Random Forest Classifier": RandomForestClassifier(),
#             "Linear Classifier": LinearRegression(),
#             "XGBoost Classifier": XGBClassifier(),
#             "CatBoost Classifier": CatBoostClassifier(verbose = False),
#             "AdaBoost Classifier": AdaBoostClassifier(),
#             "KNeighbors Classifier": KNeighborsClassifier(),
#             "SVM Classifier": SVC()
# params={
#                "Decision Tree Classifier": {
#                   'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
#                },
               
#                "Random Forest Classifier":{
#                   'n_estimators': [8,16,32,64,128,256]
#                },

#                "Linear Classifier":{},
               
#                "XGBoost Classifier":{
#                   'learning_rate':[.1,.01,.05,.001],
#                   'n_estimators': [8,16,32,64,128,256]
#                },

#                "CatBoost Regressor":{
#                   'depth': [6,8,10],
#                   'learning_rate': [0.01, 0.05, 0.1],
#                   'iterations': [30, 50, 100]
#                },

#                "AdaBoost Regressor":{
#                   'learning_rate':[.1,.01,0.5,.001],
#                   'n_estimators': [8,16,32,64,128,256]
#                },

#                "KNeighbors Regressor" : {}
               
#          }