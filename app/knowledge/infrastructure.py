"""
Infrastructure knowledge base.

Contains deterministic descriptions of common
cloud infrastructure resources.
"""

RESOURCE_INSIGHTS = {
    # Networking
    "aws_vpc": ("Forms the networking foundation of the infrastructure."),
    "aws_subnet": (
        "Provides network placement for dependent infrastructure resources."
    ),
    "aws_security_group": (
        "Controls network access to dependent infrastructure resources."
    ),
    "aws_route_table": ("Determines network traffic routing for associated resources."),
    "aws_internet_gateway": (
        "Provides external connectivity for public infrastructure."
    ),
    "aws_nat_gateway": ("Enables outbound internet access for private resources."),
    # Compute
    "aws_instance": (
        "Represents an application workload that may be directly exposed."
    ),
    "aws_launch_template": (
        "Defines the configuration used to launch compute resources."
    ),
    "aws_autoscaling_group": (
        "Manages the availability and scaling of application instances."
    ),
    # Storage
    "aws_s3_bucket": ("Stores application or business data."),
    "aws_ebs_volume": ("Provides persistent block storage for compute resources."),
    "aws_db_instance": ("Hosts persistent application data."),
    # Load Balancing
    "aws_lb": ("Distributes incoming traffic across application resources."),
    "aws_lb_target_group": ("Defines traffic destinations behind the load balancer."),
    "aws_lb_listener": ("Controls how client traffic reaches backend services."),
}
