#Lets create EC2 instances using python boto3

import time
import boto3

script = '''#!/bin/bash
cd /home/ec2-user
sudo yum update -y
sudo amazon-linux-extras install -y lamp-mariadb10.2-php7.2 php7.2
sudo yum install -y httpd
sudo systemctl start httpd
sudo systemctl enable httpd
cd /var/www/html
aws s3 cp s3://assg2/index.html .
aws s3 cp s3://assg2/page2.html .  
'''


def hold():
    for x in range(120):
        print("Wait for ", 120-x, "seconds")
        time.sleep(1)


def create_es2_instance():
    try:
        print("Started")
        resource_ec2 = boto3.resource("ec2")
        response = resource_ec2.create_instances(
            ImageId="ami-0c2b8ca1dad447f8a",
            MinCount=1,
            MaxCount=1,
            InstanceType="t2.micro",
            KeyName="key1",
            IamInstanceProfile={'Name': 'assg2'},
            SecurityGroupIds=['sg-04394bef72211c7bd'],
            UserData=script
        )
        instance = response[0]
        print('Instance created.. waiting to be in running state')
        instance.wait_until_running()
        print('Instance in running.')
        instance.load()
        hold()
        print('public dns address: ', get_name(instance))
        import webbrowser
        webbrowser.open(get_name(instance))  # Go to example.com
        print("Completed")
    except Exception as e:
        print(e)


def get_name(inst):
    client = boto3.client('ec2')
    response = client.describe_instances(InstanceIds=[inst.instance_id])
    foo = response['Reservations'][0]['Instances'][0]['NetworkInterfaces'][0]['Association']['PublicDnsName']
    return foo


create_es2_instance()
