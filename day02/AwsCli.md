# Important commands
## Configure command

``` 
Install aws cli using python
create user and get the credential cecret and access key and update in file
[default]
aws_access_key_id = *************
aws_secret_access_key = *****/*************************
If you heave multiple profile crete like this.
[prod]
aws_access_key_id = *************
aws_secret_access_key = *****/*************************
[nonprod]
aws_access_key_id = *************
aws_secret_access_key = *****/*************************
```

## List buckets with profile
### Profiles use for switching between aws accounts like prod dev test
``` 
aws s3api list-buckets --output text --profile prod
aws s3 ls --profile nonprod
aws s3 ls --profile prod
```
### Copy or download from s3 bucket

``` 
aws s3 cp source_file destination_file --profile prod
aws s3 cp s3://rama-000/mydata/image01.jpg image01.jpg --profile prod
```
