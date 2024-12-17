# S3

    Amazon S3 object is owned by the AWS account that uploaded it.This is true even when the bucket is owned by another account

## S3 Prefixing

    Amazon S3 automatically scales to high request rates. For example, 
    your application can achieve at least 3,500 PUT/COPY/POST/DELETE or 5,500 GET/HEAD requests per second per prefix in a bucket.
    There are no limits to the number of prefixes in a bucket. You can increase your read or write performance by parallelizing reads. For example, 
    if you create 10 prefixes in an Amazon S3 bucket to parallelize reads, you could scale your read performance to 55,000 read requests per second.

## S3 Transfer Acceleration (Amazon S3TA)

    Amazon S3 Transfer Acceleration enables fast, easy, and secure transfers of files over long distances between your client and an S3 bucket. 
    Amazon S3TA takes advantage of Amazon CloudFront’s globally distributed edge locations. 
    As the data arrives at an edge location, data is routed to Amazon S3 over an optimized network path.
    There are no S3 data transfer charges when data is transferred in from the internet. Also with S3TA, you pay only for transfers that are accelerated

## S3 Versioning

    Once you version-enable a bucket, it can never return to an unversioned state. 
    Versioning in Amazon S3 is a means of keeping multiple variants of an object in the same bucket. 
    You can use the S3 Versioning feature to preserve, retrieve, and restore every version of every object stored in your buckets.
    Ex:
    Versioning-enabled buckets can help you recover objects from accidental deletion or overwrite. 
    For example, if you delete an object, Amazon S3 inserts a delete marker instead of removing the object permanently. 
    The delete marker becomes the current object version. If you overwrite an object, it results in a new object version in the bucket. 
    You can always restore the previous version. 

## S3 Delete Protection

    Enable multi-factor authentication (MFA) delete on the Amazon S3 bucket

## Amazon S3 Object Lock

    Amazon S3 Object Lock is an Amazon S3 feature that allows you to store objects using a write once, read many (WORM) model.
    You can use WORM protection for scenarios where it is imperative that data is not changed or deleted after it has been written.

## Amazon S3 applies action to a group of objects.

     There are two types of actions:
        1)Transition actions — Define when objects transition to another storage class. 
                                For example, you might choose to transition objects to the S3 Standard-IA storage class 30 days after you created them
        2)Expiration actions — Define when objects expire. Amazon S3 deletes expired objects on your behalf.

## S3 sync command

    The aws S3 sync command uses the CopyObject APIs to copy objects between Amazon S3 buckets. 
    The sync command lists the source and target buckets to identify objects that are in the source bucket but that aren't in the target bucket.

## S3 Retaintion

## S3 Encription:

    1) SSE-S3: Server-Side Encryption with Amazon S3-Managed Keys.
         this option does not provide the ability to audit trail the usage of the encryption keys
         SSE-S3, you cannot log the usage of the encryption key for auditing purposes
    2)SSE-C: Server-Side Encryption with Customer-Provided Keys (SSE-C), you manage the encryption keys and Amazon S3 manages the encryption, as it writes to disks.
        decryption when you access your objects. However this option does not provide the ability to audit trail the usage of the encryption keys.
    3)SSE-KMS:server-side encryption with AWS KMS (SSE-KMS)  you can specify a customer-managed CMK that you have already created.
        SSE-KMS provides you with an audit trail that shows when your CMK was used and by whom.
        AWS KMS is a secure and resilient service that uses hardware security modules that have been validated under FIPS 140-2.
        Deleting an AWS KMS key in AWS Key Management Service (AWS KMS) is destructive and potentially dangerous. Therefore, AWS KMS enforces a waiting period. 
        To delete a KMS key in AWS KMS you schedule key deletion. You can set the waiting period from a minimum of 7 days up to a maximum of 30 days. 

## s3 Infrequent access(s3-IA)

     Unlike other S3 Storage Classes which store data in a minimum of three Availability Zones (AZs), 
     Amazon S3 One Zone-IA stores data in a single Availability Zone (AZ) and costs 20% less than Amazon S3 Standard-IA. 
     The minimum storage duration is 30 days before you can transition objects from Amazon S3 Standard to Amazon S3 One Zone-IA.

## S3 Pricing 1 GB/Month= $0.023

    S3 Standard storage, the pricing is $0.023 per GB per month. Therefore, the monthly storage cost on S3 for the test file is $0.023.

## Amazon S3 Glacier

## Amazon S3 Glacier Deep Archive

    Amazon S3 Glacier Deep Archive provides more cost savings than Amazon S3 Glacier.
    you should use Amazon S3 Glacier Deep Archive for long term archival for this use-case.

## Amazon S3 Glacier Vault

## Amazon S3 Glacier Deep Archive Vault

# EFS: Share drive

    EFS volumes provide a simple, scalable, and persistent file storage for use with your Amazon ECS tasks. 
    With Amazon EFS, storage capacity is elastic, growing and shrinking automatically as you add and remove files

    Amazon Elastic File System (EFS) Standard–IA storage class 
    The Standard–IA storage class reduces storage costs for files that are not accessed every day

# EBS:  Hard drive to virtual servers (EC2 instances)

    Amazon EBS is a block-level storage service for use with Amazon EC2. 
    Amazon EBS can deliver performance for workloads that require the lowest latency access to data from a single Amazon EC2 instance
    The Amazon EBS volume types fall into two categories:
    1) Solid state drive (SSD)
        backed volumes optimized for transactional workloads involving frequent read/write operations with small I/O size, where the dominant performance attribute is IOPS.
    2) Hard disk drive (HDD)
        Hard disk drive (HDD) backed volumes optimized for large streaming workloads where throughput (measured in MiB/s) is a better performance measure than IOPS.

    Throughput Optimized HDD (st1) and Cold HDD (sc1) volume types CANNOT be used as a boot volume.
    
    General Purpose SSD (gp2), Provisioned IOPS SSD (io1), and Instance Store can be used as a boot volume.
    
    DeleteOnTermination:The default behavior can be changed to ensure that the volume persists after the instance terminates.DeleteOnTermination attribute to false

    The recover action is supported only on instances that have Amazon EBS volumes configured on them, 
                    instance store volumes are not supported for automatic recovery by Amazon CloudWatch alarms.

## Throughput Optimized HDD (st1) : IOPS/Volume of 500.

    st1 is backed by hard disk drives (HDDs) and is ideal for frequently accessed, throughput-intensive workloads with large datasets and large I/O sizes, 
    such as MapReduce, Kafka, log processing, data warehouse, and ETL workloads. 
    It supports max IOPS/Volume of 500.

## Cold HDD (sc1) :IOPS/Volume of 250

    sc1 is backed by hard disk drives (HDDs). It is ideal for less frequently accessed workloads with large, cold datasets. 
    It supports max IOPS/Volume of 250.

## Provisioned IOPS SSD (io1) :IOPS/Volume of 64,000

    Provisioned IOPS SSD (io1) is backed by solid-state drives (SSDs) 
    and is a high-performance Amazon EBS storage option designed for critical, I/O intensive database and application workloads, as well as throughput-intensive database workloads.
    
    io1 is designed to deliver a consistent baseline performance of up to 50 IOPS/GB to a maximum of 64,000 IOPS and provide up to 1,000 MB/s of throughput per volume.

## General Purpose SSD (gp2) : IOPS/Volume of 16,000

     gp2 is backed by solid-state drives (SSDs) and is suitable for a broad range of transactional workloads, 
    including dev/test environments, low-latency interactive applications, and boot volumes. 
    It supports max IOPS/Volume of 16,000.

## EBS Pricing 1 GB/Month= $0.10

    Amazon EBS Elastic Volumes, you pay only for the resources that you use. 
    EBS General Purpose SSD (gp2) volumes, the charges are $0.10 per GB-month of provisioned storage. 
    Therefore, for a provisioned storage of 100GB for this use-case, the monthly cost on EBS is $0.10*100 = $10

## EFS Pricing 1 GB/Month= $0.30

    The Amazon EFS Standard Storage pricing is $0.30 per GB per month. Therefore the cost for storing the test file on EFS is $0.30 for the month.

# Amazon Elastic File System (Amazon EFS) :shared drive that can grow or shrink automatically as you add or remove files

    Amazon Elastic File System (Amazon EFS) provides a simple, scalable, fully managed elastic NFS(Network File System) file system for use 
    with AWS Cloud services and on-premises resources.
    Amazon EFS is a regional service storing data within and across multiple Availability Zones (AZs) for high availability and durability
    Amazon EC2 instances can access your file system across AZs, regions, and VPCs, while on-premises servers can access using AWS Direct Connect or AWS VPN.
    You can connect to Amazon EFS file systems from EC2 instances in other AWS regions using an inter-region VPC peering connection

# AWS Snowball Edge Storage

    AWS Snowball Edge Storage Optimized is the optimal choice if you need to securely and quickly transfer dozens of terabytes to petabytes of data to AWS.
    It provides up to 80 Terabytes of usable HDD storage, 40 vCPUs, 1 TB of SATA SSD storage, and up to 40 Gigabytes network connectivity to 
    address large scale data transfer and pre-processing use cases.

# AWS Cloud Trail

    AWS CloudTrail integrates with the Amazon CloudWatch service to publish the API calls being made to resources or services in the AWS account. 
    The published event has invaluable information that can be used for compliance, auditing, and governance of your AWS accounts.
    For the AWS Cloudtrail logs available in Amazon CloudWatch Logs, you can begin searching and filtering the log data by creating one or more metric filters

    AWS CloudTrail cannot stream data to Amazon Kinesis. Amazon S3 buckets and Amazon CloudWatch logs are the only destinations possible.

# Aws Cloud Front

    Amazon CloudFront is a web service that gives businesses and web application developers an easy and cost-effective way to 
    distribute content with low latency and high data transfer speeds. 
    Amazon CloudFront uses standard cache control headers you set on your files to identify static and dynamic content. 
    
    You can use different origins for different types of content on a single site – 
    e.g. Amazon S3 for static objects, Amazon EC2 for dynamic content, and custom origins for third-party content.
    
    no data transfer fee from Amazon S3 to CloudFront only pay for what is delivered to the internet from Amazon CloudFront, plus request fees

    CloudFront cannot have a custom origin pointing to the DNS record of the website on Route 53.
    
    Dynamic content, as determined at request time (cache-behavior configured to forward all headers), does not flow through regional edge caches, but goes directly to the origin.
    Proxy methods PUT/POST/PATCH/OPTIONS/DELETE go directly to the origin from the POPs and do not proxy through the regional edge caches

# Aws Lambda

    AWS Lambda currently supports 1000 concurrent executions per AWS account per region. 
    If your Amazon SNS message deliveries to AWS Lambda contribute to crossing these concurrency quotas, your Amazon SNS message deliveries will be throttled. 
    You need to contact AWS support to raise the account limit.

# SNS

    Amazon SNS follows the "publish-subscribe" (pub-sub) messaging paradigm, with notifications being delivered to clients using a "push" mechanism. 

# SQS

    Amazon SQS is a polling mechanism, that gives applications the chance to poll at their own comfort

## short polling

    Amazon SQS sends the response right away, even if the query found no messages

## long polling

    Amazon SQS sends a response after it collects at least one available message

## Standard queues

    Standard queues offer maximum throughput, best-effort ordering, and at-least-once delivery.

## SQS FIFO

    SQS FIFO queues are designed to guarantee that messages are processed exactly once, in the exact order that they are sent.
    By default, FIFO queues support up to 300 messages per second (300 send, receive, or delete operations per second). 
    When you batch 10 messages per operation (maximum), FIFO queues can support up to 3,000 messages per second.
    
    By default, FIFO queues support up to 3,000 messages per second with batching, 
    up to 300 messages per second (300 send, receive, or delete operations per second) without batching.
    The name of a FIFO queue must end with the .fifo suffix.

# I/O-Intensive Workloads

    I/O-intensive workloads are characterized by frequent or heavy input/output operations. 
    These workloads rely heavily on reading from or writing to disk, network, or other I/O devices, 
    making their performance dependent on the speed and efficiency of the I/O subsystem.

# Throughput-Intensive Workloads

    Throughput-intensive workloads focus on processing or transferring large volumes of data over time. 
    They prioritize data bandwidth (amount of data processed per second) rather than the speed of individual operations.

## Delay Queue:

    Delay queues let you postpone the delivery of new messages to a queue for several seconds.
    If you create a delay queue, any messages that you send to the queue remain invisible to consumers for the duration of the delay period.
    The default (minimum) delay for a queue is 0 seconds. The maximum is 15 minutes.

## visibility timeout

    Visibility timeout is a period during which Amazon SQS prevents other consumers from receiving and processing a given message.
    The default visibility timeout for a message is 30 seconds. The minimum is 0 seconds. The maximum is 12 hours.

## Message Group ID

    If we don't specify a GroupID, then all the messages are in absolute order, but we can only have 1 consumer at most. 
    To allow for multiple consumers to read data for each Desktop application, and to scale the number of consumers, we should use the "Group ID" attribute

## Standard queues

# Security Group

    In AWS, Security Groups act as virtual firewalls that control inbound and outbound traffic to and from your Amazon EC2 instances.

## Inbound Rules

     Inbound rules control the incoming traffic to your instances. These rules specify what kind of traffic is allowed to reach your instances and on which ports.
        Protocol: The network protocol (e.g., TCP, UDP, ICMP) the rule applies to.
        Port Range: The range of ports to which the rule applies (e.g., port 80 for HTTP, port 22 for SSH).
        Source: The source of the traffic, which can be an IP address, CIDR block, or another security group.
        Example: Allow SSH (port 22) access from a specific IP range like 203.0.113.0/24.
    Example Use Case:
    Allow HTTP traffic on port 80 from the internet (source 0.0.0.0/0).
    Allow SSH traffic on port 22 from a specific trusted IP (192.168.1.1/32).

## Outbound Rules

    Outbound rules control the traffic leaving your instances. They specify what kind of traffic your instances are allowed to send out and to where.
    Protocol: The network protocol (e.g., TCP, UDP, ICMP).
    Port Range: The range of destination ports to which the rule applies.
    Destination: The destination for the traffic, which can be an IP address, CIDR block, or another security group.
    Example Use Case:
        Allow all outbound internet traffic for instances to fetch updates or communicate with external services (0.0.0.0/0 as the destination).
        Restrict outbound traffic to a specific IP range (192.168.10.0/24).
    . By default, security groups allow all outbound traffic.
    PostgreSQL port = 5432 HTTP port = 80 HTTPS port = 443

## AWS DataSync

    AWS DataSync is an online data transfer service that simplifies, automates, 
    and accelerates copying large amounts of data between on-premises storage systems and AWS Storage services, as well as between AWS Storage services.
    
    You can use AWS DataSync to migrate data located on-premises, at the edge, or in other clouds to Amazon S3, 
    Amazon EFS, Amazon FSx for Windows File Server, Amazon FSx for Lustre, Amazon FSx for OpenZFS, and Amazon FSx for NetApp ONTA

# EC2

## Reserved Instances

    Amazon EC2 Reserved Instances for the production application as it is run 24*7. This way you can get a 72% discount if you avail a 3-year term.

## on-demand instances

    On-demand offers the flexibility to only pay for the Amazon EC2 instance when it is being used (0 to 8 hours for the given use case).

## Spot Instances EC2

    Spot Instances are available at up to a 90% discount compared to On-Demand prices
    Spot blocks EC2  can only be used for a span of up to 6 hours
    You can use Spot Instances for various stateless, fault-tolerant, or flexible applications.
    Spot instances are better at handling such batch jobs.
    
    The hourly price for a Spot Instance is called a Spot price.
    A Spot Instance request is either one-time or persistent. If the spot request is persistent, the request is opened again after your Spot Instance is interrupted
      
    If the request is persistent and you stop your Spot Instance, the request only opens after you start your Spot Instance.
    canceling the request does not terminate the instance; you must terminate the running Spot Instance manually

## Dedicated Instances

    Dedicated Instances are Amazon EC2 instances that run in a virtual private cloud (VPC) on hardware that's dedicated to a single customer.
    Dedicated Instances that belong to different AWS accounts are physically isolated at a hardware level, even if those accounts are linked to a single-payer account. 
    Dedicated Hosts allow you to use your existing software licenses on EC2 instances.This option is costlier than the Dedicated Instance .
    Shared (Shared) – Multiple AWS accounts may share the same physical hardware. This is the default tenancy option when launching an instance.

    Key Concept:
        . If either Launch Template Tenancy or VPC Tenancy is set to dedicated, then the instance tenancy is also dedicated. 
        . If you set the Launch Template Tenancy to shared (default) and the VPC Tenancy is set to dedicated, then the instances have dedicated tenancy
        . If you set the Launch Template Tenancy to dedicated and the VPC Tenancy is set to default, then again the instances have dedicated tenancy.

## Dedicated Hosts

    An Amazon EC2 Dedicated Host is a physical server with EC2 instance capacity fully dedicated to your use. 
    With a Dedicated Host, you have visibility and control over how instances are placed on the server.

## Spot Fleet

    The Spot Fleet selects the Spot Instance pools that meet your needs and launches Spot Instances to meet the target capacity for the fleet.
    Spot Fleets are set to maintain target capacity by launching replacement instances after Spot Instances in the fleet are terminated.

## Auto Scaling

    Configure your Auto Scaling group by creating a scheduled action that kicks-off at the
    Scheduled scaling allows you to set your own scaling schedule. For example, 
    let's say that every week the traffic to your web application starts to increase on Wednesday, remains high on Thursday, and starts to decrease on Friday. 

## cluster placement group : Node to Node ,HPC

    Cluster placement groups pack instances close together inside an Availability Zone. 
    These are recommended for applications that benefit from low network latency, high network throughput
    High Performance Computing (HPC):
    HPC workloads need to achieve low-latency network performance necessary for tightly-coupled node-to-node communication that is typical of HPC applications

## partition placement group: Haddop Kafka

    A partition placement group spreads your instances across logical partitions such that 
    groups of instances in one partition do not share the underlying hardware with groups of instances in different partitions
    This strategy is typically used by large distributed and replicated workloads, such as Hadoop, Cassandra, and Kafka.

## spread placement group : each rack having its own network and power source

    A spread placement group is a group of instances that are each placed on distinct racks, with each rack having its own network and power source.
     The instances are placed across distinct underlying hardware to reduce correlated failures.
    You can have a maximum of seven running instances per Availability Zone per group. Since a spread placement group can span multiple Availability Zones in the same Region, 
    therefore instances will not have low-latency network performance. Hence spread placement group is not the right fit for HPC applications.

## Instance Store based Amazon EC2 instances:  physically attached to the host computer.

    An instance store provides temporary block-level storage for your instance. This storage is located on disks that are physically attached to the host instance. 
    Instance store is ideal for the temporary storage of information that changes frequently such as buffers, caches, scratch data, and other temporary content, 
    or for data that is replicated across a fleet of instances, such as a load-balanced pool of web servers
    
    Instance store volumes are included as part of the instance's usage cost.
    As Instance Store based volumes provide high random I/O performance at low cost 

## Amazon EC2 Instance Hibernate

    When you hibernate an instance, AWS signals the operating system to perform hibernation (suspend-to-disk). 
     Hibernation saves the contents from the instance memory (RAM) to your Amazon EBS root volume.
    AWS then persists the instance's Amazon EBS root volume and any attached Amazon EBS data volumes.

## Amazon Machine Image (AMI)

    Amazon Machine Image (AMI) provides the information required to launch an instance. You must specify an AMI when you launch an instance.
    Creating an AMI may help with all the system dependencies, but it won't help us with speeding up the application start time.
    You can copy an AMI within or across AWS Regions using the AWS Management Console.
    You can share an AMI with another AWS account. 
    
     AMIs are bound to the Region they are created in. So, you need to copy the AMI across Regions for disaster recovery readiness.

## launch template

    launch templates, you can provision capacity across multiple instance types using both On-Demand Instances and Spot Instances to achieve the desired scale, performance, and cost.
    A launch template is similar to a launch configuration, in that it specifies instance configuration information such as the ID of the Amazon Machine Image (AMI), the instance type, 
    a key pair, security groups, and the other parameters that you use to launch EC2 instances

## launch configuration

    A launch configuration is an instance configuration template that an Auto Scaling group uses to launch EC2 instances
    When you create a launch configuration, you specify information for the instances such as the ID of the Amazon Machine Image (AMI), 
    the instance type, a key pair, one or more security groups, and a block device mapping.

## Recovery:

    Terminated instances cannot be recovered.
    A recovered instance is identical to the original instance, including the instance ID, private IP addresses, Elastic IP addresses, and all instance metadata
    If your instance has a public IPv4 address, it retains the public IPv4 address after recovery.
    If the impaired instance is in a placement group, the recovered instance runs in the placement group. 
    During instance recovery, the instance is migrated during an instance reboot, and any data that is in-memory is lost.

## connection draining:

    This enables the load balancer to complete in-flight requests made to instances that are de-registering or unhealthy.
    The maximum timeout value can be set between 1 and 3,600 seconds.
    When the maximum time limit is reached, the load balancer forcibly closes connections to the de-registering instance.

# Gateway Endpoints

# Farget

    Amazon Elastic Container Service (Amazon ECS) is a fully managed container orchestration service. 
    ECS allows you to easily run, scale, and secure Docker container applications on AWS.
    With the Fargate launch type, you pay for the amount of vCPU and memory resources that your containerized application requests. 
    vCPU and memory resources are calculated from the time your container images are pulled until the Amazon ECS Task terminates, rounded up to the nearest second

# IAM

## IAM permission boundary

    AWS supports permissions boundaries for IAM entities (users or roles). 
    A permissions boundary is an advanced feature for using a managed policy to set the maximum permissions that an identity-based policy can grant to an IAM entitY.

## AWS Organizations Service Control Policies (SCP): Limit permisiion

    Service control policy (SCP) offers central control over the maximum available permissions for all accounts in your organization
     
    Service control policy (SCP) does not affect any service-linked role.

    In service control policy (SCP), you can restrict which AWS services, resources, and individual API actions the users and roles in each member account can access

    Service control policies (SCPs) are a type of organization policy that you can use to manage permissions in your organization
    The SCP limits permissions for entities in member accounts, including each AWS account root user. 
    An explicit deny in any of these policies overrides the allow.

# Route53

## geolocation routing policy

    Geolocation routing lets you choose the resources that serve your traffic based on the geographic location of your users, 
    meaning the location that DNS queries originate from

# Kinensis

## Amazon Kinesis Data Firehose (KDF) :  Ingesting and delivering logs, metric , ETL

    Amazon Kinesis Data Firehose is the easiest way to load streaming data into data stores and analytics tools. 
    It is a fully managed service that automatically scales to match the throughput of your data and requires no ongoing administration.
    It can capture, transform, and load streaming data into Amazon S3, Amazon Redshift, 
    Amazon OpenSearch Service, and Splunk, enabling near real-time analytics with existing business intelligence tools and dashboards you’re already using today. 
    Firehose cannot directly write into a DynamoDB table

## Amazon Kinesis Data Analytics (KDA): transform and analyze incoming streaming data

    Kinesis Data Analytics enables you to easily and quickly build queries and sophisticated streaming applications in three simple steps: 
    1) setup your streaming data sources, 
    2)write your queries or streaming applications, 
    3)and set up your destination for processed data. 
    Kinesis Data Analytics cannot directly ingest data from the source as it ingests data either from Kinesis Data Streams or Kinesis Data Firehose

## Amazon Kinesis Data Streams (KDS): anomaly detection or log monitoring.(shared)

    (KDS) is a massively scalable,highly durable data ingestion and processing service optimized for streaming data. 
     KDS  is integrated with a number of AWS services  including Amazon Kinesis Data Firehose for near real-time transformation.
    KDS cannot directly write the output to Amazon S3. Unlike KDF, KDS does not offer a ready-made integration via an intermediary AWS Lambda function to reliably dump data into Amazon S3.
    KDS makes sure your streaming data is available to multiple real-time analytics applications, to Amazon S3, or AWS Lambda within 70 milliseconds of the data being collected. 

    Amazon Kinesis Data Streams is recommended when you need the ability to consume records in the same order a few hours later.
    For example, you have a billing application and an audit application that runs a few hours behind the billing application. 
    Because Amazon Kinesis Data Streams stores data for a maximum of 365 days, you can easily run the audit application up to 7 days behind the billing application.

## Kinesis Agent

    Kinesis Agent is a stand-alone Java software application that offers an easy way to collect and send data to Amazon Kinesis Data Streams or Amazon Kinesis Firehose.
    Kinesis Agent cannot write to Amazon Kinesis Firehose for which the delivery stream source is already set as Amazon Kinesis Data Streams

# Amazon EMR

    Amazon EMR is the industry-leading cloud big data platform for processing vast amounts of data using open source tools 
    such as Apache Spark, Apache Hive, Apache HBase, Apache Flink, Apache Hudi, and Presto
    Amazon EMR uses Hadoop, an open-source framework, to distribute your data and processing across a resizable cluster of Amazon EC2 instances
    Using an EMR cluster would imply managing the underlying infrastructure

# Amazon RDS

## Multi AZ RDS: synchronously replicates

    When you provision a Multi-AZ DB Instance, Amazon RDS automatically creates a primary DB Instance and synchronously replicates the data to a standby 
    instance in a different Availability Zone (AZ). Multi-AZ spans at least two Availability Zones (AZs) within a single region.
    
    Amazon RDS Read Replicas provide enhanced performance and durability for RDS database (DB) instances.
    Amazon RDS creates a second DB instance using a snapshot of the source DB instance. 
    It then uses the engines' native asynchronous replication to update the read replica whenever there is a change to the source DB instance.

## Amazon RDS Custom

    Amazon RDS Custom for Oracle as it allows you to access and customize your database server host and operating system
    Amazon RDS Custom for Oracle facilitates these functionalities with minimum infrastructure maintenance effort. 
    You need to set up the RDS Custom for Oracle in multi-AZ configuration for high availability.

## RDS read replica charges

    You are not charged for the data transfer, in replicating data between your source DB instance and read replica within the same AWS Region.

## RDS Encription

    You can only enable encryption for an Amazon RDS DB instance when you create it, not after the DB instance is created
    You can encrypt your Amazon RDS DB instances and snapshots at rest by enabling the encryption option for your Amazon RDS DB instances
    create a snapshot of your DB instance, and then create an encrypted copy of that snapshot.

## AWS Database Migration Service (AWS DMS)

    AWS Database Migration Service helps you migrate databases to AWS quickly and securely. 
    The source database remains fully operational during the migration, minimizing downtime to applications that rely on the database. 
    AWS Database Migration Service supports homogeneous migrations such as Oracle to Oracle, 
    as well as heterogeneous migrations between different database platforms, such as Oracle or Microsoft SQL Server to Amazon Aurora.

    AWS DMS supports specifying Amazon S3 as the source and streaming services like Kinesis and Amazon Managed Streaming of Kafka (Amazon MSK) as the target

## AWS Schema Conversion Tool (AWS SCT)

    The AWS Schema Conversion Tool (AWS SCT) is a utility provided by Amazon Web Services to help organizations migrate their database schemas from one database engine to another. 
    It is specifically designed to simplify the process of migrating between heterogeneous database systems, such as from Oracle to Amazon Aurora, 
    or SQL Server to Amazon RDS for PostgreSQL.
    That makes heterogeneous migrations a two-step process. 
        1) First use the AWS Schema Conversion Tool to convert the source schema and code to match that of the target database, 
        2) then use the AWS Database Migration Service to migrate data from the source database to the target database

# Amazon Redshift

    Amazon Redshift is a fully managed, petabyte-scale data warehouse service provided by AWS. 
    It is designed for high-performance analytics and querying, enabling businesses to process and analyze vast amounts of structured and semi-structured data quickly

# AWS Cost Explorer Resource

    AWS Cost Explorer helps you identify under-utilized Amazon EC2 instances that may be downsized on an instance by instance basis within the same instance family.
    and also understand the potential impact on your AWS bill by taking into account your Reserved Instances and Savings Plans.

# AWS Compute Optimizer

    recommends optimal AWS Compute resources for your workloads to reduce costs and improve performance by using machine learning to analyze historical utilization metrics.
     Compute Optimizer helps you choose the optimal Amazon EC2 instance types,

# AWS Trusted Advisor

    AWS Trusted Advisor checks for Amazon EC2 Reserved Instances that are scheduled to expire within the next 30 days or have expired in the preceding 30 days. 

# DynamoDB: (PITR)

    Amazon DynamoDB enables you to back up your table data continuously by using point-in-time recovery (PITR).
    DynamoDB backs up your table data automatically with per-second granularity so that you can restore to any given second in the preceding 35 days.
    PITR helps protect you against accidental writes and deletes

## Amazon DynamoDB global tables : Across AWS regions

    DynamoDB global tables provide cross-region active-active capabilities with high performance, but you lose some of the data access flexibility that comes with SQL-based databases.
    
    The active-active configuration of DynamoDB global tables, there is no concept of failover because the application writes to the table in its region, 
    and then the data is replicated to keep the other regions' table in sync.
    
    DynamoDB global tables is a much costlier solution than Aurora Global Database

## DynamoDB Accelerator(DAX)

    DAX is a DynamoDB-compatible caching service that enables you to benefit from fast in-memory performance for demanding applications. 
    So DynamoDB with DAX can be used to power the live leaderboard.
    
    Amazon DynamoDB Accelerator (DAX) is a fully managed, highly available, in-memory cache for DynamoDB that delivers up to a 10x performance 
    improvement – from milliseconds to microseconds

## DynamoDB table in the on-demand capacity mode

    Amazon DynamoDB has two read/write capacity modes for processing reads and writes 
        1)On-demand: Amazon DynamoDB on-demand is a flexible billing option capable of serving thousands of requests per second without capacity planning.
             DynamoDB on-demand offers pay-per-request pricing for read and write requests so that you pay only for what you use.
        2)Provisioned (default, free-tier eligible):
             good option for predictable application traffic.
             applications whose traffic is consistent or ramps gradually.
            forecast capacity requirements to control costs.

## Amazon DynamoDB Streams

    Amazon DynamoDB stream is an ordered flow of information about changes to items in Amazon DynamoDB table. 
    When you enable a stream on a table, DynamoDB captures information about every modification to data items in the table. 
    Amazon DynamoDB Streams will contain a stream of all the changes that happen to an Amazon DynamoDB table

# Amazon ElastiCache: Improve read-heavy application and compute-intensive workloads

    Amazon ElastiCache for Redis is a blazing fast in-memory data store that provides sub-millisecond latency to power internet-scale real-time applications. 
    Amazon ElastiCache for Redis is a great choice for real-time transactional and analytical processing use cases such as caching,chat/messaging, gaming 
    leaderboards, geospatial, machine learning, media streaming, queues, real-time analytics, and session store.
    Elasticache is used as a caching layer in front of relational databases. It is not a good fit to store data in key-value pairs from the IoT sources.

# Internet Gateway ID

    An Internet Gateway ID in AWS is the unique identifier assigned to an Internet Gateway resource when it is created in a Virtual Private Cloud (VPC).
    An Internet Gateway serves two purposes: 
        1)  to provide a target in your VPC route tables for internet-routable traffic and to perform network address translation (NAT) for instances that have been assigned public IPv4 addresses.
        2)  an Internet Gateway supports IPv4 and IPv6 traffic. It does not cause availability risks or bandwidth constraints on your network traffic.

## EFS performance

    Max I/O performance mode is used to scale to higher levels of aggregate throughput and operations per second.

## Amazon EFS Infrequent Access (EFS IA)

    Amazon EFS Infrequent Access (EFS IA) is a storage class that provides price/performance that is cost-optimized for files, 
    not accessed every day, with storage prices up to 92% lower compared to Amazon EFS Standard

# AWS Web Application Firewall (AWS WAF)

    AWS Web Application Firewall (AWS WAF) is a web application firewall service that lets you monitor web requests and protect your web applications from malicious requests
    Use AWS WAF to block or allow requests based on conditions that you specify, such as the IP addresses. 
    You can also use AWS WAF preconfigured protections to block common attacks like SQL injection or cross-site scripting.
    Geographic (Geo) Match Conditions in AWS WAF allows you to use AWS WAF to restrict application access based on the geographic location of your viewers.
    geo match conditions you can choose the countries from which AWS WAF should allow access.
    Geo match conditions are important for many customers. For example, legal and licensing requirements restrict some customers from delivering their 
    applications outside certain countries. 
    These customers can configure a whitelist that allows only viewers in those countries.
    Geo Restriction feature of Amazon CloudFront helps in restricting traffic based on the user's geographic location.  
    But, CloudFront works from edge locations and doesn't belong to a VPC.

# VPC

    An AWS VPC (Virtual Private Cloud) is a logically isolated section of the AWS cloud where you can launch and manage AWS resources in a virtual network that you define

## AWS Resource Access Manager (RAM)

    AWS Resource Access Manager (RAM) is a service that enables you to easily and securely share AWS resources with any AWS account or within your AWS Organization

## VPC Peering Connection

    A VPC peering connection is a networking connection between two VPCs ,that enables you to route traffic between them using private IPv4 addresses or IPv6 addresses.
    Instances in either VPC can communicate with each other as if they are within the same network.
    You can create a VPC peering connection between your VPCs, or with a VPC in another AWS account.

## AWS Transit Gateway : hub

    Transit Gateway acts as a hub that controls how traffic is routed among all the connected networks which act like spokes.
    AWS Transit Gateway is a service that enables customers to connect their Amazon Virtual Private Clouds (VPCs) and their on-premises networks to a single gateway. 
    With AWS Transit Gateway, you only have to create and manage a single connection from the central gateway into each Amazon VPC, 
    on-premises data center, or remote office across your network.

## Virtual private gateway (VGW)

    A virtual private gateway (VGW), also known as a VPN Gateway, is the endpoint on the VPC side of your VPN connection

## AWS PrivateLink

    AWS PrivateLink simplifies the security of data shared with cloud-based applications by eliminating the exposure of data to the public Internet
    AWS PrivateLink provides private connectivity between VPCs, AWS services, and on-premises applications, securely on the Amazon network.

## AWS VPN CloudHub

    AWS VPN CloudHub is a feature of AWS that allows you to connect multiple remote sites (branch offices) securely to a central Amazon Virtual Private Cloud (VPC) using VPN connections. 
    It acts as a hub-and-spoke model for connectivity, where each remote site connects to AWS and can communicate with other remote sites through the hub.

## VPC sharing : Sharing vpc resource with subnet

    VPC sharing (part of Resource Access Manager) allows multiple AWS accounts to create their application resources such as Amazon EC2 instances, 
    Amazon RDS databases, Amazon Redshift clusters, and AWS Lambda functions, into shared and centrally-managed Amazon Virtual Private Clouds (VPCs). 
    account that owns the VPC (owner) shares one or more subnets with other accounts (participants) that belong to the same organization from AWS Organizations.
    After a subnet is shared, the participants can view, create, modify, and delete their application resources in the subnets shared with them

## VPC Endpoint

    A VPC endpoint enables you to privately connect your VPC to supported AWS services and VPC endpoint services powered by AWS PrivateLink without requiring an internet gateway.
    There are two types of VPC endpoints:
    1) Interface Endpoints . An Interface Endpoint is an Elastic Network Interface with a private IP address from the IP address range of your subnet that serves as an entry point 
                            for traffic destined to a supported service.
                            This support other than  S3 and DynamoDb
    2) Gateway Endpoints: A Gateway Endpoint is a gateway that you specify as a target for a route in your route table for traffic destined to a supported AWS service.
                            It support only two services S3 and DynamoDb

# Amazon MQ

    Amazon MQ is a managed message broker service for Apache ActiveMQ that makes it easy to set up and operate message brokers in the cloud.
    Supports popular messaging protocols like JMS, NMS, AMQP, MQTT, OpenWire, and STOMP.
    
    Amazon SNS, Amazon SQS, and Amazon Kinesis are AWS's proprietary technologies and do not come with MQTT compatibility.

# VPN

## VPN connection: A secure connection between your on-premises equipment and your VPCs.

## VPN tunnel: An encrypted link where data can pass from the customer network to or from AWS.

## Customer Gateway: An AWS resource that provides information to AWS about your Customer Gateway device.

## Customer Gateway device: A physical device or software application on the customer side of the Site-to-Site VPN connection.

## AWS Site-to-Site VPN

    AWS Site-to-Site VPN enables you to securely connect your on-premises network or branch office site to your Amazon Virtual Private Cloud (Amazon VPC)
    You can securely extend your data center or branch office network to the cloud with an AWS Site-to-Site VPN connection

# AWS Direct Connect

    AWS Direct Connect is a cloud service solution that makes it easy to establish a dedicated network connection from your premises to AWS. 
    With AWS Direct Connect plus VPN, you can combine one or more AWS Direct Connect dedicated network connections with the Amazon VPC VPN. 
    This combination provides an IPsec-encrypted private connection that also reduces network costs, increases bandwidth throughput, 
    and provides a more consistent network experience than internet-based VPN connections.
    
     This is a physical connection that takes at least a month to set up.

## AWS Managed Microsoft AD : SSO, SQL Server

    With AWS Managed Microsoft AD, you can run directory-aware workloads in the AWS Cloud such as SQL Server-based applications.
    You can also configure a trust relationship between AWS Managed Microsoft AD in the AWS Cloud and your existing on-premises Microsoft Active Directory,
    providing users and groups with access to resources in either domain, using single sign-on (SSO).

## Active Directory Connector: SSO

    Use AD Connector if you only need to allow your on-premises users to log in to AWS applications and services with their Active Directory credentials.
    AD Connector simply connects your existing on-premises Active Directory to AWS

## Amazon Cloud Directory

    Amazon Cloud Directory is a cloud-native directory that can store hundreds of millions of application-specific objects with multiple relationships and schemas.
    You cannot use it to establish trust relationships with other domains on the on-premises infrastructure

## Simple Active Directory (Simple AD) :Subset of AWS Microsoft AD

    Simple AD provides a subset of the features offered by AWS Managed Microsoft AD
    Simple AD does not support features such as trust relationships with other domains. 

## Amazon FSx File Gateway

    Amazon FSx File Gateway provides low-latency, on-premises access to fully managed file shares in Amazon FSx for Windows File Server.
     For applications deployed on AWS, you may access your file shares directly from Amazon FSx in AWS
    Amazon FSx for Windows File Server provides all of the benefits of a native Windows SMB(Server Message Block) environment that is 
    fully managed and secured and scaled like any other AWS service.
    You get detailed reporting, replication, backup, failover, and support for native Windows tools like DFS and Active Directory.
    Amazon FSx for Windows File Server and it does not support EFS

## Amazon FSx for Lustre

    Amazon FSx for Lustre makes it easy and cost-effective to launch and run the world’s most popular high-performance file system. 
    It is used for workloads such as machine learning, high-performance computing (HPC), video processing, and financial modeling.
    The open-source Lustre file system is designed for applications that require fast storage – 
    where you want your storage to keep up with your compute. FSx for Lustre integrates with Amazon S3,

## Amazon FSx for Windows File Server : SMB Protocol, Microsoft Active Directory (AD) integration

    Amazon FSx for Windows File Server provides fully managed, highly reliable file storage that is accessible over the industry-standard Service Message Block (SMB) protocol. 
    It is built on Windows Server, delivering a wide range of administrative features such as user quotas, end-user file restore, and Microsoft Active Directory (AD) integration.
    Amazon FSx supports the use of Microsoft’s Distributed File System (DFS) to organize shares into a single folder structure up to hundreds of PB in size

# Amazon GuardDuty :  malicious activity

    Amazon GuardDuty is a threat detection service that continuously monitors for malicious activity and unauthorized behavior to protect your AWS accounts, 
    workloads, and data stored in Amazon S3. With the cloud, the collection and aggregation of account and network activities is simplified, 
    but it can be time-consuming for security teams to continuously analyze event log data for potential threats.
    Amazon GuardDuty analyzes tens of billions of events across multiple AWS data sources, such as AWS CloudTrail events, Amazon VPC Flow Logs, and DNS logs.

# Amazon Macie :  sensitive data

    Amazon Macie is a fully managed data security and data privacy service that uses machine learning and pattern matching to discover and protect your sensitive data on Amazon S3.
    Macie automatically detects a large and growing list of sensitive data types, including personally identifiable information (PII) such as names, addresses, and credit card numbers. 

# AWS Storage Gateway

    AWS Storage Gateway is a hybrid cloud storage service that gives you on-premises access to virtually unlimited cloud storage
    The service provides three different types of gateways – Tape Gateway, File Gateway, and Volume Gateway – 
    that seamlessly connect on-premises applications to cloud storage, caching data locally for low-latency access.
    
    1) AWS Storage Gateway's file interface, or file gateway, 
        offers you a seamless way to connect to the cloud in order to store application data files and backup images as durable objects on Amazon S3 cloud storage
        File gateway offers SMB(Server Message Block) or NFS-based access to data in Amazon S3 with local caching
    2) AWS Storage Gateway service as a Volume Gateway
        AWS Storage Gateway service as a Volume Gateway to present cloud-based iSCSI block storage volumes to your on-premises applications.
    3) AWS Storage Gateway - Tape Gateway
        AWS Storage Gateway - Tape Gateway allows moving tape backups to the cloud
        Tape Gateway enables you to replace using physical tapes on-premises with virtual tapes in AWS without changing existing backup workflows. 

# AWS Global Accelerator

    AWS Global Accelerator utilizes the Amazon global network, allowing you to improve the performance of your applications by 
    lowering first-byte latency (the round trip time for a packet to go from a client to your endpoint and back again) and 
    jitter (the variation of latency), and increasing throughput (the amount of time it takes to transfer data) as compared to the public internet

    AWS Global Accelerator improves performance for a wide range of applications over TCP or UDP by proxying packets at the edge to applications running in one or more AWS Regions
    
    It provides static IP addresses that provide a fixed entry point to your applications and eliminate the complexity 
    of managing specific IP addresses for different AWS Regions and Availability Zones.

# Network ACLs (NACL) VS Security Group

    Security groups are stateful, so allowing inbound traffic to the necessary ports enables the connection.
    Network ACLs are stateless, so you must allow both inbound and outbound traffic.

# Aurora

    Amazon Aurora is a MySQL and PostgreSQL-compatible relational database built for the cloud.
    Amazon Aurora is up to five times faster than standard MySQL databases and three times faster than standard PostgreSQL databases.

## Amazon Aurora Serverless

    Amazon Aurora Serverless is an on-demand, auto-scaling configuration for Amazon Aurora (MySQL-compatible and PostgreSQL-compatible editions), 
    where the database will automatically start-up, shut down, and scale capacity up or down based on your application's needs.
     It's a simple, cost-effective option for infrequent, intermittent, or unpredictable workloads

## Amazon Aurora Global Database

    Amazon Aurora Global Database is designed for globally distributed applications, allowing a single Amazon Aurora database to span multiple AWS regions.
    It replicates your data with no impact on database performance, enables fast local reads with low latency in each region, and provides disaster recovery from region-wide outages

## Aurora Replicas

    Amazon Aurora Replicas have two main purposes. 
    1) You can issue queries to them to scale the read operations for your application. 
    You typically do so by connecting to the reader endpoint of the cluster. 
    That way, Aurora can spread the load for read-only connections across as many Aurora Replicas as you have in the cluster
    2) Amazon Aurora Replicas also help to increase availability. If the writer instance in a cluster becomes unavailable, 
    Aurora automatically promotes one of the reader instances to take its place as the new writer. 
    Up to 15 Aurora Replicas can be distributed across the Availability Zones (AZs) that a DB cluster spans within an AWS Region.

    If two or more Aurora Replicas share the same priority, then Amazon RDS promotes the replica that is largest in size
    If two or more Aurora Replicas share the same priority and size, then Amazon Aurora promotes an arbitrary replica in the same promotion tier.

# Amazon Neptune :social networking, relation,high-performance graph database

    Amazon Neptune is a fast, reliable, fully-managed graph database service that makes it easy to build and run applications that work with highly connected datasets. 
    
    The core of Amazon Neptune is a purpose-built, high-performance graph database engine optimized for storing billions of relationships and querying the graph with milliseconds latency.
    
    Amazon Neptune is highly available, with read replicas, point-in-time recovery, continuous backup to Amazon S3, and replication across Availability Zones.
    
    Amazon Neptune can quickly and easily process large sets of user-profiles and interactions to build social networking applications

# CloudFront

    Amazon CloudFront is a fast content delivery network (CDN) service that securely delivers data, videos, applications, 
    and APIs to customers globally with low latency, high transfer speeds,all within a developer-friendly environment
    
    CloudFront points of presence (POPs) (edge locations) make sure that popular content can be served quickly to your viewers.
    
    Amazon CloudFront also has regional edge caches that bring more of your content closer to your viewers, 
    even when the content is not popular enough to stay at a POP, to help improve performance for that content.

    Amazon CloudFront provides two ways to send authenticated requests to an Amazon S3 origin: 
     1)origin access control (OAC) and
     2)origin access identity (OAI).
    
    Please note that AWS recommends using OAC because it supports: 
        All Amazon S3 buckets in all AWS Regions
        Amazon S3 server-side encryption with AWS KMS (SSE-KMS)

# Amazon EventBridge

    Amazon EventBridge is recommended when you want to build an application that reacts to events from SaaS applications and/or AWS services.
    Amazon EventBridge is the only event-based service that integrates directly with third-party SaaS partners
        Example: EventBridge enables out-of-the-box integration with SaaS providers, such as Zendesk, Datadog, Stripe, Auth0, Okta, and more.

    Amazon EventBridge also automatically ingests events from over 90 AWS services without requiring developers to create any resources in their account.

# AWS Shield

    AWS Shield is a managed Distributed Denial of Service (DDoS) protection service that safeguards applications running on AWS.
    AWS Shield provides always-on detection and automatic inline mitigations that minimize application downtime and latency.
    AWS Shield cannot be used to improve application resiliency to handle spikes in traffic.

## AWS Shield - Standard

## AWS Shield - Advanced

# AWS Global Accelerator

    AWS Global Accelerator is a service that improves the availability and performance of your applications with local or global users. 
    It provides static IP addresses that act as a fixed entry point to your application endpoints in a single or multiple AWS Regions, 
    such as your Application Load Balancers, Network Load Balancers or Amazon EC2 instances.
    
    Amazon Global Accelerator is a good fit for non-HTTP use cases, such as gaming (UDP), IoT (MQTT), or Voice over IP, 
    as well as for HTTP use cases that specifically require static IP addresses or deterministic, fast regional failover.

# AWS Direct Connect

    AWS Direct Connect lets you establish a dedicated network connection between your network and one of the AWS Direct Connect locations
    Using industry-standard 802.1q VLANs, this dedicated connection can be partitioned into multiple virtual interfaces. 
    
    AWS Direct Connect does not involve the Internet; instead, it uses dedicated, private network connections between your intranet and Amazon VPC. 

# AWS API Gateway

    Are HTTP-based.
    Enable stateless client-server communication.
    Amazon API Gateway creates WebSocket APIs that: WebSocket protocol, which enables stateful, full-duplex communication between client and server. 
    Route incoming messages based on message content.
    Amazon API Gateway supports stateless RESTful APIs as well as stateful WebSocket APIs.

## CNAME

    A CNAME (Canonical Name) record is a type of DNS (Domain Name System) record used to map an alias domain name to another domain name, which is the canonical (true or primary) name. 
    This allows multiple domain names to point to the same resource.
    
    A CNAME record can redirect DNS queries to any DNS record. For example, 
    you can create a CNAME record that redirects queries from acme.example.com to zenith.example.com or to acme.example.org. 
    
    A hostname is not case-sensitive, can be up to 128 characters in length, and can contain any of the following characters: 
    1. A–Z, a–z, 0–9 
    2. - . 
    3. * (matches 0 or more characters) 
    4. ? (matches exactly 1 character)

## The Time To Live (TTL)

    TTL (time to live), is the amount of time, in seconds, that you want DNS recursive resolvers to cache information about a record

## alias record

## Route 53

    Route 53 doesn't charge for alias queries to AWS resources but Route 53 does charge for CNAME queries
    By default, Amazon Route 53 Resolver automatically answers DNS queries for local VPC domain names for Amazon EC2 instances
    
    Amazon Route 53 to configure DNS health checks to route traffic to healthy endpoints

# Amazon Cognito User Pools

    A user pool is a user directory in Amazon Cognito. You can leverage Amazon Cognito User Pools to either provide built-in user management or 
    integrate with external identity providers, such as Facebook, Twitter, Google+, and Amazon.
    User pools provide: 
        1. Sign-up and sign-in services. 
        2. A built-in, customizable web UI to sign in users. 
        3. Social sign-in with Facebook, Google, Login with Amazon, and Sign in with Apple, as well as sign-in with SAML identity providers from your user pool. 
        4. User directory management and user profiles. 
        5. Security features such as multi-factor authentication (MFA), checks for compromised credentials, account takeover protection, and phone and email verification. 
        6. Customized workflows and user migration through AWS Lambda triggers.

# AWS DataSync:

    AWS DataSync is an online data transfer service that simplifies, automates, 
    and accelerates copying large amounts of data to and from AWS storage services over the internet or AWS Direct Connect.

    AWS DataSync fully automates and accelerates moving large active datasets to AWS, up to 10 times faster than command-line tools. 
    It is natively integrated with Amazon S3, Amazon EFS, Amazon FSx for Windows File Server, Amazon CloudWatch, and AWS CloudTrail, 
    which provides seamless and secure access to your storage services, as well as detailed monitoring of the transfer.

# AWS Snowball

    WS Snowball is a data migration and edge computing service offered by Amazon Web Services (AWS). 
    It helps move large amounts of data between on-premises locations and AWS, either for initial cloud migration, disaster recovery, or as part of hybrid cloud workflows.
    Snowball devices are physically shipped to your location, allowing you to transfer data without relying on slow or costly network connections.

## SnowCone

    AWS Snowcone is the smallest member of the AWS Snow Family, designed for edge computing, data migration, and storage. 
    It is a lightweight, portable, and rugged device ideal for environments with limited space, power, or connectivity.

## AWS Snowmobile

    AWS Snowmobile is an extremely high-capacity data transfer service designed by Amazon Web Services (AWS) to help 
    usinesses move large volumes of data to the cloud in a fast and secure manner. 
    
    AWS Snowmobile moves up to 100 PB of data in a 45-foot long ruggedized shipping container and 
    is ideal for multi-petabyte or Exabyte-scale digital media migrations and data centers shutdowns.

## AWS Snowball Edge Compute

    AWS Snowball is a data migration and edge computing device that comes in two device options: 
     1) Compute Optimized : Snowball Edge Compute Optimized devices provide 52 vCPUs, 42 terabytes of usable block or object storage, 
                            and an optional GPU for use cases such as advanced machine learning and full-motion video analysis in disconnected environments.
                            Use FOR ML and AI

     2) Storage Optimized: AWS Snowball Edge Storage Optimized devices provide 40 vCPUs of compute capacity coupled with 80 terabytes of usable block or Amazon S3-compatible object storage.

# Cloud Formation Template

## CloudFormation StackSet

    AWS CloudFormation StackSet extends the functionality of stacks by enabling you to create, update, or delete stacks across multiple accounts and regions with a single operation.
    A stack set lets you create stacks in AWS accounts across regions by using a single AWS CloudFormation template. 

## AWS Config

    AWS Config is a fully managed service provided by Amazon Web Services (AWS) that enables you to assess, audit, and evaluate the configurations of your AWS resources. 
    It helps you ensure compliance with internal policies and regulatory requirements by continuously monitoring resource configurations and changes over time.

# AWS Systems Manager

    AWS Systems Manager is a comprehensive management service that enables you to manage and automate your AWS infrastructure and resources securely. 
    It provides a unified interface for operational tasks such as patch management, configuration compliance, resource monitoring, and automation of repetitive tasks.

# AWS Network

## Elastic Fabric Adapter (EFA)

    An Elastic Fabric Adapter (EFA) is a network device that you can attach to your Amazon EC2 instance to accelerate High Performance Computing (HPC) and machine learning applications.
    It enhances the performance of inter-instance communication that is critical for scaling HPC and machine learning applications.
    
    EFA devices provide all Elastic Network Adapter (ENA) devices functionalities plus a new OS bypass hardware interface that allows user-space applications 
    to communicate directly with the hardware-provided reliable transport functionality.

## Elastic Network Interface (ENI)

     An Elastic Network Interface (ENI) is a logical networking component in a VPC that represents a virtual network card. 

    You can create a network interface, attach it to an instance, detach it from an instance, and attach it to another instance. 

## Elastic Network Adapter (ENA)

    Elastic Network Adapter (ENA) devices support enhanced networking via single root I/O virtualization (SR-IOV) to provide high-performance networking capabilities. 

## Elastic IP Address (EIP)

    An Elastic IP address (EIP) is a static IPv4 address associated with your AWS account. An Elastic IP address is a public IPv4 address, which is reachable from the internet. 

# Disaster Recovery (DR) strategies

    1) Backup and Restore : Data and application backups are taken periodically and stored in Amazon S3 or Amazon Glacier. 
                            During a disaster, backups are restored to bring systems back online.
                            it has an RPO in hours
    2) Pilot Light        : A minimal version of your environment (key components) runs in AWS. 
                            In a disaster, you "scale up" this environment to full production.
                             For Pilot light, RPO/RTO is in 10s of minutes

    3) Warm Standby       : A scaled-down version of the fully functional environment is always running in AWS. 
                            It can quickly scale up to production capacity when needed.
    4) Multi-Site Active/Active: The application runs fully active in two or more regions simultaneously. 
                            Traffic is distributed using DNS or load balancers. In case of failure in one region, the other region automatically takes over with no downtime.

# Aws Glue

    AWS Glue is a fully managed extract, transform, and load (ETL) service that makes it easy for customers to prepare and load their data for analytics. 
    AWS Glue job is meant to be used for batch ETL data processing. Glue is for performing ETL, but cannot run custom shell scripts and hence not the right choice here.

# Concept

    You may see scenario-based questions asking you to select one of Amazon CloudWatch vs AWS CloudTrail vs AWS Config. Just remember this thumb rule -

    Think resource performance monitoring, events, and alerts; think Amazon CloudWatch.

    Think account-specific activity and audit; think AWS CloudTrail.

    Think resource-specific history, audit, and compliance; think AWS Config.