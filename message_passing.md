## Consideration

### Technical
-- Cost -memory, CPU, and overhead needed to handle messages
-- Maintainability - ease of modifications and enhancements
-- Efficiency - the amount of time it takes to handle a message or multiple messages
-- Reliability - messages being lost or improperly processed

### Business
-- Cost - financial impact of paying for infrastructure
-- Maintainability - financial impact of developers to upkeep the system; ease of integration for external customers
-- Efficiency- productivity and cost-effectiveness of systems
-- Reliability - risks for when a system becomes unavailable for the user; reputation of business services

## Monolith vs Microservices
-- Monoliths are easier to develop and have less overhead for infrastructure
-- Microservices are more scalable and enable parallel development as multiple developers can easily work simultaneously on different parts of the application
-- Refactoring each microservice to make small changes can become frustrating and overwhelming
-- It is safer to start with a MONOLITH
-- Microservices are inherently more complex than monoliths
-- Microservices have more moving pieces: services are individually deployed and communicate througha network
-- Microservices are a distributed system. Distributed systems come with new properties that inherently make it more complex than a single-node system like a monolith. All distributed systems are inevitably at risk for network failures and need additional overhead to manage the inherent risk.


## Creating dependency graph
-- Review source code
-- Review existing documentation
-- Understand external use cases
-- http://www.cs.sjsu.edu/faculty/pearce/modules/lectures/ood/metrics/Dependency.htm
-- https://en.wikipedia.org/wiki/CAP_theorem

## Refactor to Microservices
-- Use dependency graph
-- Refactor the least downstream effect
-- Strangler Pattern: gradually replace components of the application
-- https://martinfowler.com/bliki/StranglerFigApplication.html
-- https://docs.microsoft.com/en-us/azure/architecture/patterns/strangler-fig
-- https://aws.amazon.com/blogs/enterprise-strategy/the-great-cloud-refactoring-debate/
-- It is okay to have duplicate code
-- https://overreacted.io/goodbye-clean-code/
-- https://sandimetz.com/blog/2016/1/20/the-wrong-abstraction?duplication
-- 