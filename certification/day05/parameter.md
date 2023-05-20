## Put in parameter store
``` 
aws ssm put-parameter --name "/planets/vulcan/population" --value 4.9B --type String
aws ssm put-parameter --name "/planets/vulcan/gravity" --value 4.3B --type String
aws ssm put-parameter --name "/planets/vulcan/earth" --value 3.9G --type String
```
## Get Hirarical from parameter store

``` 
aws ssm get-parameters-by-path --path /planets/vulcan
```
