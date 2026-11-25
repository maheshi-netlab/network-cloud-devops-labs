resource "aws_route_table" "public" {
  vpc_id = aws_vpc.network_lab.id

  tags = {
    Name = "terraform-network-lab-public-rt"
    Type = "Public"
  }
}

resource "aws_route" "public_internet" {
  route_table_id         = aws_route_table.public.id
  destination_cidr_block = "0.0.0.0/0"
  gateway_id             = aws_internet_gateway.network_lab_igw.id
}

resource "aws_route_table" "private" {
  vpc_id = aws_vpc.network_lab.id

  tags = {
    Name = "terraform-network-lab-private-rt"
    Type = "Private"
  }
}
