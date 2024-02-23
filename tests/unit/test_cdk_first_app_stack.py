import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_first_app.cdk_first_app_stack import CdkFirstAppStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_first_app/cdk_first_app_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkFirstAppStack(app, "cdk-first-app")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
