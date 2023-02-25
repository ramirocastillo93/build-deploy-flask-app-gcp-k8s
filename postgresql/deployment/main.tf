# Deploy pgsql cluster on GKE

# https://registry.terraform.io/providers/hashicorp/helm/latest/docs
provider "helm" {
  kubernetes {
    config_path = var.kubeconfig_path
  }
  alias = "gke"
}

# https://www.terraform.io/docs/language/settings/index.html
terraform {
  required_version = ">= 1.0.0"
  required_providers {
    helm = {
      source  = "hashicorp/helm"
      version = "~> 2.3.0"
    }
  }
}

module "postgresql" {
  source = "../modules"

  enable_ha          = var.env == "prod" ? true : false
  postgresqlPassword = var.pgPass
  postgresqlUsername = var.pgUser
  postgresqlDatabase = var.pgDb

}