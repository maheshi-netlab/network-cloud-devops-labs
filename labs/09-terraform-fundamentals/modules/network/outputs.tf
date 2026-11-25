output "vpc_id" {
  description = "ID of the network lab VPC"
  value       = aws_vpc.network_lab.id
}

output "vpc_cidr" {
  description = "CIDR block of the network lab VPC"
  value       = aws_vpc.network_lab.cidr_block
}

output "public_subnet_id" {
  description = "ID of the public subnet"
  value       = aws_subnet.public.id
}

output "private_subnet_id" {
  description = "ID of the private subnet"
  value       = aws_subnet.private.id
}

output "internet_gateway_id" {
  description = "ID of the Internet Gateway"
  value       = aws_internet_gateway.network_lab_igw.id
}
