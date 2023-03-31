# Create ECS cluster

## Create Cluster
```
aws ecs create-cluster --cluster-name MyCluster 
```

## List Container instances

```
aws ecs list-container-instances --cluster MyCluster 
```

## Describe your container instances

```
aws ecs describe-container-instances --cluster default --container-instances container_instance_ID
```


### Swagger access

``` 
http://3.231.56.218:8080/swagger-ui/index.html
http://3.231.56.218:8080/swagger-ui/index.html
```
