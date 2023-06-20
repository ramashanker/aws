from aws_cdk import (
    # Duration,
    Stack,
    aws_ec2 as ec2
)
from constructs import Construct


class SgCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.vpc_id = "vpc-06340f3cfaa877f8e"
        # The code that defines your stack goes here
        vpc = ec2.Vpc.from_lookup(
            self
            , "vpc"
            , vpc_id=self.vpc_id
        )
        sg = ec2.SecurityGroup(
            self,
            id="sg_1",
            vpc=vpc,
            allow_all_outbound=True,
            description="CDK Security Group"
            # security_group_name = "sg_elb"
            # not recommended https://docs.aws.amazon.com/cdk/api/latest/docs/@aws-cdk_aws-ec2.SecurityGroup.html
        )

        sg.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.tcp(22),
            description="ssh",
        )
