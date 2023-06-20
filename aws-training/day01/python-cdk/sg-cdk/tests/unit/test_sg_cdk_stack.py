import aws_cdk as core
import aws_cdk.assertions as assertions

from sg_cdk.sg_cdk_stack import SgCdkStack

# example tests. To run these tests, uncomment this file along with the example
# resource in sg_cdk/sg_cdk_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = SgCdkStack(app, "sg-cdk")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
