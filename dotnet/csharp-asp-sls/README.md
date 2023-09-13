# AWS DevOps in a Box (DiBs) ASP.NET Core, Powertools, Serverless Template

This repository contains two templates for creating serverless applications
using ASP.NET Core, Lambda Powertools, and Serverless Framework.

This template is designed to help you get started with serverless development
using ASP.NET Core, Lambda Powertools, and Serverless Framework. It is not
intended to be a comprehensive guide or a production-ready solution. You should
always review the code and modify it according to your needs and organization
best practices.

The templates include:

- A `serverless.yml` file that defines the AWS resources and configuration
  for your application.
- Full Visual Studio projects containing all required dependencies

To use this template, you need to have .NET 6.0 or higher, Serverless Framework,
and AWS CLI installed on your machine. You also need to have an AWS account
and configured credentials for serverless framework to deploy in AWS.

To get started, clone the repository, and run `dotnet restore`
to install the dotnet dependencies. Then, you can modify the `serverless.yml`
file and the various classes and files in the project to your needs.

Lambda Powertools is a suite of .NET libraries that makes it easier to implement
best practices for serverless applications, like distributed logging, tracing,
metrics, and error handling. It also provides native integration and fast load
times with .NET 6. You can learn more about Lambda Powertools here: [.NET Lambda Powertools](https://github.com/aws-powertools/powertools-lambda-dotnet).

