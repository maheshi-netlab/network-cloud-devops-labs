resource "aws_subnet" "public" {
  vpc_id                  = aws_vpc.network_lab.id
  cidr_block              = var.public_subnet_cidr
  availability_zone       = "us-east-1a"
  map_public_ip_on_launch = true

  tags = {
    Name        = "terraform-network-lab-public-subnet"
    Type        = "Public"
    Environment = var.environment
  }
}

resource "aws_subnet" "private" {
  vpc_id                  = aws_vpc.network_lab.id
  cidr_block              = var.private_subnet_cidr
  availability_zone       = "us-east-1b"
  map_public_ip_on_launch = false

  tags = {
    Name        = "terraform-network-lab-private-subnet"
    Type        = "Private"
    Environment = var.environment
  }
}
