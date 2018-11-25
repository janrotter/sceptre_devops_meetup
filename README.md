# sceptre DevOps Meetup

Slides from the [Wroclaw Devops Meetup](https://www.meetup.com/pl-PL/Wroclaw-DevOps-Meetup/events/255394680/) presentation and sample sceptre projects

- [Sceptre GitHub project](https://github.com/cloudreach/sceptre)

- [Sceptre documentation](https://sceptre.cloudreach.com/latest/docs/)

## How to run the presentation?

Install [reveal-md](https://github.com/webpro/reveal-md) using [npm](https://www.npmjs.com/get-npm):
```
npm install -g reveal-md
```

Run:

```
reveal-md presentation/rule_the_aws.md
```

## How to use the example projects?

The easiest way to take advantage of the examples is to use [Vagrant](https://www.vagrantup.com/).
This will allow you to play with sceptre without the risk of altering your current computer setup.

Once installed, simply run `vagrant up` followed by `vagrant ssh` to access the Vagrant VM.

You will also need AWS access credentials. If you just want to play with the provided examples,
the best way is to simply spin up the attached [cloudformation template](/v1/0_initial_setup/templates/iam.yaml) inside a sandbox account (you can create one using [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_create.html)).
It will create a `sceptre` user with the required permissions. The access key id
and the secret access key will be available in the stack outputs.
**Note: the permissions there are too strict for real-world sceptre usage.**.

Inside the Vagrant VM create a file `~/.aws/config` with your credentials:
```
[profile sceptre_sandbox]
aws_access_key_id = AKIA...
aws_secret_access_key = OwQ...
```
Then navigate to either `/vagrant/v1` or `/vagrant/v2` for examples for sceptre v1 and v2
respectively.

Once there, run:
```pipenv shell```
to setup the virtual environment with the appropriate sceptre version.

**Now you can easily play with the provided sceptre projects!**

For instance:
```
vagrant@ubuntu-bionic:~$ cd /vagrant/v1
vagrant@ubuntu-bionic:/vagrant/v1$ pipenv shell
Launching subshell in virtual environment…
vagrant@ubuntu-bionic:/vagrant/v1$  . /home/vagrant/.local/share/virtualenvs/v1-jH8cTHgZ/bin/activate
(v1) vagrant@ubuntu-bionic:/vagrant/v1$ ls
0_initial_setup  1_basic_structure  2_resolvers  3_hooks  4_jinja  Pipfile  Pipfile.lock
(v1) vagrant@ubuntu-bionic:/vagrant/v1$ cd 1_basic_structure/
(v1) vagrant@ubuntu-bionic:/vagrant/v1/1_basic_structure$ tree
.
├── config
│   ├── config.yaml
│   ├── devaccount
│   │   └── eu-west-1
│   │       └── dummy.yaml
│   └── prodaccount
│       └── eu-west-1
│           ├── dummy.yaml
│           └── dummyB.yaml
└── templates
    └── dummy.yaml

6 directories, 5 files
(v1) vagrant@ubuntu-bionic:/vagrant/v1/1_basic_structure$ sceptre launch-env devaccount
[2018-11-25 21:12:00] - sceptre.stack - devaccount/eu-west-1/dummy - Launching stack
[2018-11-25 21:12:00] - sceptre.stack - devaccount/eu-west-1/dummy - Stack is in the PENDING state
[2018-11-25 21:12:00] - sceptre.stack - devaccount/eu-west-1/dummy - Creating stack
[2018-11-25 21:12:01] - sceptre.stack - 2018-11-25T21:12:00+00:00 devaccount/eu-west-1/dummy sceptre-1-devaccount-eu-west-1-dummy AWS::CloudFormation::Stack CREATE_IN_PROGRESS User Initiated
[2018-11-25 21:12:09] - sceptre.stack - 2018-11-25T21:12:05+00:00 devaccount/eu-west-1/dummy DummyResource AWS::CloudFormation::WaitConditionHandle CREATE_IN_PROGRESS
[2018-11-25 21:12:09] - sceptre.stack - 2018-11-25T21:12:05+00:00 devaccount/eu-west-1/dummy DummyResource AWS::CloudFormation::WaitConditionHandle CREATE_IN_PROGRESS Resource creation Initiated
[2018-11-25 21:12:09] - sceptre.stack - 2018-11-25T21:12:05+00:00 devaccount/eu-west-1/dummy DummyResource AWS::CloudFormation::WaitConditionHandle CREATE_COMPLETE
[2018-11-25 21:12:09] - sceptre.stack - 2018-11-25T21:12:07+00:00 devaccount/eu-west-1/dummy sceptre-1-devaccount-eu-west-1-dummy AWS::CloudFormation::Stack CREATE_COMPLETE
(v1) vagrant@ubuntu-bionic:/vagrant/v1/1_basic_structure$
(v1) vagrant@ubuntu-bionic:/vagrant/v1/1_basic_structure$
(v1) vagrant@ubuntu-bionic:/vagrant/v1/1_basic_structure$
(v1) vagrant@ubuntu-bionic:/vagrant/v1/1_basic_structure$ sceptre delete-env devaccount
[2018-11-25 21:12:42] - sceptre.stack - devaccount/eu-west-1/dummy - Deleting stack
[2018-11-25 21:12:42] - sceptre.stack - 2018-11-25T21:12:42+00:00 devaccount/eu-west-1/dummy sceptre-1-devaccount-eu-west-1-dummy AWS::CloudFormation::Stack DELETE_IN_PROGRESS User Initiated
[2018-11-25 21:12:46] - sceptre.stack - devaccount/eu-west-1/dummy - delete complete
(v1) vagrant@ubuntu-bionic:/vagrant/v1/1_basic_structure$ exit
vagrant@ubuntu-bionic:/vagrant/v1$
```

