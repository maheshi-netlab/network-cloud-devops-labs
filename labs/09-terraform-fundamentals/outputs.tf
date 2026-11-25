output "vpc_id" {
  description = "ID of the network lab VPC"
  value       = module.network.vpc_id
}

output "vpc_cidr" {
  description = "CIDR block of the network lab VPC"
  value       = module.network.vpc_cidr
}

output "public_subnet_id" {
  description = "ID of the public subnet"
  value       = module.network.public_subnet_id
}

output "private_subnet_id" {
  description = "ID of the private subnet"
  value       = module.network.private_subnet_id
}

output "internet_gateway_id" {
  description = "ID of the Internet Gateway"
  value       = module.network.internet_gateway_id
}

output "security_group_id" {
  description = "ID of the network lab security group"
  value       = aws_security_group.network_lab.id
}

output "ec2_instance_id" {
  description = "ID of the network lab EC2 instance"
  value       = aws_instance.network_lab.id
}

output "ec2_private_ip" {
  description = "Private IP address of the EC2 instance"
  value       = aws_instance.network_lab.private_ip
}

output "ec2_public_ip" {
  description = "Public IP address of the EC2 instance"
  value       = aws_instance.network_lab.public_ip
}
