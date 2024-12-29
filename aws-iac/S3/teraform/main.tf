provider "aws" {
  region = "us-east-1"  # Change to your desired region
}

# Create the S3 bucket
resource "aws_s3_bucket" "my_bucket" {
  bucket = "rama-bucket-001"  # Replace with a globally unique bucket name
}

# Create IAM role
resource "aws_iam_role" "s3_role" {
  name = "S3AccessRole"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "ec2.amazonaws.com"  # Change this to the service you need (e.g., lambda.amazonaws.com)
        }
      }
    ]
  })
}

# Create IAM policy for S3 access
resource "aws_iam_policy" "s3_policy" {
  name        = "S3AccessPolicy"
  description = "A policy to allow access to the S3 bucket"
  policy      = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect   = "Allow"
        Action   = ["s3:GetObject", "s3:PutObject", "s3:DeleteObject"]
        Resource = "${aws_s3_bucket.my_bucket.arn}/*"
      }
    ]
  })
}

# Attach the IAM policy to the IAM role
resource "aws_iam_role_policy_attachment" "role_policy_attachment" {
  policy_arn = aws_iam_policy.s3_policy.arn
  role       = aws_iam_role.s3_role.name
}

# Output the bucket name
output "bucket_name" {
  value = aws_s3_bucket.my_bucket.bucket
}
