# ASP.NET Core Web API Serverless Application

This project shows how to run an ASP.NET Core Web API project as an AWS Lambda
exposed through Amazon API Gateway. The NuGet package
[Amazon.Lambda.AspNetCoreServer](https://www.nuget.org/packages/Amazon.Lambda.AspNetCoreServer)
contains a Lambda function that is used to translate requests from API Gateway
into the ASP.NET Core framework and then the responses from ASP.NET Core back to API Gateway.


For more information about how the Amazon.Lambda.AspNetCoreServer package works
and how to extend its behavior view its
[README](https://github.com/aws/aws-lambda-dotnet/blob/master/Libraries/src/Amazon.Lambda.AspNetCoreServer/README.md)
file in GitHub.


### Configuring for API Gateway HTTP API ###

API Gateway supports the original REST API and the new HTTP API.
In addition HTTP API supports 2 different payload formats. When using the 2.0
format the base class of `LambdaEntryPoint` must be `Amazon.Lambda.AspNetCoreServer.APIGatewayHttpApiV2ProxyFunction`.
**Note:** when using the `AWS::Serverless::Function` CloudFormation resource with an event type of `HttpApi` the default payload
format is 2.0 so the base class of `LambdaEntryPoint` must be `Amazon.Lambda.AspNetCoreServer.APIGatewayHttpApiV2ProxyFunction`.

### Project Files ###

* serverless.yml - a configuration file defining the all the infrastructure we need to run
  our serverless application in the cloud. 
* LambdaEntryPoint.cs - class that derives from **Amazon.Lambda.AspNetCoreServer.APIGatewayProxyFunction**. The code in 
this file bootstraps the ASP.NET Core hosting framework. The Lambda function is defined in the base class.
* LocalEntryPoint.cs - for local development this contains the executable Main function which bootstraps the ASP.NET Core hosting framework with Kestrel, as for typical ASP.NET Core applications.
* Startup.cs - usual ASP.NET Core Startup class used to configure the services ASP.NET Core will use.
* Controllers\ValuesController - example Web API controller

You may also have a test project depending on the options selected.

## Here are some steps to follow from Visual Studio:

To deploy your Serverless application, right click the project in Solution Explorer and select *Publish to AWS Lambda*.

To view your deployed application open the Stack View window by double-clicking the stack name shown beneath the AWS CloudFormation node in the AWS Explorer tree. The Stack View also displays the root URL to your published application.

## Here are some steps to follow to get started from the command line:

Once you have edited your template and code you can deploy your application using the [Amazon.Lambda.Tools Global Tool](https://github.com/aws/aws-extensions-for-dotnet-cli#aws-lambda-amazonlambdatools) from the command line.

Install Amazon.Lambda.Tools Global Tools if not already installed.
Install the Amazon.Lambda.Templates to have the templates used for ASP.NET.
```sh
    dotnet tool install -g Amazon.Lambda.Tools
    dotnet new -i Amazon.Lambda.Templates
```

If already installed check if new version is available.
```sh
    dotnet tool update -g Amazon.Lambda.Tools
```

Install Project dependencies if not already done
```sh
dotnet add package AWSSDK.DynamoDBv2
dotnet add package AWSSDK.Lambda
dotnet add package Amazon.Lambda.AspNetCoreServer
dotnet add package Amazon.Lambda.APIGatewayEvents
dotnet add package AWS.Lambda.Powertools.Logging
dotnet add package AWS.Lambda.Powertools.Tracing
dotnet add package AWS.Lambda.Powertools.Metrics
```

Execute unit tests
```sh
    cd "dibs-asp-dotnet/test/dibs-asp-dotnet.Tests"
    dotnet test
```

Deploy application
```sh
    cd "dibs-asp-dotnet/src/dibs-asp-dotnet"
    dotnet lambda deploy-serverless
```
