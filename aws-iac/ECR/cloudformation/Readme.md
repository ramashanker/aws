# Create CloudFormation for ECR

## Execute cloudformation to create ecr repository

       aws cloudformation deploy --template-file ecr-template.yml --stack-name create-ecr-repo --capabilities CAPABILITY_NAMED_IAM --profile rama

## Verify ECR

###  List all ECR repositories:

    aws ecr describe-repositories --profile rama

### Check details of a specific repository:

    aws ecr describe-repositories --repository-names microservice-repo --profile rama

### List images in the repository:

    aws ecr list-images --repository-name microservice-repo --profile rama

### Login to ECR (for Docker):
    aws ecr get-login-password --region us-east-1 --profile rama| docker login --username AWS --password-stdin 201964534042.dkr.ecr.us-east-1.amazonaws.com

## Push Image to ECR

### Build docker image

### Tag Image with ECR Repository URL:

    docker tag falcon007/calculator-app:0.0.1-SNAPSHOT 201964534042.dkr.ecr.us-east-1.amazonaws.com/microservice-repo:latest

### Login to ECR (for Docker):
    aws ecr get-login-password --region us-east-1 --profile rama| docker login --username AWS --password-stdin 201964534042.dkr.ecr.us-east-1.amazonaws.com

### Push images:
    docker push 201964534042.dkr.ecr.us-east-1.amazonaws.com/microservice-repo:latest

### List images in the repository:
    aws ecr list-images --repository-name microservice-repo --profile rama