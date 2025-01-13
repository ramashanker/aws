# Create CloudFormation for SQS

## Execute cloudformation to create sqs queue

       aws cloudformation deploy --template-file create-queue-template.yml --stack-name create-queue --capabilities CAPABILITY_NAMED_IAM --profile rama

## Queue command to verify

### List Queue

    aws sqs list-queues --profile rama

### Describe SQS queue

    aws sqs get-queue-attributes \
    --queue-url https://sqs.us-east-1.amazonaws.com/201964534042/simple-data-queue \
    --attribute-names All \
    --profile rama

### Send message to queue

    aws sqs send-message \
        --queue-url https://sqs.us-east-1.amazonaws.com/201964534042/simple-data-queue \
        --message-body "Hello, this is a test message!" \
        --profile rama

### Send Message to queue as json

    aws sqs send-message \
        --queue-url https://sqs.us-east-1.amazonaws.com/201964534042/simple-data-queue \
        --message-body '{"to": "test1", "from": "test", "messge": "Hello from test"}' \
        --profile rama

### Send Message to queue with attribute

    aws sqs send-message \
        --queue-url https://sqs.us-east-1.amazonaws.com/201964534042/simple-data-queue \
        --message-body "Hello from test" \
        --message-attributes '{
           "Username": {"StringValue": "test@123", "DataType": "String"},
           "RegistrationTimestamp": {"StringValue": "2025-01-11T10:30:00Z", "DataType": "String"},
           "IsPremiumUser": {"StringValue": "true", "DataType": "String"}}' \
        --profile rama

### Retrieve Message from queue

    aws sqs receive-message \
        --queue-url https://sqs.us-east-1.amazonaws.com/201964534042/simple-data-queue \
        --attribute-names All \
        --message-attribute-names All \
        --max-number-of-messages 1 \
        --profile rama

### Purge message from queue

    aws sqs purge-queue \
        --queue-url https://sqs.us-east-1.amazonaws.com/201964534042/simple-data-queue \
        --profile rama


## Delete stack

    aws cloudformation delete-stack --stack-name create-queue --profile rama

## Verify Cloudformation template

    aws cloudformation validate-template --template-body file://create-queue-with-dlq.yml --profile rama


## Cloudformation queue with dlq

    aws cloudformation deploy \
        --template-file create-queue-with-dlq.yml \
        --stack-name create-queue-with-dlq \
        --capabilities CAPABILITY_NAMED_IAM \
        --profile rama

## Delete stack

    aws cloudformation delete-stack \
        --stack-name create-queue-with-dlq \
        --profile rama