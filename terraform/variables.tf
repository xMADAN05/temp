variable "aws_region" {
  description = "AWS region for the resources"
  type        = string
  default     = "us-west-2"
}

variable "dynamodb_table_name" {
  description = "Name of the DynamoDB table"
  type        = string
  default     = "feedback"
}

variable "dynamodb_hash_key" {
  description = "Hash key for the DynamoDB table"
  type        = string
  default     = "id"
}

variable "dynamodb_table_class" {
  description = "Storage class for the DynamoDB table"
  type        = string
  default     = "STANDARD"
}

variable "dynamodb_billing_mode" {
  description = "Billing mode for the DynamoDB table"
  type        = string
  default     = "PROVISIONED"
}

variable "dynamodb_read_capacity" {
  description = "Provisioned read capacity units for the DynamoDB table"
  type        = number
  default     = 5
}

variable "dynamodb_write_capacity" {
  description = "Provisioned write capacity units for the DynamoDB table"
  type        = number
  default     = 5
}

variable "environment" {
  description = "Deployment environment (e.g., dev, staging, prod)"
  type        = string
  default     = "dev"
}

variable "project_name" {
  description = "Name of the project"
  type        = string
  default     = "feedback-system"
}

# variable "owner" {
#   description = "Owner of the resource (team or individual)"
#   type        = string
#   default     = ""
# }
