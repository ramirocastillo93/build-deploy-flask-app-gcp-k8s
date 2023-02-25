variable "env" {
  description = "Environment"
  type        = string

  validation {
    condition     = contains(["prod", "dev"], var.env)
    error_message = "${var.env} not in accepted values: \"prod\", \"env\""
  }
}

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