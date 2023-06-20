from constructs import Construct
from aws_cdk import (
    Stack,
    aws_ec2 as ec2
)


class Ec2CdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.instance_ami = "ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-20230516"
        self.instance_type = "t2.micro"
        self.vpc_id = "vpc-06340f3cfaa877f8e"
        self.security_group_id = "sg-07276703468ccad6c"

        vpc = ec2.Vpc.from_lookup(
            self
            , "vpc"
            , vpc_id=self.vpc_id
        )

        security_group = ec2.SecurityGroup.from_lookup_by_id(
            self
            , "security_group"
            , security_group_id=self.security_group_id
        )
        instance = ec2.Instance(
            self
            , "Instance"
            , instance_type=ec2.InstanceType(self.instance_type)
            , machine_image=ec2.MachineImage().lookup(name=self.instance_ami)
            , vpc=vpc
            , security_group=security_group
        )
