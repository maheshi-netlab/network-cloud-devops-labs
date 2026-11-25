locals {
  name_prefix = "terraform-network-lab"

  environment_type = var.environment == "Production" ? "prod" : "non-prod"

  common_tags = {
    Project         = "Network-Cloud-DevOps-Labs"
    Environment     = var.environment
    EnvironmentType = local.environment_type
    ManagedBy       = "Terraform"
  }
}
