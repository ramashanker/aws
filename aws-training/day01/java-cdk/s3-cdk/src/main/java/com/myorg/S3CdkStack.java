package com.myorg;
import software.amazon.awscdk.*;
import software.amazon.awscdk.services.s3.Bucket;

public class S3CdkStack extends Stack {
    public S3CdkStack(final App scope, final String id) {
        this(scope, id, null);
    }

    public S3CdkStack(final App scope, final String id, final StackProps props) {
        super(scope, id, props);

        Bucket.Builder.create(this, "MyFirstBucket-001")
                .versioned(true).build();
    }
}
