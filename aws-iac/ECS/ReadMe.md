# Create CloudFormation for ECS Farget

## Execute cloudformation to create ECS

    aws cloudformation deploy \
        --template-file ecs-ecr-farget-template.yml \
        --stack-name create-ecs-farget \
        --capabilities CAPABILITY_NAMED_IAM \
        --profile rama

## ECS command 

### Get Public IP address of ECS Task

    aws ecs describe-tasks \
        --cluster create-ecs-farget-ECSCluster-RN8taCEAizoY \
        --tasks bc31c75f879745cea60b201e15dbfe7d --profile rama

### Invoke calculator api.

    curl -X GET 'http://54.221.51.136:8080/substraction?a=9&b=5'
    curl http://54.221.51.136:8080/actuator/health/
    
## Delete Stack

    aws cloudformation delete-stack \
        --stack-name create-ecs-farget \
        --profile rama