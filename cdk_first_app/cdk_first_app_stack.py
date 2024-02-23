from aws_cdk import (
    Stack,
    aws_s3 as s3,
    aws_lambda as _lambda,
    aws_iam as iam
)
from constructs import Construct

class CdkFirstAppStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        bucket = s3.Bucket(self, "TestBucket")
        
        lambda_role = iam.Role(self, "Testrole",
                        assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"))
        
        bucket.grant_read_write(lambda_role)
        
        function = _lambda.Function(
            self, "lambdatest",
            runtime=_lambda.Runtime.PYTHON_3_12,
            handler="lambdatest-handler.main",
            code=_lambda.Code.from_bucket(bucket=bucket, key=".\lambda\lambdatest-handler.py"),
            role = lambda_role
        )