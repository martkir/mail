# mail

Simple application for sending automatic bulk email using **gmail** SMTP server.

## Getting Started

Run `./install.sh`.

Create Gmail **App Password**:

Creating an App Password requires you to have 2FA enabled.

- https://myaccount.google.com/security/signinoptions/two-step-verification

If you have 2FA click the link below to create an App Password:

- https://security.google.com/settings/security/apppasswords

## Sending Bulk Email

The command for sending bulk email is as follows.

```
./mail.sh config.json content.txt
```

- `config.json` use to specify form and who to send email to.
- `content.txt` what content of email should be.

`config.json` should look like:

```
{
  "from_addr": "email@gmail.com",
  "app_pass": "gmail app pass",
  "subject": "Test Email",
  "to_list": [
    "abc@gmail.com",
    "xyz@yahoo.com",
  ],
  "num_workers": 15
}
```

- `num_workers` how many emails to send in parallel.

`content.txt` example:

```
Hi,

Blah blah. Something something. This is a message.

Best,

A Name
```


