import datetime

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm.attributes import flag_modified

import crypto
from core.models import Classes
from .schedule import get_schedule_with_class, RU_TO_EN_subjects, EN_TO_RU_subjects


async def get_all(session: AsyncSession) -> list[Classes]:
    stmt = select(Classes).order_by(Classes.class_name)
    result: Result = await session.execute(stmt)
    class_ = result.scalars().all()
    return list(class_)


async def get_classes(session: AsyncSession, class_name: str) -> Classes | None:
    return await session.get(Classes, class_name)


# class_name: Mapped[str] = mapped_column(unique=True)
#     schedule: Mapped[dict] = mapped_column(JSON)
#     homeworks: Mapped[dict] = mapped_column(JSON)
#     owner: Mapped[str]
#     admins: Mapped[list] = mapped_column(JSON)


async def create_info_class(
    session: AsyncSession, class_name: str, owner: str
) -> Classes:
    class_info = Classes(class_name=class_name, homeworks={}, owner=owner, admins=[])
    session.add(class_info)
    await session.commit()
    # await session.refresh(User)
    return class_info


async def check_admin(session: AsyncSession, class_name: str, email: str) -> int:
    class_ = await session.get(Classes, class_name)
    if len(email) == 344:
        email = crypto.unencrypt(email)

    return email == class_.owner or email in class_.admins


async def less_in_day(class_name: str, subject: str, weekday: str) -> int:
    schedule = get_schedule_with_class(class_name)
    subject = RU_TO_EN_subjects[subject]
    return int(subject in schedule[weekday])


async def add_hw(
    session: AsyncSession, class_name: str, subject: str, date: str, homework: str
) -> int:
    try:
        date_obj = datetime.datetime.strptime(date, "%d.%m.%Y")
        weekday = date_obj.strftime("%A").lower()
        subject = RU_TO_EN_subjects[subject]
        if not subject in get_schedule_with_class(class_name)[weekday]:
            return 0
        class_ = await session.get(Classes, class_name)
        homeworks = class_.homeworks
        if subject not in homeworks.keys():
            homeworks[subject] = {}
        if date not in homeworks[subject].keys():
            homeworks[subject][date] = []
        homeworks[subject][date].append(homework)
        class_.homeworks = homeworks
        flag_modified(class_, "homeworks")
        await session.commit()
        return 1
    except:
        return 0


async def get_hw(
    session: AsyncSession, class_name: str, date: str
) -> tuple[list, list, list]:
    weekday = datetime.datetime(
        int(date.split(".")[2]), int(date.split(".")[1]), int(date.split(".")[0])
    ).weekday()
    if weekday == 6:
        return ["нет предметов"], ["нет дз"], ["0:00\n1:10"]
    class_ = await session.get(Classes, class_name)
    day, month, year = map(int, date.split("."))
    weekday = datetime.date(year, month, day).strftime("%A").lower()
    schedule = get_schedule_with_class(class_name)
    lesson_times = [
        "08:10\n08:55",
        "09:10\n09:55",
        "10:05\n10:45",
        "11:00\n11:45",
        "11:55\n12:40",
        "13:00\n13:40",
        "14:00\n14:40",
        "14:45\n15:25",
    ]

    subjects = [EN_TO_RU_subjects[subject] for subject in schedule[weekday]]
    homeworks = [
        class_.homeworks.get(RU_TO_EN_subjects[subject], {}).get(date, "нет дз")
        for subject in subjects
    ]

    return subjects, homeworks, lesson_times


async def get_admins(session: AsyncSession, class_name: str) -> dict:
    class_ = await session.get(Classes, class_name)
    array = {"owner": class_.owner, "admins": class_.admins}
    return array


async def add_admin(session: AsyncSession, class_name: str, email: str) -> int:
    try:
        if len(email) == 344:
            email = crypto.unencrypt(email)
        class_ = await session.get(Classes, class_name)
        admins = class_.admins
        admins.append(email)
        class_.admins = admins
        flag_modified(class_, "admins")
        await session.commit()
        return 1
    except:
        return 0


async def del_admin(session: AsyncSession, class_name: str, email: str) -> int:
    try:
        if len(email) == 344:
            email = crypto.unencrypt(email)
        class_ = await session.get(Classes, class_name)
        admins = class_.admins
        admins.remove(email)
        class_.admins = admins
        flag_modified(class_, "admins")
        await session.commit()
        return 1
    except:
        return 0
