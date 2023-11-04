# CircleCI Provisioning

## Prep

The commands used here are mostly using Bash, Git, and Python 3 - make sure they are installed and available. If using Windows, the commands might be different than the ones listed here.

Copy over the credentials source file. This is untracked in Git and will be used by a script to populate your CircleCI secret variables.

```
cp .circleci/scripts/sample_credentials.toml credentials.toml
```

Install Python depedencies:

```
pip3 install -r requirements.txt
```

### IMPORTANT! Sign up for the required services and prepare credentials

Create accounts in the 3rd party services you intend to integrate your pipelines with.

#### AWS IAM Account

Input your AWS credentials into the credentials.toml file.

- Copy the AWS Access Key ID and Secrets strings into `credentials.toml` - `AWS_ACCESS_KEY_ID`
- Copy the AWS Secret Access Key strings into `credentials.toml` - `AWS_SECRET_ACCESS_KEY`

#### Snyk

We will use Snyk to run an automated security scan of our application an its dependencies. 

- Create an account with Snyk - https://app.snyk.io/
- Skip the integration step by clicking "Choose other integration" at the bottom of the options list.
- Click on your avatar in the bottom of the sidebar to show a dropdown
- Choose "Account Settings"
- Click to show your Auth Token
- Copy the auth token string to `credentials.toml` - `snyk_token` 

## CircleCI

Follow these steps to set up a new project in CircleCI:

- In the CircleCI web app, click Projects in the sidebar.
- Find your project in the list and click the blue Set Up Project button next to it.
- If you cannot see your project, check you have selected the correct organization in the top left-hand corner of CircleCI.
- Once you have set up your project, you will be prompted to provide a config.yml file.
- From the pop-up window, select your preferred option. You can either:
    - Include a config.yml in the .circleci directory of your repo.
    - Commit a starter CI pipeline to a new branch of your repo.
    - Use an editable config.yml template.
    - If you choose the starter CI pipeline, a sample config.yml file is created and committed to a circleci-project-setup branch in your repo.
    - For guidance on creating a config.yml file, see Configuration Introduction.
    - Click the blue Set Up Project button.

#### Provision Context environment variables

In this step you will excute the `provsioning.py` script to create the environment variables used in your project

```
python3 python/powertools-sls/.circleci/scripts/provisioning.py
```

Upon completion the contexts variables and their values will be created for yourt project.

<!-- #### Terraform Cloud

Provision Terraform Cloud.

- Create an account with Terraform Cloud - https://app.terraform.io/ 
- Go to your user settings by clicking on your avatar (top left), and select "User Settings"
- From there, click on "Tokens"
- Create an API token
- Copy the token string to `credentials.toml` - `tf_cloud_token` -->

