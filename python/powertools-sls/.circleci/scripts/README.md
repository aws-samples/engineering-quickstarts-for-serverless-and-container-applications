# IDT Provisioning Instructions

This document provides a step by step procedure for IDT instrcutors to follow in provisioning an AWS Integrated DevOps Toolchain (IDT) environment to facilitate training, workshops, iead labs etc...

## Package 0: Provisioning  + Prerequisties

These instructions are drafts and will be broken out into sections using labels used by the AWS and CircelCI teams. We will use the Generic term `Package:` followed by a number to designate which segment of the project we're addressing. The Package: term is for internal use at the moment.

**Package 0:** Defines the core segment. Subsequent packages will be built upon Package 0.

## GitHub Organization

A GitHub Organization must be created. The following will guid you through creating a GitHub organization.

**Step 1: Login to GitHub**
- Login to your GitHub account. Go to GitHub's official website "[github.com](https://github.com)" and enter your login credentials.

**Step 2: Go to the New Organization Creation Page**
- After logging in, click on your profile picture (avatar) on the top right side of your dashboard screen. A dropdown menu will appear.
- Click on "Your organizations" in the dropdown menu. It will forward you to another page.
- On this page, click on the green button "New organization" on the right side.

**Step 3: Choose Your Plan**
- You will be asked to choose your plan. You can choose either Free or Team.
- Choose as per your requirement. If you're creating just for practice then go with the 'Free' plan. Click the 'Next' button after selecting the plan.

**Step 4: Fill out Organization Details**
- You will be taken to a 'Create a new organization' page.
- Fill in the Organization account name which should be unique.
- Provide an email (The email will help GitHub to send updates related to organization).
- Choose your Team/Project name. 
- Click on 'Create Organization'.

**Step 5: Invite Members**
- After creating the organization, you can optionally enter the usernames or email addresses of other GitHub users you want to add to your new organization.
- You can also define a role for new members whether they are owners or just members.
- Then, click the "Invite" button to send them an invitation. 

**Step 6: Setup Teams (Optional)**
- You can also set up different teams for your organization. It helps you manage access control by grouping users permissions into teams.

**Step 7: Verify your Email**
- Finally, you'll receive a verification link in your email that you've provided for the organization.
- Go to your email and click on the verification link to verify your account. 

Your organization is now created and active on GitHub! You can start creating repositories and start working on your projects. Remember, any repositories, issues, and notes created under this organization will belong to it as per GitHub rules.

## Fork the AWS IDT Example repo into a GitHub Organization

Sure, here is a step-by-step guide on how to fork the provided repository into a GitHub organization:

**Step 1: Go to the Repository Link**
- Open the link to the repository you wish to fork: [https://github.com/aws-samples/engineering-quickstarts-for-serverless-and-container-applications](https://github.com/aws-samples/engineering-quickstarts-for-serverless-and-container-applications)

**Step 2: Start the Forking Process**
- Click on the 'Fork' button. This is located in the top right part of the webpage, right next to the 'Star' and 'Watch' buttons.

**Step 3: Choose the Destination**
- Once you click on 'Fork', a popup appears asking you where you want to fork the repository. This is where you should choose the organization where you want the fork to go to.

**Step 4: Fork Initialization**
- After selecting the organization, GitHub starts the forking process, creating a new repository in the selected organization. This process may take several seconds, depending on the size of the repository.

**Step 5: Workflow Verification**
- When the process finishes, you'll be redirected to the forked repository in your GitHub organization.

Remember, you need to be an owner or have sufficient permissions in the organization to create new repositories, in order to be able to fork repositories into a GitHub organization. If the chosen place is an organization and you don't have the required permissions, you'll need to contact the organization administrators.

## CircleCI - Provision and setup project

**Step 1: Create a CircleCI Account**

Create a CircleCI account by doing the following:

- Visit [https://circleci.com/](https://circleci.com/)
- Click on 'Go to app' or 'Start building for free'.
- Click on 'Sign Up' and sign up with GitHub. You'll be redirected to the GitHub login page.
- Enter your GitHub Account Credentials and click on 'Sign In'.
- If prompted, authorize CircleCI to have access to your GitHub account.

**Step 2: Connect Your repository to CircleCI**

After that, set up the integration with the forked GitHub repository:

- Within the CircleCI app, navigate to 'Project', present on the left side of the sidebar.
- Click on the 'Set Up Project' button next to the repository you want to build (which in this case, is the forked repository).
- Choose the operating system and language that matches your project.
- On the next page, click 'Start Building'. Your repository is now connected to CircleCI and it will run a build every time you commit to your repository.

This completes your CircleCI setup and your forked repository should now be linked to your CircleCI account.

## CircleCI Enable Orb usage in Organizations

**Step 1: Sign in to CircleCI**

Sign in to your CircleCI account using your GitHub or Bitbucket credentials.

**Step 2: Select Your Organization**

On the landing page, choose the organization for which you'd like to enable the use of Orbs.

**Step 3: Access Organization Settings**

Click on the "Settings" gear icon in the bottom-left corner of your CircleCI dashboard.

**Step 4: Navigate to Security Section**

Within the left navigation panel, under the "ORGANIZATION SETTINGS" section, click on "Security".

**Step 5: Allow Uncertified Orbs**

Within the "Security Settings" section, you will find an option saying "Allow Uncertified Orbs". Toggle this option to enable the usage of uncertified orbs. 

**Step 6: Save Changes**

Click the Save button to apply the changes.


## Pacakage: 1 - Extensible Segments

In this package you'll provision accounts and access for the various services and tools your pipelines will integrate with.

## CircleCI Context environment variable provisioning

This section demostrates how to create CircleCI Context Environment Variables programaticaly using a special purpose built python script. You must provide the script the data it will use to create the context variables for your project. These values are defined and stored in the `credentials.toml` file.

## Capture credentials from the services and tools you will use in your pipeline.

For this section we will demonstrate how to generate a new `credentials.toml` file and populate it with the values for the respective integrations. In this examnple we'll use, Snyk, Git Guardian and AWS services which will require you to create a new account and generate new API Tokens for the respective integration.

## Git Guardian

Follow the step-by-step instructions below to create a new account and generate API Tokens on GitGuardian:

### Creating a new account

**Step 1:** Head to GitGuardian's homepage

Access GitGuardian's website by entering the following URL into your browser: `https://www.gitguardian.com/`.

**Step 2:** Click on `Get Started`

You can find this button on the upper right side of the screen. 

**Step 3:** Create a New Account

In the login screen, click on the `Sign up` link.

**Step 4:** Provide Required Information

You will need to enter the following information to create your account:
- Your first and last name
- Company name (if applicable)
- Job title (if applicable)
- Your work email
- Password of your choosing

Make sure to read and agree to GitGuardian's Terms of Service and Privacy Policy before proceeding.

**Step 5:** Verification

After providing all information, click `Sign up`. Check your provided email for a verification link from GitGuardian and verify your account by clicking on the link.

**Step 6:** Log in with your new credentials

Log in to your GitGuardian account using your email and the password you created.

### Generating an API Token

**Step 1:** Navigate to the API Dashboard

Once logged in, click on the `Dashboard` button, then the `API` button.

**Step 2:** Create a new API Token

On the API page, click on the `Create new token` button.

**Step 3:** Provide a name for your token

You will be prompted to name the new API token. Using a descriptive name can be beneficial to remember what specific project or purpose the token was created for.

**Step 4:** Token Configuration

Choose the permissions and scope for this token based on your needs. Be cautious while doing this since the token authorization can provide access to your GitGuardian account.

**Step 5:** Generate the Token

After setting the configurations, click on the `Generate token` button. 

**Step 6:** Copy your new API Token

Once the token is generated, it will be displayed to you. Be sure to copy the auth token string to `credentials.toml` - `snyk_token` 

**Note:** Treat your API tokens as you would your password - don't share them with untrusted third parties, don't transmit them insecurely, and don’t commit them in your codebase.

## Snyk

We will use Snyk to run an automated security scan of our application an its dependencies. 

- Create an account with Snyk - https://app.snyk.io/
- Skip the integration step by clicking "Choose other integration" at the bottom of the options list.
- Click on your avatar in the bottom of the sidebar to show a dropdown
- Choose "Account Settings"
- Click to show your Auth Token
- Copy the auth token string to `credentials.toml` - `snyk_token` 

### CircleCI

Create a CircleCI Personal API token:

**Step 1**
Visit the CircleCI official website and log in to your account. You will need an existing account on CircleCi to proceed. 

**Step 2**
After logging in, navigate to the main dashboard, where you will see an overview of your projects. 

**Step 3**
In the left-hand navigation sidebar, click on "User".

**Step 4**
In the opened drop-down list, select "Personal API Tokens".

**Step 5**
On the Personal API Tokens page, click on the "Create New Token" button. 

**Step 6**
A dialog box will appear. You will need to input the name of your new token. It helps to give it a name that represents its purpose. After typing the token name, click on the "Add API Token" button.

**Step 7**
Your new token will be generated and shown to you. Please remember to copy it and keep it safe since it will not be shown again for security reasons. 

**Step 8**
Once you have copied your token, click on the "I have copied my token" button.

You have now successfully created your CircleCI Personal API Token! Use it carefully and remember, it's personal, so it's crucial to keep it secured and not share it with anyone else. Always remember to regenerate a new token if you suspect a security threat.

### Configure credemtials in the credentials.toml file

Copy over the credentials source file. This is untracked in Git and will be used by a script to populate your CircleCI secret variables.

```
cd python/powertools-sls/.circleci/scripts

cp .circleci/scripts/sample_credentials.toml credentials.toml
```

In the credentials.toml file, populate the values of the respective keys with the credentials you captured in previous steps. These values will be retirived by the provisioning.py script and create the context variables in the CircleCI platform.


Install Python depedencies:

```
pip3 install -r requirements.txt
```

#### Provision Context environment variables

In this step you will excute the `provsioning.py` script to create the environment variables used in your project

```
python3 provisioning.py
```

Upon completion the contexts variables and their values will be created for yourt project.

## Create AWS ODIC Access for CircelCI Pipelines

Here are the step-by-step instructions on how to create an AWS OpenID Connect (OIDC) connection and use it with CircleCI:

**Step 1: Create an IAM OIDC identity provider**

1. In the AWS Management Console, navigate to the IAM service.
2. In the navigation pane on the left, choose "Identity Providers" and then choose "Create Provider".
3. For "Provider Type", choose "OpenID Connect".
4. For "Provider URL", type your OIDC identity provider URL.
5. For "Audience", type your audience string. This is typically the client ID for your application.
6. Choose "Verify Provider Information" and then choose "Create".

**Step 2: Create an IAM role for CircleCI and attach policies**

1. Navigate to the IAM service in the AWS Management Console.
2. In the navigation pane, choose "Roles" and then choose "Create role".
3. For "Select type of trusted entity", choose "Web identity".
4. For "Identity provider", choose the OIDC identity provider you created in the first step.
5. For "Audience", type the audience you specified when you created the identity provider.
6. Choose "Next: Permissions".
7. Attach the specific policy that CircleCI requires for the tasks it performs for your service or application.
8. Choose "Next: Tags" - add tags if required.
9. Name the role and provide an adequate description.
10. Click "Create Role".




