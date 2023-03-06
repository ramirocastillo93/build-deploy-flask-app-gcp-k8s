variable "env" {
  description = "Environment variable"
  type        = string

  validation {
    condition     = contains(["prod", "dev"], var.env)
    error_message = "Error! \"${var.env}\" not in acceptable values: \"prod\", \"env\""
  }
}