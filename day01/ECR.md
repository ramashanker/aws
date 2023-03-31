# Create ECR Repository
# Retrieve an authentication token and authenticate your Docker client to your registry.

## Use the AWS CLI for ECR:

### Login to ECR using aws cli

``` 
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 201964534042.dkr.ecr.us-east-1.amazonaws.com
```

### Create ECR repository

``` 
aws ecr create-repository --repository-name falcon007/calculator-app
```
Result:
`{
"repository": {
"repositoryArn": "arn:aws:ecr:us-east-1:201964534042:repository/falcon007/calculator-app",
"registryId": "201964534042",
"repositoryName": "falcon007",
"repositoryUri": "201964534042.dkr.ecr.us-east-1.amazonaws.com/falcon007/calculator-app",
"createdAt": "2023-03-31T11:45:59+02:00",
"imageTagMutability": "MUTABLE",
"imageScanningConfiguration": {
"scanOnPush": false
},
"encryptionConfiguration": {
"encryptionType": "AES256"
}
}
}`

### Describe docker images

``` 
aws ecr describe-image-tags --repository-name falcon007/calculator-app
```

#### Delete Docker images

``` 
aws ecr batch-delete-image --repository-name falcon007/calculator-app --image-ids imageTag=latest --region us-east-1
```
### Delete ECR repository

``` 
aws ecr delete-repository --repository-name falcon007/calculator-app
```

### Build your docker image

``` 
docker build -t falcon007/calculator-app .
```
### Change tag of your docker image

``` 
docker tag falcon007/calculator-app:0.0.1-SNAPSHOT falcon007/calculator-app:latest
```

### Remove or untagged old image

```
docker rmi falcon007/calculator-app:0.0.1-SNAPSHOT 
```

## After the build completes, tag your image so you can push the image to this repository:

``` 
docker tag falcon007/calculator-app:latest 201964534042.dkr.ecr.us-east-1.amazonaws.com/falcon007/calculator-app:latest
```

## Run the following command to push this image to your newly created AWS repository:

``` 
docker push 201964534042.dkr.ecr.us-east-1.amazonaws.com/falcon007/calculator-app:latest
```

