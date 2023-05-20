## Day1 Topics Elastic Bean Stack

### Create cloud9 environment:
 Create manually cloud9 environment

### Clone the code
``` 
git clone https://ramashanker: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@github.com/ramashanker/awsapp.git
```

### Install c9 command
install node in it: npm i c9 -g

### Install java in to environment:

``` 
sudo yum install java-11-amazon-corretto
sudo alternatives --config java
```
### Install maven in to environment

``` 
sudo wget http://repos.fedorapeople.org/repos/dchen/apache-maven/epel-apache-maven.repo -O /etc/yum.repos.d/epel-apache-maven.repo
sudo sed -i s/\$releasever/6/g /etc/yum.repos.d/epel-apache-maven.repo
sudo yum install -y apache-maven
``` 

### Get detail for the metadata in aws

``` 
curl -s http://169.254.169.254/latest/meta-data
``` 
Result: List of options

### reach security group:
``` 
curl -s http://169.254.169.254/latest/meta-data/network/interfaces/macs/12:32:9f:d9:62:9d/security-group-ids
``` 
Result:sg-07f0e144d9eb7bbd9

### Check aws machine ip:
``` 
https://checkip.amazonaws.com/
``` 
Result:84.19.151.155

### change outbound rules:

``` 
aws ec2 authorize-security-group-ingress --group-id sg-07f0e144d9eb7bbd9 --port 8080 --protocol tcp --cidr 84.19.151.155/32
```
Result:
{
    "Return": true,
    "SecurityGroupRules": [
    {
        "SecurityGroupRuleId": "sgr-0965e0e52dc7a54d0",
        "FromPort": 8080,
        "GroupOwnerId": "201964534042",
        "ToPort": 8080,
        "IpProtocol": "tcp",
        "CidrIpv4": "84.19.151.155/32",
        "GroupId": "sg-07f0e144d9eb7bbd9",
        "IsEgress": false
    }
    ]
}

### Check the security group changes:

``` 
aws ec2 describe-security-groups --group-ids sg-07f0e144d9eb7bbd9 --output text --filter Name=ip-permission.to-port,Values=8080
```
Result:
SECURITYGROUPS  Security group for AWS Cloud9 environment aws-cloud9-DevEnv-dcf94a339f5b41abb77cd0f2a0c7e65f    sg-07f0e144d9eb7bbd9    aws-cloud9-DevEnv-dcf94a339f5b41abb77cd0f2a0c7e65f-InstanceSecurityGroup-6P452K9A4XY3   201964534042
vpc-00e087f1a7e8f9b23
IPPERMISSIONS   8080    tcp     8080
IPRANGES        84.19.151.155/32
IPPERMISSIONSEGRESS     -1
IPRANGES        0.0.0.0/0
TAGS    Name    aws-cloud9-DevEnv-dcf94a339f5b41abb77cd0f2a0c7e65f
TAGS    aws:cloudformation:stack-name   aws-cloud9-DevEnv-dcf94a339f5b41abb77cd0f2a0c7e65f
TAGS    aws:cloudformation:stack-id     arn:aws:cloudformation:us-east-1:201964534042:stack/aws-cloud9-DevEnv-dcf94a339f5b41abb77cd0f2a0c7e65f/2b7ee720-cd78-11ed-b8bf-0e2d83f2deef
TAGS    aws:cloud9:owner        201964534042
TAGS    aws:cloudformation:logical-id   InstanceSecurityGroup
TAGS    aws:cloud9:environment  dcf94a339f5b41abb77cd0f2a0c7e65f

### Get the public ip address for ec2

``` 
curl -s http://169.254.169.254/latest/meta-data/public-ipv4
```

Result:3.83.154.249

### Run the applicaton:

```
mvn spring-boot:run 
```

prompt with this url :https://dcf94a339f5b41abb77cd0f2a0c7e65f.vfs.cloud9.us-east-1.amazonaws.com/swagger-ui/index.html
or use public ip address


### EB cli setup

```
https://github.com/aws/aws-elastic-beanstalk-cli-setup
```

### Initialize the elastic bean 

``` 
eb init
```
Note: Always run from where .git is available

### First time we need to create one sample manual repository

### Create this role before eb create :

   aws-elasticbeanstalk-ec2-role
   With following access:
   AWSElasticBeanstalkWebTier
   AWSElasticBeanstalkMulticontainerDocker

### Create the elastic bean
``` 
eb create --single
```










