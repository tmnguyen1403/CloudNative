## Definition
_ Container Orchestrators:

_Pros:
Portability: open-source, platform agnostic
Scalability: in-build resources, eslaticity feature
Resilience: remediation (replicaSet, readiness, livenes probes)
Service Discovery: Cluster-level DNS, Distribute traffic
Extensibility: building-blocks principle, custom resource definition
Operational Cost: powerful scheduler
Cluster autoscaler: 

## Architecture:
_Cluster : master and work nodes
_Master : global decisions (control plane) - 
++ kube-apiserver: the nucleus of the cluster that exposes the Kubernetes API, and handles and triggers any operations within the cluster
++ kube-scheduler - the mechanism that places the new workloads on a node with sufficient satisfactory resource requirements
++ kube-controller-manager - the component that handles controller processes. It ensures that the desired configuration is propagated to resources
++ etcd - the key-value store, used for backs-up and keeping manifests for the entire cluster
_Worker : dataplane - host workloads -
++ kubelet - the agent that runs on every node and notifies the kube-apiserver that this node is part of the cluster
++ kube-proxy - a network proxy that ensures that reachability and accessibility of workloads places on this specific node

## Terms
CRD - Custom Resource Definition provides the ability to exetend Kubernetes API and create new resources
Node - a physical or virtual server
Cluster - a collection of distributed nodes that are used to manage and host workloads
Master node - a node from the Kubernetes control plane, that has installed components to make global, cluster-level decisions
Worker node - a node from the Kubernetes data plane, that has installed components to host workloads

## References
https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/


