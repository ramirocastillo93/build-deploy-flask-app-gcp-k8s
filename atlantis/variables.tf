variable "project_id" {
  type        = string
  description = "Project ID"
}

variable "region" {
  type        = string
  description = "Region name"
}

variable "cluster_name" {
  type        = string
  description = "Cluster name"
}

variable "namespace_name" {
  type        = string
  description = "Namespace name to be created"
}

variable "env" {
  type        = string
  description = "Environment: \"prod\" or \"dev\""

  validation {
    condition     = contains(["prod", "dev"], var.env)
    error_message = "Error! \"${var.env}\" not in possible values: \"prod\" or \"dev\""
  }
}

