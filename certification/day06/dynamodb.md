# Dynamo Db Lab
## Create Table

``` 
aws dynamodb create-table \
    --table-name Starships \
    --attribute-definitions \
      AttributeName=ShipClass,AttributeType=S \
      AttributeName=Registry,AttributeType=S \
    --key-schema \
      AttributeName=ShipClass,KeyType=HASH \
      AttributeName=Registry,KeyType=RANGE \
    --provisioned-throughput \
      ReadCapacityUnits=5,WriteCapacityUnits=5 \
    --region us-east-1  
```

## Describe Tables

``` 
aws dynamodb describe-table --table-name --output table
```

## Batch Write Item

### Create batch of json file from CSV

``` 
python csv-to-json-batch.py
```

### Write batch of json to dynamodb

``` 
aws dynamodb batch-write-item --request-items file://json_data/batch_1.json 
aws dynamodb batch-write-item --request-items file://json_data/batch_2.json 
aws dynamodb batch-write-item --request-items file://json_data/batch_3.json 
aws dynamodb batch-write-item --request-items file://json_data/batch_4.json 
aws dynamodb batch-write-item --request-items file://json_data/batch_5.json 
aws dynamodb batch-write-item --request-items file://json_data/batch_6.json 
aws dynamodb batch-write-item --request-items file://json_data/batch_7.json 
aws dynamodb batch-write-item --request-items file://json_data/batch_8.json 
aws dynamodb batch-write-item --request-items file://json_data/batch_9.json 
aws dynamodb batch-write-item --request-items file://json_data/batch_10.json 
aws dynamodb batch-write-item --request-items file://json_data/batch_11.json 
```

## Get items from dynamodb 

### Get Items from dynamo db

``` 
aws dynamodb get-item --table-name Starships --key file://key.json 
```
### Batch Get Items from dynamodb

``` 
aws dynamodb batch-get-item --request-items file://request-items.json --output text

```

## Delete Items from dynamodb

``` 
aws dynamodb delete-item --table-name Starships --key file://key.json 

```
## Put Items to dynamodb

``` 
aws dynamodb put-item --table-name Starships \
    --item file://item.json \
    --return-consumed-capacity TOTAL \
    --return-item-collection-metrics SIZE
```
## Update Item in dynamoDb

``` 
aws dynamodb update-item \
    --table-name Starships \
    --key file://key.json \
    --update-expression "SET #D = :D" \
    --expression-attribute-names file://expression-attribute-names.json \
    --expression-attribute-values file://expression-attribute-values.json  \
    --return-values ALL_NEW 
```

## Scan item in dynamodb

### Scan with json file
``` 
aws dynamodb scan \
    --table-name Starships \
    --filter-expression "ShipClass = :s" \
    --projection-expression "#RE, #DC" \
    --expression-attribute-names file://expression-attribute-scan-names.json \
    --expression-attribute-values file://expression-attribute-scan-values.json
```

### Scan with values

``` 
aws dynamodb scan \
    --table-name Starships \
    --filter-expression "begins_with(Description, :D)" \
    --expression-attribute-values '{":D":{"S":"Destroyed"}}'
```

## Query item from dynamodb(By default no scan forward)

``` 
aws dynamodb query \
    --table-name Starships \
    --projection-expression "Registry" \
    --key-condition-expression "ShipClass = :C" \
    --expression-attribute-values '{":C":{"S":"Galaxy"}}' \
    --return-consumed-capacity TOTAL \
    --output text
    
```
### Query for Scan forward index

``` 
aws dynamodb query \
    --table-name Starships \
    --projection-expression "Registry" \
    --key-condition-expression "ShipClass = :C" \
    --expression-attribute-values '{":C":{"S":"Galaxy"}}' \
    --return-consumed-capacity TOTAL \
    --scan-index-forward \
    --output text
```

## Delete table command

``` 
aws dynamodb delete-table \
    --table-name Starships
```
