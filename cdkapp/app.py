#!/usr/bin/env python3
import os

import aws_cdk as cdk

from cdkapp.cdkapp_stack import CdkappStack


app = cdk.App()
CdkappStack(app, "CdkappStack",

    # Specify ID of your account.
    env=cdk.Environment(account='123456789', region='us-east-1'),

    )

app.synth()
