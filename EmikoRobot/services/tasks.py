from asyncio import Lock, create_task
from time import time
from pyrogram import filters
from pyrogram.types import Message
from EmikoRobot import BOT_ID, BOT_USERNAME, DEV_USERS
from EmikoRobot.services.sections import bold, section, w

tasks = {}
TASKS_LOCK = Lock()
arrow = lambda x: (x.text if x else "") + "\n`→`"


def all_tasks():
    return tasks


async def add_task(
    taskFunc,
    task_name,
    *args,
    **kwargs,
):

    async with TASKS_LOCK:
        global tasks

        task_id = (list(tasks.keys())[-1] + 1) if tasks else 0

        task = create_task(
            taskFunc(*args, **kwargs),
            name=task_name,
        )
        tasks[task_id] = task, int(time())
    return task, task_id


async def rm_task(task_id=None):
    global tasks

    async with TASKS_LOCK:
        for key, value in list(tasks.items()):
            if value[0].done() or value[0].cancelled():
                del tasks[key]

        if (task_id is not None) and (task_id in tasks):
            task = tasks[task_id][0]

            if not task.done():
                task.cancel()

            del tasks[task_id]


async def _get_tasks_text():
    await rm_task()  # Clean completed tasks
    if not tasks:
        return f"{arrow('')} No pending task"

    text = bold("Tasks") + "\n"

    for i, task in enumerate(list(tasks.items())):
        indent = w * 4

        t, started = task[1]
        elapsed = round(time() - started)
        info = t._repr_info()

        id = task[0]
        text += section(
            f"{indent}Task {i}",
            body={
                "Name": t.get_name(),
                "Task ID": id,
                "Status": info[0].capitalize(),
                "Origin": info[2].split("/")[-1].replace(">", ""),
                "Running since": f"{elapsed}s",
            },
            indent=8,
        )
    return text
