# Concepts

## S3

### S3 Server side encription::

### Server-side encryption with Amazon S3 managed keys (SSE-S3)
    The default option for server-side encryption is with Amazon S3 managed keys (SSE-S3)
    256-bit Advanced Encryption Standard (AES-256), to encrypt your data
    "s3:x-amz-server-side-encryption": "AES256"
    "s3:x-amz-server-side-encryption": "true"

### Server-side encryption with AWS Key Management Service (AWS KMS) keys (SSE-KMS)
    Server-side encryption with AWS KMS keys (SSE-KMS) is provided through an integration of the AWS KMS service with Amazon S3
    --server-side-encryption aws:kms
    Correct the policy of the IAM user to allow the kms:GenerateDataKey action
    you have the option to create and manage encryption keys yourself

### Dual-layer server-side encryption with AWS Key Management Service (AWS KMS) keys (DSSE-KMS)
    Dual-layer server-side encryption with AWS KMS keys (DSSE-KMS) is similar to SSE-KMS, 
    but DSSE-KMS applies two individual layers of object-level encryption instead of one layer
    "s3:x-amz-server-side-encryption":"aws:kms:dsse"

### Server-side encryption with customer-provided keys (SSE-C)
    With server-side encryption with customer-provided keys (SSE-C), you manage the encryption keys, 
    and Amazon S3 manages the encryption as it writes to disks and the decryption when you access your objects
    "s3:x-amz-server-side-encryption-customer-algorithm": "true"

### S3 replication:
    S3 lifecycle actions are not replicated with S3 replication
    Same-Region Replication (SRR) and Cross-Region Replication (CRR)
    Replication only replicates the objects added to the bucket after replication is enabled

### S3 Object Ownership:
    S3 Object Ownership to default bucket owner to be the owner of all objects in the bucket
    S3 Object Ownership has two settings: 
        1. Object writer – The uploading account will own the object. 
        2. Bucket owner preferred – The bucket owner will own the object if the object is uploaded with the bucket-owner-full-control canned ACL
### AWS CLI for S3 for pagination
    Amazon S3 has a default page size of 1000
    the AWS CLI calls a service's API to populate the list.

    --page-size: You can use the --page-size option to specify that the AWS CLI requests a smaller number of items from each call to the AWS service

    --max-items: Use to fetch 

    --starting-token

    Example: results of an S3 List to show 100 results per page to your users and minimize the number of API calls 
    aws s3api list-objects \
    --bucket my-bucket \
    --max-items 100 \
    --starting-token eyJNYXJrZXIiOiBudWxsLCAiYm90b190cnVuY2F0ZV9hbW91bnQiOiAxfQ==

### Macie:Sensitive data analysis
    Amazon Macie discovers sensitive data using machine learning and pattern matching, provides visibility into data security risks, 
    and enables automated protection against those risks.

### Versioning
    If you overwrite an object (file), it results in a new object version in the bucket
    when you delete an object (file), Amazon S3 inserts a delete marker,which becomes the current object version and you can restore the previous version
    Any file that was unversioned before enabling versioning will have the 'null' version

### S3 Select:
    You would like to retrieve a CVS data and only 3 columns out of the 10
    
### Bucket deletion:
    If you delete a bucket and immediately list all buckets, the deleted bucket might still appear in the list 
## SQS:

### Maximum message to retrieve
    10

### Visibility timeout
    The default visibility timeout for a message is 30 seconds. The minimum is 0 seconds. The maximum is 12 hours.
    ChangeMessageVisibility: use to change the default value

### ApproximateNumberOfMessagesVisible

    To illustrate with an example, 
    let's say that the current ApproximateNumberOfMessages is 1500 and 
    the fleet's running capacity is 10. 
    If the average processing time is 0.1 seconds for each message and 
    the longest acceptable latency is 10 seconds, 
    then the acceptable backlog per instance is 10 / 0.1, which equals 100. 
    This means that 100 is the target value for your target tracking policy. 
    If the backlog per instance is currently at 150 (1500 / 10), 
    your fleet scales out, and it scales out by five instances to maintain proportion to the target value.

### Message Size
    the max message size is 256KB minimum 1 byte

### Encription
    Enable SQS KMS encryption
    Server-side encryption (SSE) lets you transmit sensitive data in encrypted queues. 
    SSE protects the contents of messages in queues using keys managed in AWS Key Management Service (AWS KMS).

### MessageGroupId
    The message group ID is the tag that specifies that a message belongs to a specific message group. 
    Messages that belong to the same message group are always processed one by one, in a strict order relative to the message group

### MessageDeduplicationId: 
    make sure that duplicate messages should not be sent to SQS as this would cause application failure
    The message deduplication ID is the token used for the deduplication of sent messages. If a message with a particular 
    message deduplication ID is sent successfully, any messages sent with the same message deduplication ID are accepted successfully 
    but aren't delivered during the 5-minute deduplication interval

## Kinensis:

### Kinensys exception:
    type of error and can be one of the following values: 
    ProvisionedThroughputExceededException or InternalFailure.
    ProvisionedThroughputExceededException indicates that the request rate for the stream is too high,
    or the requested data is too large for the available throughput. Reduce the frequency or size of your requests.

### AWS Kinesis Data Streams
     KDS can continuously capture gigabytes of data per second from hundreds of thousands of sources such as website clickstreams
    
    Amazon Kinesis Data Streams that automatically encrypts data before it's at rest by using an AWS KMS customer master key (CMK) you specify

    your data is encrypted at rest within the Kinesis Data Streams service. Also, the HTTPS protocol ensures that data inflight is encrypted as well

### Fanout feature of Kinesis Data Streams
    You should use enhanced fan-out if you have multiple consumers retrieving data from a stream in parallel. 
    With enhanced fan-out developers can register stream consumers to use enhanced fan-out and receive their 
    own 2MB/second pipe of read throughput per shard, and this throughput automatically scales with the number of shards in a stream.


### AWS Kinensis Data Firehose:
    Amazon Kinesis Data Firehose is the easiest way to load streaming data into data stores and analytics tools. It can capture, 
    transform, and load streaming data into Amazon S3, Amazon Redshift, Amazon Elasticsearch Service, and Splunk, enabling near real-time analytics 

    
### AWS Kinesis Data Analytics 
    Amazon Kinesis Data Analytics is the easiest way to analyze streaming data in real-time. 
    You can quickly build SQL queries and sophisticated Java applications using built-in templates and operators for common processing

### Note:
    Data Streams is also a cost-effective option compared to Firehose

### Kinensys agent
    Kinesis Agent is a stand-alone Java software application that offers an easy way to collect and send data to Kinesis Data Streams. 
    The agent continuously monitors a set of files and sends new data to your stream

### Partition Key
    The partition key is used by Kinesis Data Streams to distribute data across shards. 
    Kinesis Data Streams segregates the data records that belong to a stream into multiple shards, 
    using the partition key associated with each data record to determine the shard to which a given data record belongs

### shards
    A shard is a uniquely identified sequence of data records in a stream. A stream is composed of one or more shards, each of which provides a fixed unit of capacity.

    

## IAM

### Identity based policy:
    Identity-based policies are attached to an IAM user, group, or role
    These policies let you specify what that identity can do (its permissions). 
    For example, you can attach the policy to the IAM user named John, stating that 
    he is allowed to perform the Amazon EC2 RunInstances action:
    Example: John can list Read on resources X

### Resource-based policies:
    Resource-based policies are attached to a resource. 
    For example,you can attach resource-based policies to Amazon S3 buckets, Amazon SQS queues, 
    VPC endpoints,and AWS Key Management Service encryption keys
    Example: Resources X John can list read, Mary can List Read, Rama Can list read

### Trust policy:(resource based policy)
    Trust policies define which principal entities (accounts, users, roles, and federated users) can assume the role.
    The IAM service supports only one type of resource-based policy called a role trust policy,
    which is attached to an IAM role.
    
### Execution Role:
    The primary role in account A that gives the lambda function permission to do its work

### Assumed Role
    A role in account B that the lambda function in account A assumes to gain access to cross-account resources.

### AWS Organizations Service Control Policies (SCP)
    Service control policies (SCPs) are a type of organization policy that you can use to manage permissions in your organization
    The SCP limits permissions for entities in member accounts, including each AWS account root user. 
    An explicit deny in any of these policies overrides the allow.

### Access control list (ACL)
    Access control lists (ACLs) are service policies that allow you to control which principals in another account can access a resource. 
    ACLs cannot be used to control access for a principal within the same account. 
    Amazon S3, AWS WAF, and Amazon VPC are examples of services that support ACLs.

### Permissions boundary:
    AWS supports permissions boundaries for IAM entities (users or roles). A permissions boundary is an advanced feature for using a managed policy 
    to set the maximum permissions that an identity-based policy can grant to an IAM entity

### IAM Access Analyzer
    identify unintended access to your resources and data, which is a security risk
    IAM reports the last-used timestamp that represents when a role was last used to make an AWS request.

### IAM roles and resource-based policies delegate access across accounts only within a single partition
    assume that you have an account in US West (N. California) in the standard aws partition. 
    You also have an account in China (Beijing) in the aws-cn partition. 
    You can't use an Amazon S3 resource-based policy in your account in China (Beijing) to allow access for users in your standard AWS account.

### Access Advisor feature on IAM console
    To help identify the unused roles,
    dentify, analyze, and then confidently remove unused roles.

### Amazon Inspector
    security assessment service that helps improve the security and compliance 

### Cross account access
    You can give EC2 instances in one account ("account A") permissions to assume a role from another account ("account B") 
    to access resources such as S3 buckets. 
    You need to create an IAM role in Account B and set Account A as a trusted entity. 
    Then attach a policy to this IAM role such that it delegates access to Amazon S3

### EC2 read data from non public s3 bucket
    Set up an EC2 service role(AWS services) with read-only permissions for the S3 bucket and attach the role to the EC2 instance profile

## Auto Scaling Group(ASG)

### Boundry of ASg:
    An Auto Scaling group can contain EC2 instances in one or more Availability Zones within the same Region.

## EC2

### DeleteOnTermination
    DeleteOnTermination attribute for each attached EBS volume determines whether to preserve or delete the volume. By default, 
    the DeleteOnTermination attribute is set to True for the root volume and is set to False for all other volume types

### Dedicated instance
    Dedicated to single customer,Its can share hardware with other instance

### Dedicated host
    fully dedicated to your use, install your own software licence

### Spot Instances
    less than on demand price

### Reserved Instance
    A Reserved Instance billing benefit can apply to a maximum of 3600 seconds (one hour) of instance usage per clock-hour.
    When you purchase a Reserved Instance for a specific Availability Zone, it's referred to as a Zonal Reserved Instance.
    This gives you the ability to create and manage Capacity Reservations independently from the billing discounts offered 
    by Savings Plans or regional Reserved Instances.

### Monitor EC2
    aws ec2 monitor-instances --instance-ids i-1234567890abcdef0

### EFS
    EFS volumes provide a simple, scalable, and persistent file storage for use with your Amazon ECS tasks. 
    With Amazon EFS, storage capacity is elastic, growing and shrinking automatically as you add and remove files

    Amazon Elastic File System (EFS) Standard–IA storage class 
    The Standard–IA storage class reduces storage costs for files that are not accessed every day
    

### EBS
    Amazon Elastic Block Store (Amazon EBS) is an easy-to-use, scalable, high-performance block-storage service designed for Amazon Elastic Compute Cloud
    Amazon EBS works with AWS KMS to encrypt and decrypt your EBS volume
    EBS volumes support both in-flight encryption and encryption at rest using KMS .
    
    When you create an EBS volume, it is automatically replicated within its Availability Zone to prevent data 
    loss due to the failure of any single hardware component. 
    You can attach an EBS volume to an EC2 instance in the same Availability Zone.
    
    EBS volumes are AZ locked

    EBS Encryption by default is a Region-specific setting. If you enable it for a Region, you cannot disable it for individual 
    volumes or snapshots in that Region

### ElsticIP
    An Elastic IP address is allocated to your AWS account, and is yours until you release it
    An Elastic IP address is static; it does not change over time

### EC2 Volume
    Amazon EC2 Auto Scaling cannot add a volume to an existing instance if the existing volume is approaching capacity.

## Load Balancer

### ALB

#### ALB access log:
    Elastic Load Balancing provides access logs that capture detailed information about requests sent to your load balancer. 
    Each log contains information such as the time the request was received, 
    the client's IP address, latencies, request paths, and server responses

#### ALB request tracing:
    ALB request tracing - You can use request tracing to track HTTP requests. 
    The load balancer adds a header with a trace identifier to each request it receives

#### ALB target type
    An ALB has three possible target types: Instance, IP and Lambda
    Instance - The targets are specified by instance ID
    IP - The targets are IP addresses
        When the target type is IP, you can specify IP addresses from specific CIDR blocks only. You can't specify publicly routable IP addresses.
    Lambda - The target is a Lambda function
    

### Load Balancer Sticky sessions
    Sticky sessions are a mechanism to route requests to the same target in a target group

### Classic Load Balancer
    Classic Load Balancer doesn't allow you to run multiple copies of a task on the same instance

## API Gateway

### Mapping teamplate
    propagate response with variable instead of actual value of response
    foreach($elem in $inputRoot.bins)
    {
      "kind": "$elem.type",
      "suggestedPrice": "$elem.price per $elem.unit",
      "available": $elem.quantity
    }#if($foreach.hasNext),#end

### API Gateway Usage Plans
    who can access on  how much and how fast they can access them

### API caching in API Gateway
    optimizing your API to improve responsiveness, like response caching and payload compression
    reduce the number of calls made to your endpoint and also improve the latency of requests to your API
### CORS
    Cross-origin resource sharing (CORS) defines a way for client web applications that are loaded in one domain 
    to interact with resources in a different domain.
    When your API's resources receive requests from a domain other than the API's own domain and you want to restrict 
    servicing these requests, you must disable cross-origin resource sharing (CORS) for selected methods on the resource
    Disable CORS: restrict access from other domain

### Test to prod upgrade
    The promotion can be done by redeploying the API to the prod stage or 
    updating a stage variable value from the stage name of test to that of prod.

### Invalidate Api caching
    invalidate caching for the API clients to get the most recent responses
    The client receives the response directly from the integration endpoint instead of the cache
    Using the Header Cache-Control: max-age=0

### STS
    AWS Security Token Service (AWS STS) is a web service that enables you to request temporary, limited-privilege credentials for 
    AWS Identity and Access Management (IAM) users or for users that you authenticate (federated users). 
    However, it is not supported for access API Gateway.
    But (STS) is used by API Gateway for logging data to CloudWatch logs.
    
## SSM Parameter Store
    store data such as passwords, database strings, and license codes as parameter values. 
    SSM Parameter Store cannot be used to automatically rotate the database credentials.


## AWS Serverless Application Repository (SAR)
     individual developers to store and share reusable applications, and easily assemble and deploy serverless architectures


## X-Ray
    You can use X-Ray to collect data across AWS Accounts

### X-Ray Daemon:
    Can download and install in on prem system to cature and relay data to x-ray service
    It use UDP port 2000 to listen 

### Annotation
    XRay traces to search and filter through them efficiently.
    Annotations are simple key-value pairs that are indexed for use with filter expressions. Use annotations to record data that 
    you want to use to group traces in the console, or when calling the GetTraceSummaries API.

### AWS_XRAY_DAEMON_ADDRESS
    Set the host and port of the X-Ray daemon listener. By default, the SDK uses 127.0.0.1:2000 for both trace data (UDP) and sampling (TCP). 
    Use this variable if you have configured the daemon to listen on a different port or if it is running on a different host.

    

## Lambda

### Lambda Authorizer
    An Amazon API Gateway Lambda authorizer (formerly known as a custom authorizer) 
    is a Lambda function that you provide to control access to your API.
    A Lambda authorizer uses bearer token authentication strategies, such as OAuth or SAML

    Configure Lambda to connect to VPC with private subnet and Security Group needed to access RDS 

### Concurency
    In Lambda, concurrency is the number of in-flight requests your function is handling at the same time. 
    There are two types of concurrency controls available

### Reserved concurrency: limit the lambda running concurency
    
    Reserved concurrency is the maximum number of concurrent instances you want to allocate to your function. 
    Ensure no other function can use that concurrency.

    When a function has reserved concurrency, no other function can use that concurrency. 
    There is no charge for configuring reserved concurrency for a function

### Provisioned concurrency: cold start improve
    Minimize startup time for lambda or optimize the startup time of the Lambda function
    Provisioned concurrency is the number of pre-initialized execution environments you want to allocate to your function. 
    These execution environments are prepared to respond immediately to incoming function requests. 
    Configuring provisioned concurrency incurs charges to your AWS account

### Lambda Memory
    Lambda account quota: your account quota shows 10GB
    between 128 MB and 10,240 MB
    At 1,769 MB, a function has the equivalent of one vCPU
    The maximum amount of memory available to the Lambda function at runtime is 10,240 MB. 
    Your Lambda function was deployed with 10,240 MB of RAM, but it seems your code requested or used more than that, so the Lambda function failed.

### Dependency
    dependencies already provided by AWS in your Lambda Runtime (aws-sdk and cfn-response and many other AWS related libraries are preloaded via, 
    for example, boto3 (python) in the lambda instances.)
## DynamoDB:

### Parallel Scan:
    Amazon DynamoDB returns data to the application in 1 MB increments, 
    and an application performs additional Scan operations to retrieve the next 1 MB of data
    parallel Scan feature, you will need to run multiple worker threads or processes in parallel

### FilterExpression
    A filter expression determines which items within the Scan results should be returned to you. All of the other results are discarded.
    A filter expression is applied after a Scan finishes, but before the results are returned.
    
    similar to WHERE clauses in SQL

    The below example shows how to use the filter expression to get all projects that contain the word "Project" in their name.
    TableName: 'projects-manager',
    FilterExpression : "contains(#name, :name)",
    ExpressionAttributeNames: { "#name": "name" },
    ExpressionAttributeValues: {
        ':name':"Project"
    }
    

### Project expression:
    allow you to retrieve a subset of the attributes coming from a DynamoDB scan
    A projection expression is a string that identifies the attributes that you want. To retrieve a single attribute, specify its name. 
    For multiple attributes, the names must be comma-separated.
    
    Its similar to select column in sql.
    SELECT name,is_active FROM customers    

    Ex:
    aws dynamodb get-item \
    --table-name ProductCatalog \
    --key file://key.json \
    --projection-expression "Description, RelatedItems[0], ProductReviews.FiveStar"
    OutPut:
    {
    "Item": {
        "Description": {
            "S": "123 description"
        },
        "ProductReviews": {
            "M": {
                "FiveStar": {
                    "L": [
                        {
                            "S": "Excellent! Can't recommend it highly enough! Buy it!"
                        },
                        {
                            "S": "Do yourself a favor and buy this."
                        }
                    ]
                }
            }
        }
      }
    }
    
    
### Two table write consistency
    You can use DynamoDB transactions to make coordinated all-or-nothing changes to multiple items both within and across tables.
    Complete both operations on RDS MySQL in a single transaction block
 
### Conditional writes
     A conditional write succeeds only if the item attributes meet one or more expected conditions. Otherwise, it returns an error.

### Batch writes
    Bath operations (read and write) help reduce the number of network round trips from your application to DynamoDB. 
    In addition, DynamoDB performs the individual read or write operations in parallel

### TransactWriteItems 
    is a synchronous and idempotent write operation that groups up to 25 write actions in a single all-or-nothing operation
    The aggregate size of the items in the transaction cannot exceed 4 MB
### Hot Partition:
    When data access is imbalanced, a "hot" partition can receive a higher volume of read and write traffic compared to other partitions

### Backup
    DynamoDB has two built-in backup methods (On-demand, Point-in-time recovery) 
    that write to Amazon S3, but you will not have access to the S3 buckets that are used for these backups.

### Indexing
    AWS DynamoDB being a No SQL database doesn’t support queries such as SELECT with a condition such as the following query.
    SELECT * FROM Users WHERE email='username@email.com';
    It is possible to obtain the same query result using the DynamoDB scan operation. 
    However, scan operations access every item in a table which is slower than query operations that access items at specific indices

### GSI
    An index with a partition key and a sort key that can be different from those on the base table.
    A global secondary index is considered "global" because queries on the index can span all of the data in the base table, across all partitions
    Consider this table that contains Uuid (as primary key), UserId and Data attributes.

    | Uuid(Partition Key) | UserId | Data |
    With this base table key schema, it can answer queries to retrieve data for a uuid. However, to get all data for a UserId, 
    it would have to do a scan query and get all the items that have matching user id.

    To be able to get all data for a user efficiently, you can use a global secondary index that has UserId as its primary key (partition key). 
    Using this index, you can do a query to retrieve all data for a user.

    In short, use DynamoDB Global Secondary Index when you need to support querying non-primary key attribute of a table.
    Ex: 
    SELECT * FROM user WHERE UserId='1234'


### LSI
    An index that has the same partition key as the base table, but a different sort key. A local secondary index is "local" in the sense that 
    every partition of a local secondary index is scoped to a base table partition that has the same partition key value.

    LSI use the RCU and WCU of the main table

    Local Secondary Index enables different sorting order of the same list of items as LSI uses the same partition key as base table but different sort key. 
    Consider this table that uses composite keys: UserId as partition key, ArticleName as sort key and other attributes: DateCreated and Data.

    |UserId(Partition Key) | ArticleName(Sort Key) | DateCreated | Data|

    With this base table key schema, it can answer queries to retrieve all the article sorted by names for a specific user(query by UserId). However, 
    to retrieve all the articles associated with a user sorted by date created, you would have to retrieve all the articles first and sort them.

    With a local secondary index that has UserId as its partition key and DateCreated as its sort key, you can retrieve a user’s articles sorted by date created.

    |UserId(Partition Key) | DateCreated(Sort Key) | ArticleName | Data|

    And, use DynamodB Local Secondary index when you need to support querying items with different sorting order of attributes.
    Ex:
    SELECT * FROM user ORDER BY DateCreated

### Global tables
    This can significantly reduce latency for your users. So, reducing the distance between the client and the DynamoDB endpoint is an 
    important performance fix to be considered.

## ElastiCache

### Write Through strategy
    The write-through strategy adds data or updates data in the cache whenever data is written to the database.

### Lazy Loading strategy without TTL
    Lazy Loading is a caching strategy that loads data into the cache only when necessary. Whenever your application requests data, 
    it first requests the ElastiCache cache. If the data exists in the cache and is current,ElastiCache returns the data to your application. 
    If the data doesn't exist in the cache or has expired, your application requests the data from your data store.

### Lazy Loading strategy with TTL
    In the case of Lazy Loading, the data is loaded onto the cache whenever the data is missing from the cache. 
    In case the blog gets updated, it won't be updated from the cache unless that cache expires (in case you used a TTL)
    

### Elasticache for redis
    ElastiCache for Redis with cluster mode enabled to enhance reliability and availability with little change to your existing workload.
    All the nodes in a Redis cluster (cluster mode enabled or cluster mode disabled) must reside in the same region
    While using Redis with cluster mode enabled, there are some limitations:

        You cannot manually promote any of the replica nodes to primary.

        Multi-AZ is required.

        You can only change the structure of a cluster, the node type, and the number of nodes by restoring from a backup.

## AWS Elastic Beanstalk

### All at once
    'All at once' is the quickest deployment method, but the application may become unavailable to users (or have low availability) for a short time. 
    Also in case of deployment failure, the application sees a downtime
### Rolling
    This policy avoids downtime and minimizes reduced availability, at a cost of a longer deployment time. 
    However in case of deployment failure, the rollback process is via manual redeploy

### Rolling with additional batch
    This policy avoids any reduced availability, at a cost of an even longer deployment time compared to the Rolling method. 
    Suitable if you must maintain the same bandwidth throughout the deployment. However in case of deployment failure, 
    the rollback process is via manual redeploy
### Immutable
    The 'Immutable' deployment policy ensures that your new application version is always deployed to new instances, 
    instead of updating existing instances. It also has the additional advantage of a quick and safe rollback in case the deployment fails. 
    In an immutable update, a second Auto Scaling group is launched in your environment and the new version serves traffic alongside the 
    old version until the new instances pass health checks. 
    In case of deployment failure, the new instances are terminated, so the impact is minimal

### Blue green deployement
    Each blue green deploy swap the EB environment and DNS level swapping(ROute53 swap).
    Each new version deploy the user session will be lost so maintain the Elasticache for user session

### In place deployment
    An in-place deployment allows you to deploy your application without creating new infrastructure; 
    however, the availability of your application can be affected during these deployments

### Canary Deployment
    the canary deployement receives a small percentage of API traffic and the production release takes up the rest

### Cron job
    Elastic Beanstalk environment should you set up for performing the repetitive tasks with Setup a Worker environment and a cron.yaml file
    

## Code Deploy:
    The CodeDeploy agent cleans up these artifacts to conserve disk space.
### Deployement Group
    The deployment group contains settings and configurations used during the deployment
    Some settings, such as rollbacks, triggers, and alarms can be configured for deployment groups for any compute platform.

## Express workflow
    Express Workflows support event rates of more than 100,000 per second.
    You should use Express Workflows for workloads with high event rates and short durations

## CloudFormation

### Drift Ditection
    Drift detection enables you to detect whether a stack's actual configuration differs, or has drifted, from its expected configuration.
    Use CloudFormation to detect drift on an entire stack, or individual resources within the stack
    
### Stack deletion:
    All of the imports must be removed before you can delete the exporting stack or modify the output value

### cloudformation package
    The cloudformation package command packages the local artifacts (local paths) that your AWS CloudFormation template references. 
    The command will upload local artifacts, such as your source code for your AWS Lambda function.

### Pseudo parameter
    Pseudo parameters are parameters that are predefined by AWS CloudFormation. 
    You don't declare them in your template. Use them the same way as you would a parameter, as the argument for the Ref function.
    You can access pseudo parameters in a CloudFormation template like so:

    Outputs:
        MyStacksRegion:
            Value: !Ref "AWS::Region"

    The AWS::Region pseudo parameter returns a string representing the Region in which the encompassing resource is being created, such as us-west-2.

### Export
    To export a stack's output value, use the Export field in the Output section of the stack's template.
    To import those values, use the Fn::ImportValue function in the template for the other stacks.
    Output

### ImportValue
    To import the values exported by another stack, we use the Fn::ImportValue function in the template for the other stacks
    Input

## Cloud Front
    When you create signed URLs or signed cookies, you use the private key from the signer’s key pair to sign a portion of the URL or the cookie. 
    When someone requests a restricted file, CloudFront compares the signature in the URL or cookie with the unsigned URL or cookie, 
    to verify that it hasn’t been tampered with
    you can only have up to two active CloudFront key pairs per AWS account

### Fail over
    CloudFront only sends requests to the secondary origin after a request to the primary origin fails.


### CloudFront CACHE
    CloudFront can cache different versions of your content based on the values of query string parameters.   
    Then specify the parameters that you want CloudFront to use as a basis for caching in the Query string whitelist field

### CloudFront distribution
    When you associate a CloudFront function with a CloudFront distribution, CloudFront intercepts requests and responses 
    at CloudFront edge locations and passes them to your function.

## VPC

### VPC Flow Logs - 
    VPC Flow Logs is a feature that enables you to capture information about the IP traffic going to and from network interfaces in your VPC
### VPC endpoint
    A VPC endpoint enables you to privately connect your VPC to supported AWS services and VPC endpoint services powered by 
    AWS PrivateLink without requiring an internet gateway, NAT device, VPN connection, or AWS Direct Connect connection
    There are two types of VPC endpoints: 
    interface endpoints:  An interface endpoint is an elastic network interface with a private IP address 
    gateway endpoints:A gateway endpoint is a gateway that you specify as a target for a route in your 
                      route table for traffic destined to a supported AWS service

## CodeCommit

### Encription
    AWS CodeCommit repositories is encrypted in transit and at rest. When data is pushed into an AWS CodeCommit repository (for example, by calling git push), 
    AWS CodeCommit encrypts the received data as it is stored in the repository.


## Cloudwatch

### Encription
    Use the AWS CLI associate-kms-key command and specify the KMS key ARN
    To associate the CMK with an existing log group, you can use the associate-kms-key command.

### CloudWatch Events
    Amazon CloudWatch Events delivers a near real-time stream of system events that describe changes in Amazon Web Services (AWS) resources    

### CloudWatch agent
    Collect system-level metrics from on-premises servers
    Collect logs from Amazon EC2 instances and on-premises servers, running either Linux or Windows Server
    CloudWatch agent to send data from an on-premises server
    

## CloudTrail

### Audit
    Audit using CloudTrail: AWS CloudTrail is a service that enables governance, compliance, operational auditing, and risk auditing of your AWS account.

## STS
    AWS provides AWS Security Token Service (AWS STS) as a web service that enables you to request temporary, limited-privilege credentials for user.
    AWS STS supports AWS CloudTrail, a service that records AWS calls for your AWS account and delivers log files to an Amazon S3 bucket
    It is not supported with API Gateway
### Time of validity
    Credentials that are created by using account credentials can range from 900 seconds (15 minutes) up to a maximum of 3,600 seconds (1 hour), 
    with a default of 1 hour

### Exception
    Encoded authorization failure message:AWS STS decode-authorization-message
    If a user is not authorized to perform an action that was requested, the request returns a Client.UnauthorizedOperation response (an HTTP 403 response). 

### Cloud trail for EBS
    AWS CloudTrail event logs for 'CreateVolume' aren't available for EBS volumes created during an Amazon EC2 launch

## NACL
### Stateless
    Nacl is stateless:If configure inbound need explicitely to configure outbound policy
    Network ACLs to allow outbound traffic on ports 1024 - 65535

## Code Build

### Its use buildspec.yml file 
    For automatically encript at the end it can use AWS KMS 

## AWS KMS

### Size for KMS
    Maximum size supported for KMS is 4 KB

