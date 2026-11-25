resource "aws_internet_gateway" "network_lab_igw" {
  vpc_id = aws_vpc.network_lab.id

  tags = {
    Name = "terraform-network-lab-igw"
  }
}
