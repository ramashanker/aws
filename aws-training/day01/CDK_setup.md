# Prerequisit
    Run with node version v18.16.0
    Update node :
    sudo apt-get remove nodejs
    curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
    sudo apt-get install nodejs

## CDK SET UP For python

#### Linux
| Steps   | command                       | output  |
|---------|-------------------------------|---------|
| Install | sudo pip3 install aws-cdk-lib | success |
| import  | import aws_cdk as cdk         | success |


#### Windows
| Steps   | command                  | output  |
|---------|--------------------------|---------|
| Install | pip3 install aws-cdk-lib | success |
| import  | import aws_cdk as cdk    | success |



## CDK SET UP For typescript

#### Linux

| Steps   | command                             | output  |
|---------|-------------------------------------|---------|
| Install | sudo npm install -g aws-cdk-lib     | success |
| import  | import * as cdk from 'aws-cdk-lib'; | success |

#### Windows

| Steps   | command                             | output  |
|---------|-------------------------------------|---------|
| Install |  npm install -g aws-cdk-lib     | success |
| import  | import * as cdk from 'aws-cdk-lib'; | success |

## CDK SET UP For java
| Steps   | command                  | output  |
|---------|--------------------------|---------|
| Add to pom.xml | Group software.amazon.awscdk; artifact aws-cdk-lib | success |
| Import | import software.amazon.awscdk.App; (for example) | success |