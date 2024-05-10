import os
from random import random, randint

import mlflow

if __name__ == "__main__":
    os.environ['AWS_ACCESS_KEY_ID'] = "admin"
    os.environ['AWS_SECRET_ACCESS_KEY'] = "sample_key"
    os.environ['MLFLOW_TRACKING_USERNAME'] = "mlflow"
    os.environ['MLFLOW_TRACKING_PASSWORD'] = "mlflow"
    os.environ['MLFLOW_S3_ENDPOINT_URL'] = "http://10.2.10.159:9000"

    mlflow.set_tracking_uri('http://10.2.10.159:5000')
    print("Running mlflow_tracking.py")
    # 실험이 없는 경우, 'my_experiment'라는 이름의 실험을 생성합니다.
    if mlflow.get_experiment_by_name('test_experiment') is None:
        mlflow.create_experiment('test_experiment')
    # 'my_experiment' 실험으로 변경합니다.
    mlflow.set_experiment('test_experiment')

    #with mlflow.start_run():
    mlflow.log_param("param2", randint(0, 100))
    mlflow.log_metric("foo2", random())
    mlflow.log_metric("foo2", random() + 1)
    mlflow.log_metric("foo2", random() + 2)

    if not os.path.exists("outputs"):
        os.makedirs("outputs")
    with open("outputs/test.txt", "w") as f:
        f.write("hello world!")

    #mlflow.set_registry_uri('s3://mlflow')
    mlflow.log_artifacts("outputs")
