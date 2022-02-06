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

## REST (representational state transfer)
1. Client-Server
-- A client makes a request and receives a repsonse from the server
-- The client doesnt' need to know all the details in how the server is implemented
2. Statelessness
-- The server should not be keeping track of the context of client requests
Each inbound request should have all the information necessary to process the request.
3. Cacheability
-- REsponses can potentially be cached for improved performance.
Client shouldn't care about their responses being cached
4. Layered System
-- The client makes requests against an API endpoint and receives a response. The request may have gone through layers of a system
(proxy, load balancer, etc...)
5. Uniform interface
-- The interface should be consistent, and API messages and endpoints should be self-describing.
6. HTTP REQUEST
-- Method (POST -create, GET-retrieve, PUT-replace, PATCH-update, DELETE-delete)
-- Endpoint - URL to send the request
-- Header - additional metadata
-- Body - content
7. HTTP Response
-- Response code- status of the HTTP request
-- Header - additional metadata
-- Body - content
8. URL
/api/items/<item_id>?created_by=<user_id>
-- item_id is a path parameter
-- user_id is a query parameter
### Best practices review
-- Stripe, Twilio, Plaid, Trello, Digital Ocean, Google Docs, Slack
https://www.vinaysahni.com/best-practices-for-a-pragmatic-restful-api

