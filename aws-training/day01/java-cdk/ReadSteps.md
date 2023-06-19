# https://docs.aws.amazon.com/cdk/v2/guide/hello_world.html
# https://docs.aws.amazon.com/cdk/v2/guide/bootstrapping.html
## Create CDK using python

    mkdir java-cdk
    cd java-cdk

## Initialize CDK for python
    create fresh directory
    mkdir s3-cdk
    cd s3-cdk
    cdk init app --language java    

## Build the app
    mvn compile -q

## List stack in app
    cdk ls

## Add an Amazon S3 bucket
        package com.myorg;

    import software.amazon.awscdk.*;
    import software.amazon.awscdk.services.s3.Bucket;

        public class HelloCdkStack extends Stack {
            public HelloCdkStack(final App scope, final String id) {
            this(scope, id, null);
        }

        public HelloCdkStack(final App scope, final String id, final StackProps props) {
            super(scope, id, props);

                Bucket.Builder.create(this, "MyFirstBucket")
                    .versioned(true).build();
        }
    }

## Synthesize an AWS CloudFormation template
    cdk synth

    cdk.out
    Resources:
        MyFirstBucketB8884501:
            Type: AWS::S3::Bucket
            Properties:
                VersioningConfiguration:
                    Status: Enabled
                UpdateReplacePolicy: Retain
                DeletionPolicy: Retain
                Metadata:...

## Bootstrap environment

    cdk bootstrap

## Deploying the stack

    cdk deploy

## Modifying the app

    bucket = s3.Bucket(self, "MyFirstBucket",
    versioned=True,
    removal_policy=cdk.RemovalPolicy.DESTROY,
    auto_delete_objects=True)

## Check differences

    cdk diff

## Deploy

    cdk deploy

## Destroying the app's resources

    cdk destroy