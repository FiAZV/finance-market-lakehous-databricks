terraform {
  required_providers {
    databricks = {
      source  = "databricks/databricks"
      version = "~> 1.0" # Define a versão do provider
    }
  }
}

provider "databricks" {
  host  = var.databricks_host
  token = var.databricks_token
}