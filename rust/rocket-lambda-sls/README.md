# rust-serverless
Current status:
    Working first on the Inventory Microservice and devising a standardized deployment strategy.
    Have yet to start working on Cart, Wishlist Microservices, though they will follow the same structure and libraries as listed below.

Key parts of the Environment (currently) are:
* Rocket - Webserver
* Tokio - Async Runtime
* aws-sdk-dynamodb - AWS API Integration for DynamoDB API calls
* lambda-web - Bootstraps our Web Server (Rocket) for AWS Lambda
* opentelemetry-rust - Specifically the opentelemetry-aws and opentelemetry-http

## Getting Started
Setting up a Rust powered lambda API

Install [Cargo-Lambda](https://www.cargo-lambda.info/guide/getting-started.html) to make rust's build manager (cargo) aware of AWS Lambda.

Use `cargo lambda new <API-Name>` to create a folder that's ready for you to program in rust.

Install the following to our rust environment:
* [Rocket](https://rocket.rs/)
* [Tokio](https://tokio.rs/)
* [aws-sdk-dynamodb](https://docs.rs/aws-sdk-dynamodb/latest/aws_sdk_dynamodb/)
* [lambda-web](https://crates.io/crates/lambda-web)
* [opentelemetry-rust](https://opentelemetry.io/docs/instrumentation/rust/) - Specifically opentelemetry-aws and opentelemetry-http

to bootstrap the rust runtime within lambda and run the rocket webserver.

---
