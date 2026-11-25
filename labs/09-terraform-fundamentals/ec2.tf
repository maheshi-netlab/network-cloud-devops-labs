resource "aws_instance" "network_lab" {
  ami                    = "ami-0c02fb55956c7d316"
  instance_type          = "t2.micro"
  subnet_id              = module.network.public_subnet_id
  vpc_security_group_ids = [aws_security_group.network_lab.id]

  associate_public_ip_address = true

  tags = {
    Name = "terraform-network-lab-ec2"
    Role = "Network-Lab-Server"
  }
}
