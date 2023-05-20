## Secret Manager 

### Describe Secret for secret id
``` 
aws secretsmanager describe-secret --secret-id enterprise/Shipdatabase 
aws secretsmanager describe-secret --secret-id /rama/data/secret --profile wcar-voc-nonprod
```

### Get secret for secret-id

``` 
aws secretsmanager get-secret-value --secret-id enterprise/Shipdatabase 
aws secretsmanager get-secret-value --secret-id /rama/data/secret --profile wcar-voc-nonprod
```
