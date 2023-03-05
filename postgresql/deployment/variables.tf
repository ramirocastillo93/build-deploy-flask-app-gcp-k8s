variable "pgPass" {
  description = "PostgreSQL Password"
  type        = string
}

variable "pgUser" {
  description = "PostgreSQL Username"
  type        = string
}

variable "pgDb" {
  description = "PostgreSQL Database"
  type        = string
}
variable "kubeconfig_path" {
  description = "GKE kubeconfig path (usually ~/.kube/config)"
  type        = string
}

variable "cluster_name" {
  type        = string
  description = "GKE cluster name"
}

variable "location" {
  type        = string
  description = "GKE Location"
}

variable "env" {
  description = "Environment"
  type        = string

  validation {
    condition     = contains(["prod", "dev"], var.env)
    error_message = "${var.env} not in accepted values: \"prod\", \"env\""
  }
}
