variable "databricks_host" {
  description = "A URL do workspace do Databricks"
  type        = string
}

variable "databricks_token" {
  description = "O token de autenticação do Databricks"
  type        = string
  sensitive   = true
}