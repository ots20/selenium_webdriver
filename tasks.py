from invoke import task


@task
def run(context, tags="", browser=""):
    behave_cmd = "behave"
    if browser != "":
        behave_cmd = f"{behave_cmd} -D browser={browser}"
    if tags != "":
        behave_cmd = f"{behave_cmd} --tags={tags}"
    context.run(behave_cmd)


@task
def run_with_allure(context, tags="", browser=""):
    behave_cmd = "behave -f allure_behave.formatter:AllureFormatter -o artifacts -f pretty"
    if browser != "":
        behave_cmd = f"{behave_cmd} -D browser={browser}"
    if tags != "":
        behave_cmd = f"{tags} --tags={tags}"
    context.run(behave_cmd)
