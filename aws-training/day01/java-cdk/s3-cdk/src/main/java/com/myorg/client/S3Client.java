package com.myorg.client;

import com.amazonaws.services.s3.AmazonS3;
import com.amazonaws.services.s3.AmazonS3ClientBuilder;
import com.amazonaws.services.s3.model.Bucket;

import java.util.List;

public class S3Client {
    public static void main(String[] args) {
        AmazonS3 s3client = AmazonS3ClientBuilder
                .standard()
                .build();

        List<Bucket> buckets = s3client.listBuckets();
        for(Bucket bucket : buckets) {
            System.out.println(bucket.getName());
        }


    }
}
