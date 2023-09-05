# AWS DevOps in a Box (DiBs) Python, Powertools, Serverless Template

This repository contains a template for creating serverless applications using
Python, Lambda Powertools, and Serverless Framework. It also includes a CI/CD
pipeline using CircleCI to automate the deployment of your application to AWS.

This template is designed to help you get started with serverless development
using Python, Lambda Powertools, and Serverless Framework. It is not intended
to be a comprehensive guide or a production-ready solution. You should always
review the code and modify it according to your needs and best practices.

The template includes:

- A `serverless.yml` file that defines the AWS resources and configuration
for your application.
- A `requirements.txt` file that lists the Python dependencies for your
application.
- A `src` folder that contains the Python code for your serverless functions.
- A `tests` folder that contains unit tests and integration tests for your
serverless functions.

To use this template, you need to have Python 3.8 or higher, Serverless Framework,
and AWS CLI installed on your machine. You also need to have an AWS account and
configure your credentials for Serverless Framework.

To get started, clone this repository and run `pip install -r requirements.txt`
to install the Python dependencies. Then, you can modify the `serverless.yml`
file and the `src` folder to suit your needs.

Lambda Powertools is a suite of Python libraries that makes it easier to implement
best practices for serverless applications, such as logging, tracing, metrics,
and error handling. It also provides some handy features such as parameter store
caching, middleware injection, and event source data classes. You can learn more
about Lambda Powertools here: [Python Lambda Powertools](https://awslabs.github.io/aws-lambda-powertools-python/)

Serverless Framework is a tool that simplifies the development and deployment of
serverless applications on various cloud providers. CircleCI is a cloud-based
platform that provides continuous integration and delivery for your code.

## Requirements
If you're at an AWS event, follow the instructions provided under (At an AWS Event)[#at-an-aws-event]

### Bring your own Account
To get started and use this template, you need the following installed on
your local machine:
* Python 3.8 or higher
* Serverless Framework CLI
* AWS CLI

You may also need to configure your AWS CLI with credentials, please follow the
instructions provided
[here](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html).

To test the CI/CD functionality provided by this template:
You also need to have a [CircleCI account](https://circleci.com/signup/) and an
AWS account with the appropriate permissions.

You can customize the template by editing the serverless.yml file and the src
folder where your lambda functions are located. You can also add tests,
dependencies, and other configurations as needed.

### At an AWS event
Please use the pre-provided Cloud9 environment in the account.

You will need to either setup a [CircleCI](https://circleci.com/signup/) with
AWS credentials or use a pre-existing CircleCI account with the appropriate
AWS credentials already added. To set these up, refer to CircleCI's documentation
on the AWS Orb [here](https://circleci.com/developer/orbs/orb/circleci/aws-cli).

To deploy your application, you need to push your code to a GitHub repository
and connect it to CircleCI. You can follow the instructions on the CircleCI
website to set up your project and environment variables. Once you have done
that, CircleCI will automatically build and deploy your application to AWS
whenever you push new changes to your repository.

## Usage

### Deployment

In order to deploy the example, you need to run the following command:

```
$ serverless deploy
```

After running deploy, you should see output similar to:

```bash
Deploying aws-python-project to stage dev (us-east-1)

✔ Service deployed to stack aws-python-project-dev (112s)

functions:
  hello: aws-python-project-dev-hello (1.5 kB)
```

### Invocation

After successful deployment, you can invoke the deployed function by using the
following command:

```bash
serverless invoke --function hello
```

Which should result in response similar to the following:

```json
{
    "statusCode": 200,
        "body": {
            "message": "Congrtulations! You have deployed and tested an AWS Lambda using DiBs"
        }
}
```

### Local development

You can invoke your function locally by using the following command:

```bash
serverless invoke local --function hello
```

Which should result in response similar to the following:

```json
{
    "statusCode": 200,
        "body": {
            "message": "Congrtulations! You have deployed and tested an AWS Lambda using DiBs"
        }
}
```

### Bundling dependencies

In case you would like to include third-party dependencies, you will need to use a plugin called `serverless-python-requirements`.
You can set it up by running the following command:

```bash
serverless plugin install -n serverless-python-requirements
```

Running the above will automatically add `serverless-python-requirements` to
`plugins` section in your `serverless.yml` file and add it as a `devDependency`
to `package.json` file. The `package.json` file will be automatically created
if it doesn't exist beforehand. Now you will be able to add your dependencies
to `requirements.txt` file (`Pipfile` and `pyproject.toml` is also supported but
requires additional configuration) and they will be automatically injected to
Lambda package during build process. For more details about the plugin's
configuration, please refer to
[official documentation](https://github.com/UnitedIncome/serverless-python-requirements).
