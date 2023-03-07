terraform {
  # required_version = ">= 1.3.1"
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "4.54.0"
    }
  }
  backend "gcs" {
    bucket = "tf-flask-app-v1"
    prefix = "state"
  }
}