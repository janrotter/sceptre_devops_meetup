## Rule the AWS with sceptre

![https://commons.wikimedia.org/wiki/File:Imperial_Crown_of_Austria_Globus_cruciger_Sceptre.jpg](images/sceptre_small.jpg)

Notes:
- Warm welcome in our office
- your presence is appreciated
- sceptre - a tool to drive cloudformation
- who the presentation is for? assume experience with AWS + CF
- how sceptre can enhance your experience with cloudformation

---

## Agenda

- About me
- A short story of failure
- How to use the sample projects
- Sceptre v1
- Sceptre v2 (RC)

Notes:
- Quickly introduce myself
- How I found sceptre
- Please interrupt me in case of any questions
---

## About me

<div style="display: flex; justify-content: center; align-items: center;">
<div style="flex: 1">
<p>Jan Rotter</p>
<p style="font-size: 20px;">jan.rotter@ocado.com</p>
</div>
<div style="flex: 1;">
![I have a beard!](images/jrotter.jpg) <!-- .element: style="width: 90%;" -->
</div>
<div style="flex: 1; font-size: 30px;">
DevOps @ Ocado Technology
</div>

Notes:
- *nix admin since my early teens
- DevOps for ~4-5 years

---

## A short story of failure

<div style="display: flex; justify-content: space-around; align-items: center;">
<div style="display: inline-block;">It all began with...</div>
![Ansible](images/ansible.png) <!-- .element: style="width: 10%; border: 0px; background: none; box-shadow: none;" class="fragment" -->
<div style="display: inline-block;">and</div>
![Windows](images/windows.png) <!-- .element: style="width: 10%; border: 0px; background: none; box-shadow: none;" class="fragment" -->
</div>

Notes:
- Snowflake servers
- Script everything!
- Ansible should be easier to maintain than pure Powershell, right?
- Scarce Ansible modules for windows
- Unreliable PowerShell Remoting
- Could be better, but it wasn't that bad after all

---

## What could possibly go wrong?

![https://commons.wikimedia.org/wiki/File:Paris_Tuileries_Garden_Facepalm_statue.jpg](images/facepalm.jpg) <!-- .element: style="width: 70%; border: 0px; background: none; box-shadow: none;" -->

Notes:
- Bugs in the ECS Ansible modules and the PR's not pulled in time
- Forked ansible
- Updating ansible is not trivial - no changesets, so the result is hard to predict
- April 5, 2017 - Host-based routing for the Application Load Balancers

---

## What are my options then?

<ul style="display: flex; justify-content: space-around; align-items: center; list-style: none;">
<li style="flex: 1; padding: 10px;">![Ansible](images/ansible.png) <!-- .element: style="width: 100%; border: 0px; background: none; box-shadow: none;" class="fragment fade-in-then-semi-out" -->
<li style="flex: 1; padding: 10px;">![Terraform](images/terraform.png) <!-- .element: style="width: 100%; border: 0px; background: none; box-shadow: none" class="fragment fade-in-then-semi-out" -->
<li style="flex: 1; padding: 10px; font-size: 50px; border: 4px solid #fff;  text-align: center;border: 0px; background: none; box-shadow: none" class="fragment fade-in-then-semi-out">Cloudformation
<li style="flex: 1; padding: 10px; font-size: 150px; border: 4px solid #fff; text-align: center; border: 0px; background: none; box-shadow: none" class="fragment fade-in-then-semi-out">_#!_
</ul>
<div class="fragment">
</div>

Notes:
- Ansible - ...
- Terraform
    - [+] Supports changesets
    - [+] Multi-cloud
    - [Cloudformation supports changesets since 29 MAR 2016](https://aws.amazon.com/blogs/aws/new-change-sets-for-aws-cloudformation/)
    - Hard to trust with version 0.11.10
    - I'm not a fan of the HCL syntax
    - We were AWS only anyway
    - Sharing the state
- CF
    - no structure / framework, so custom scripting needed
    - pure CF - felt like reinventing the wheel
- #!
    - bash? hard to maintain
    - python? aren't we going too far?

---

## Meet sceptre!
![http://artemisiasroyaljewels.blogspot.com/2013/01/cullinan-diamonds-cullinan-i-star-of.html](images/sceptre_photo.jpg) <!-- .element: style="width: 45%;" -->

Notes:
- Recommendation of a friend
- Basically what I needed and more
    - structure
    - jinja
    - hooks
    - can easily add already existing stacks
    - [*] no lock-in - just a wrapper, readable source

---

## Basic project structure

```nosyntax
.
├── config
│   ├── config.yaml
│   ├── devaccount
│   │   └── eu-west-1
│   │       └── dummy.yaml
│   └── prodaccount
│       └── eu-west-1
│           └── dummy.yaml
└── templates
    └── dummy.yaml
```
<!-- .element: style="border: 0px; box-shadow: none;" -->

---

## Demo 1 and sandbox intro

---

## Resolvers

![https://store.storeimages.cdn-apple.com/4981/as-images.apple.com/is/image/AppleInc/aos/published/images/p/ow/power/cables/power-cables-category-201610?wid=1440&hei=320&fmt=jpeg&qlt=95&op_usm=0.5,0.5&.v=1475790422131](images/cables.jpg) <!-- .element: style="width: 75%;" -->

Notes:
- Allow you to use any data source for your parameters
- Allows you to chain together the stacks
- Great for secrets!

---

## Demo 2

---

## Hooks

![https://www.amazon.com/Pro-Chef-Kitchen-Tools-Round/dp/B00OJJ2Z88](images/hooks.jpg) <!-- .element: style="width: 45%;" -->

Notes:
- Act on stack operations
- Can e.g. send Slack notifications for prod updates
- Can do post-provisioning configuration

---

## Demo 3

---

## Jinja2

![https://www.flickr.com/photos/dlato/5530553658/sizes/o/](images/ninja.jpg) <!-- .element: style="width: 45%;" -->

Notes:
- Solves the issue of dynamic value vs hardcoded one
- Control structures - if / for
- Macros
    - Helpful for e.g. ACL's
- includes - you can split your CF template into separate files

---

## Demo 4

---

## sceptre v2

![http://qrkoko.pl/craftmonday-7-new-is-always-better/](images/newisalwaysbetter.jpg) <!-- .element: style="width: 35%;" -->

Notes:
- Coming out soon!
- install with `pip install sceptre --pre`
- CLI redesigned
- improved dependency resolution
- easier resolvers sharing (installed with pip)
- [*] hopefully launch-env-cs equivalent

---

## sceptre v2 demo

---

## Not everything is perfect...

![http://www.kickvick.com/perfectionists-nightmare/](images/imperfect.jpg) <!-- .element: style="width: 45%;" -->

Notes:
- Cryptic error messages
- v2 not ready yet, better stick with the v1 until it's stable
- Build your solution incrementally to avoid issues
But...
- PR's welcome!

---

## Links

https://sceptre.cloudreach.com/dev/docs/index.html
https://github.com/cloudreach/sceptre

---

## Thank you!

Feedback? Questions?

jan.rotter@ocado.com

https://github.com/janrotter/sceptre_devops_meetup
