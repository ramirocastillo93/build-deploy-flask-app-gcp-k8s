variable "env" {
  description = "Environment variable"
  type        = string

  validation {
    condition     = contains(["prod", "dev"], var.env)
    error_message = "Error! \"${var.env}\" not in acceptable values: \"prod\", \"env\""
  }
}

variable "k8s_secret_name" {
  type        = string
  description = "Kubernetes secret name"
}

variable "k8s_secret_server" {
  type        = string
  description = "Kubernetes server name"
}

variable "k8s_secret_username" {
  type        = string
  description = "Kubernetes username"
}

variable "k8s_secret_password" {
  type        = string
  description = "Kubernetes password"
}