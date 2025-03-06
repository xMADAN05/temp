provider "aws"{
    region = var.aws_region
}


resource "aws_dynamodb_table" "feedback_table" {
  name = var.dynamodb_table_name
  hash_key = var.dynamodb_hash_key
  table_class = var.dynamodb_table_class
  billing_mode = var.dynamodb_billing_mode
  read_capacity = var.dynamodb_read_capacity
  write_capacity = var.dynamodb_write_capacity

    attribute {
      name = var.dynamodb_hash_key
      type = "S"
    }

    tags = {
      Name = var.dynamodb_table_name
      Environment = var.environment
      Project = var.project_name
      # Owner = var.owner
      Service = "feedback"
      terraform = "true"
    }

  


}