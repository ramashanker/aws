# Create CloudFormation for S3

## Execute cloudformation to create bucket

    aws cloudformation create-stack --stack-name s3-bucket-with-policy-stack --template-body file://s3-bucket-with-policy.yml --capabilities CAPABILITY_NAMED_IAM

## List S3 bucket

    aws s3 ls

## Delete Stack after excution

    aws cloudformation delete-stack --stack-name s3-bucket-with-policy-stack

## Describe stack status

    aws cloudformation describe-stacks --stack-name s3-bucket-with-policy-stack

##   