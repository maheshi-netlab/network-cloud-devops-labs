variable "vpc_cidr" {
  description = "CIDR range for the network lab VPC"
  type        = string
}

variable "public_subnet_cidr" {
  description = "CIDR range for the public subnet"
  type        = string
}

variable "private_subnet_cidr" {
  description = "CIDR range for the private subnet"
  type        = string
}

variable "environment" {
  description = "Deployment environment"
  type        = string
}

variable "name_prefix" {
  description = "Prefix for network resource names"
  type        = string
}

variable "common_tags" {
  description = "Common tags applied to network resources"
  type        = map(string)
}
