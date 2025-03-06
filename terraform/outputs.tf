output "dynamodb_table_name" {
    description = "Name of created DynamoDB table"
    value = aws_dynamodb_table.feedback_table.name
}

output "dynamodb_table_arn"{
    description = "value"
    value = aws_dynamodb_table.feedback_table.arn
}