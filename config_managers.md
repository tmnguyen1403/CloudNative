## Configuration managers are tools that help to manage manifest files
1. Helm - package manager that templates exiting manifests, and uses input files to tailor configuration for each environment
2. Kustomize - a template-free mechanism that uses a base and mutiple overlays, to manage the configuration for each environment
3. Jsonnet - a programming language, that enables the templating of manifests as JSON files, that can be easily consumed by Kubernetes
