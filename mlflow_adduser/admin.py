import os
from mlflow.server import get_app_client
from mlflow import MlflowClient

if __name__ == "__main__":
    os.environ['MLFLOW_TRACKING_USERNAME'] = "admin"
    os.environ['MLFLOW_TRACKING_PASSWORD'] = "password"

    tracking_uri = 'http://10.2.10.159:5000'

    auth_client = get_app_client("basic-auth", tracking_uri=tracking_uri)
    auth_client.update_user_password(username='admin', password='admin')

    auth_client.create_user(username='koast', password='koast3369')
    auth_client.create_user(username='mlflow', password='mlflow')
    client = MlflowClient(tracking_uri=tracking_uri)
    experiment_id = client.create_experiment(name="test_experiment")
    
    auth_client.create_experiment_permission(
            experiment_id=experiment_id, username='koast', permission='MANAGE') # can manage(admin)
    auth_client.create_experiment_permission(
            experiment_id=experiment_id, username='mlflow', permission='EDIT')  # can read, update
