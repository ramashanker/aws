import aws_cdk as core
import aws_cdk.assertions as assertions

from sqs_cdk.sqs_cdk_stack import SqsCdkStack

# example tests. To run these tests, uncomment this file along with the example
# resource in sqs_cdk/sqs_cdk_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = SqsCdkStack(app, "sqs-cdk")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
