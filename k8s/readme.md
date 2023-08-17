# Kubernetes (K8s)

1. **Orchestration**: Kubernetes (K8s) orchestrates containerized app deployment and scaling.
2. **Containers**: It uses containers for app packaging and portability.
3. **Clusters**: K8s manages server clusters, abstracting infrastructure.
4. **Master-Worker**: A Master node manages, while Worker nodes run apps.
5. **Configuration**: Developers define app states in YAML files.
6. **Scalability**: K8s scales apps horizontally, adapting to loads.
7. **Self-Healing**: Monitors app health, auto-replacing failures.
8. **Updates**: Supports seamless app updates without downtime.
9. **Extensions**: Extensive plugin ecosystem for monitoring, more.


# the Learning Plan

**Introduction to Containers and Docker**
- Learn how to create, run, and manage Docker containers.

**Kubernetes Fundamentals**
- Get an overview of Kubernetes architecture and components.
- Learn about Pods, Deployments, Services, and ConfigMaps.

**Practical Kubernetes Setup**
- Set up a local Kubernetes environment using tools like Minikube or Kind.
- Deploy a simple application using Kubernetes manifest files.

**Kubernetes Deployments**
- Understand Deployments and ReplicaSets for managing application scaling.

**Kubernetes Services**
- Learn about Kubernetes Services for networking and load balancing.

**Kubernetes Configurations and Secrets**
- Understand ConfigMaps and Secrets for managing configuration data.

**Horizontal Pod Autoscaling and Resource Management**
- Learn about Horizontal Pod Autoscaling to dynamically adjust resources.
- Optimize resource requests and limits for your ML workloads.

**Custom Kubernetes Resources**
- Dive into Custom Resources like CustomResourceDefinitions (CRDs) for specialized ML use cases.
- Experiment with customizing Kubernetes behavior using CRDs.

**Monitoring and Logging**
- Learn how to monitor resource usage, application health, and logs in Kubernetes.
- Explore tools like Prometheus, Grafana, and Kubernetes-native logging solutions.

**Multi-container Pods and Sidecars**
- Explore scenarios where multiple containers collaborate in a single Pod.
- Understand how sidecar containers can enhance your ML deployments.

**Helm and Package Management**
- Learn about Helm, a package manager for Kubernetes.
- Create and manage Helm charts to simplify deploying complex ML applications.
