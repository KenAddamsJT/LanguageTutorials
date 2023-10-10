# K8s

A container is a standard unit of software that packages up code and all its dependencies allowing the application to reliably run across computing environments. It includes everything required to run an application, that is the application code, runtime, system tools, libraries and settings.

But are these by themselves enough to provide modern day resilient & scalable applications? The answer is no! And for these and multiple other reasons, we need a framework on top of the container entities. Kubernetes is a portable, extensible, open source platform for managing containerized workloads and services. Facilitating both declarative configuration and automation.

K8s resources are created via YAML configuration files.

The smallest deployable unit in K8s is a "pod". It is a logical host of one or more containers, which is ephemeral in design. Their configuration define the container images, ports, environment variables and other settings required to run the defined containers. Containers within a pod can connect to each other via localhost.

Next up to scale the number of running pods, we have the replicaSet controller, which ensures that a defined number of pods are running at any given time. A replicaSet ensures the parity between the actual and desired state by creating/deleting pods as required.

K8s deployments are a higher level abstraction over replicasets. They provide advanced features for updating (example: rolling updates) and rolling back applications while maintain a history of revisions.

K8s Services are controllers responsible for selecting and load balancing requests to pods based on labels and selectors. Although each launched pod gets its own IP-Address, pods are volatile entities, thus the need for a stable network endpoint for accessing pods arises, which is provided by Services.

K8s volumes provide persistent storage solutions to such application beyond the lifecycle of their containers / scheduled pods. 

We also have ConfigMaps & Secrets which can be mounted to the container file system at runtime and be utilized to configure the application / running job or to make secure transactions using the mounted secrets.
