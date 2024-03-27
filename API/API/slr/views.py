import csv
import os
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import CSVFile
from .serializers import CSVFileSerializer
from django.http import HttpResponseRedirect
from sklearn.linear_model import LinearRegression
from django.http import HttpResponseForbidden
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
@api_view(['POST'])
def upload_csv(request, username):
    if request.method == 'POST' and request.FILES.get('csv_file'):
        csv_file = request.FILES['csv_file']
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({'error': 'User does not exist.'}, status=400)
        
        new_csv_file = CSVFile.objects.create(user=user, file=csv_file)
        new_csv_file.save()
        return HttpResponseRedirect(f"http://localhost:8000/slr/show/{username}")
    else:
        return Response({'error': 'CSV file not provided.'}, status=400)

def show_all_csv_files(request, username):
    if request.user.username==username:
        user = User.objects.get(username=username)
        csv_files = CSVFile.objects.filter(user=user)
        return render(request, 'csv_files.html', {'csv_files': csv_files})
    else:
        return HttpResponseForbidden("You don't have permission to access this page.")
def read_csv_file(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        column_names = next(reader)
        data_rows = list(reader)  
    return column_names, data_rows

def show_csv_data(request, username, csv_file_name):
    if request.user.username==username:
        file_path = "csv_files/"+username+"/"+csv_file_name
        column_names, data_rows = read_csv_file(file_path)
        return render(request, 'csv_data.html', {'column_names': column_names, 'data_rows': data_rows})
    else:
        return HttpResponseForbidden("You don't have permission to access this page.")

def simple_linear_regression_algorithm(request, username, csv_file_name):
    path = "csv_files/"+username+"/"+csv_file_name
    dataset = pd.read_csv(path)
    X = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, -1].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)    
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)
    y_pred = regressor.predict(X_test)
    plt.scatter(X_train, y_train, color = 'red')
    plt.plot(X_train, regressor.predict(X_train), color = 'blue')
    plt.title('Salary vs Experience (Training set)')
    plt.xlabel('Years of Experience')
    plt.ylabel('Salary')
    plot_path = os.path.join("static", f"{username}_{csv_file_name}_plot.png")
    plt.savefig(plot_path)
    plot_pathDTL = os.path.join(f"{username}_{csv_file_name}_plot.png")
    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    return render(request, 'analysis_result.html', {"r2":r2,"mean_absolute": mae, "mean_squared":mse, "root_mean": rmse, "plot_path":plot_pathDTL})