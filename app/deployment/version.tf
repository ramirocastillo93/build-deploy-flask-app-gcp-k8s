# https://www.terraform.io/docs/language/settings/index.html
terraform {
  required_version = ">= 1.0.0"
  required_providers {
    helm = {
      source  = "hashicorp/helm"
      version = "~> 2.3.0"
    }
  }
  backend "gcs" {
    bucket = "tf-flash-app-v1"
    prefix = "app_state"
  }
}