# CDK Install
    
    brew install aws-cdk
    cdk --version
    python3 --version
    pipx install pipenv
    
# CDK commands

    * `cdk ls`          list all stacks in the app
    * `cdk synth`       emits the synthesized CloudFormation template
    * `cdk deploy`      deploy this stack to your default AWS account/region
    * `cdk diff`        compare deployed stack with current state
    * `cdk docs`        open CDK documentation

## Install CDK dependency and initialize project from empty directory
    
    mkdir cdk-project
    cd cdk-project

    cdk init app --language=python

## Import project to PyCharm

## Once the virtualenv is activated, you can install the required dependencies.

    follow the READme file inside project

## At this point you can now synthesize the CloudFormation template for this code.

    cdk synth

## Bootstrap Your Environment

    cdk bootstrap

## Deploy CDK
    
    cdk deploy

## Verify S3

    aws s3 ls

## Destroy CDK
    
    cdk destroy

