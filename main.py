import json
import smtplib
from email.message import EmailMessage
import click
import os
import concurrent.futures
import functools


def send(from_addr, app_pass, to_addr, subject, content):

    print(f"Sending from {from_addr} to {to_addr}...")
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(from_addr, app_pass)

        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = from_addr
        msg["To"] = to_addr

        # content = "Hello this is a test!"
        msg.set_content(content)
        smtp.send_message(msg)


def bulk(from_addr, app_pass, to_list, subject, content, num_workers):

    tasks = []
    for _ in range(num_workers):
        try:
            to_addr = to_list.pop()
            tasks.append(functools.partial(send, to_addr=to_addr, from_addr=from_addr, app_pass=app_pass,
                                           subject=subject, content=content))
        except:
            break

    if len(tasks) == 0:
        return

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for task in tasks:
            future = executor.submit(task)
            futures.append(future)

    return bulk(from_addr, app_pass, to_list, subject, content, num_workers)


@click.command()
@click.argument("config_path", nargs=1, default=f"{os.getcwd()}/config.json")
@click.argument("content_path", nargs=1, default=f"{os.getcwd()}/content.txt")
def main(config_path, content_path):
    config = json.load(open(config_path))
    num_workers = min([config["num_workers"], len(config["to_list"])])

    bulk(
        from_addr=config["from_addr"],
        app_pass=config["app_pass"],
        to_list=config["to_list"],
        subject=config["subject"],
        content=open(content_path, "r").read(),
        num_workers=num_workers
    )


if __name__ == "__main__":
    main()


# basically just add to $PATH
# https://earthly.dev/blog/python-makefile/
# https://thoughtbot.com/upcase/videos/lets-build-a-cli

# you can just use shell script for install
# https://stackoverflow.com/questions/3798562/why-use-make-over-a-shell-script

# The only obvious alternative with a shell script is to rebuild everything every time. F

