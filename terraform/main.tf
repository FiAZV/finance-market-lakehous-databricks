data "databricks_node_type" "smallest" {
  local_disk = true
}

data "databricks_spark_version" "latest_lts" {
  long_term_support = true
}

data "databricks_catalog" "wolf_of_wallstreet" {
  name = "wolf_of_wallstreet"
}

resource "databricks_schema" "bronze_finance" {
  catalog_name = data.databricks_catalog.wolf_of_wallstreet.name
  name         = "bronze_finance"
  comment      = "this schema is managed by terraform"
  properties = {
    kind = "various"
    layer = "bronze"
  }
}

resource "databricks_schema" "silver_finance" {
  catalog_name = data.databricks_catalog.wolf_of_wallstreet.name
  name         = "silver_finance"
  comment      = "this schema is managed by terraform"
  properties = {
    kind = "various"
    layer = "silver"
  }
}

resource "databricks_schema" "gold_finance" {
  catalog_name = data.databricks_catalog.wolf_of_wallstreet.name
  name         = "gold_finance"
  comment      = "this schema is managed by terraform"
  properties = {
    kind = "various"
    layer = "gold"
  }
}

resource "databricks_volume" "landind" {
  name             = "landind"
  catalog_name     = data.databricks_catalog.wolf_of_wallstreet.name
  schema_name      = databricks_schema.bronze_finance.name
  volume_type      = "MANAGED"
  comment          = "Volume for landing zone"
}