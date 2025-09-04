from typing import Any
from datetime import datetime

from playwright.async_api import async_playwright
import re


async def log_ps(login: str, password: str) -> bool:
    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            await page.goto("https://dnevnik.pravgym.ru/")
            await page.fill("input[name=login]", login)
            await page.fill("input[name=password]", password)
            await page.click("button[type=submit]")

            if await page.locator("text=Неверный логин или пароль").is_visible():
                return False

            await page.locator("tr").first.wait_for(timeout=3000)
            return True
    except Exception as e:
        print("Ошибка playwright:", e)
        return False


def rename_subject(subject):
    mapping = {
        "Основы православной веры": "ОПВ",
        "Физическая культура": "Физкультура",
        "Иностранный язык: Английский": "Английский",
        "Индивидуальный проект": "ИП",
        "Древние языки": "ДРЯ",
        "За страницами учебника русского языка": "Русский язык 2.0",
        "Церковно-славянский язык": "ЦСЯ/Литургика",
        "Основы безопасности и защиты Родины": "ОБЖ",
        "Алгебра и начала математического анализа": "Алгебра",
        "Избранные вопросы математики": "Профмат",
        "Вероятность и статистика": "Вероятность",
        "Избранные вопросы информатики": "Информатика проф",
    }
    if subject in mapping.keys():
        subject = mapping.get(subject)
    return subject


async def parse(login: str, password: str) -> list[list[str | int]]:
    array = await browser_connect(login, password)
    grades: list[list[str | int]] = []
    for row in array:
        try:
            date, subject, grade = row[0].split("\t")
            subject = rename_subject(subject)
            grades.append([date, subject, int(grade)])
        except ValueError:
            continue
    return grades


async def browser_connect(login: str, password: str):
    async with async_playwright() as p:
        date = get_trimestr()
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto("https://dnevnik.pravgym.ru/")

        await page.fill("input[name=login]", login)
        await page.fill("input[name=password]", password)
        await page.fill("input[name=date]", date)
        await page.click("button[type=submit]")

        await page.locator("tr").first.wait_for()
        rows = (await page.locator("tr").all())[1:]
        array = [await row.all_inner_texts() for row in rows]
        await browser.close()
        return array


async def parse_all(login: str, password: str) -> list[list[str | list[Any]]]:
    array = await browser_connect(login, password)

    index_start = array.index(["ПредметСр. баллОценки"])
    index_finish = array.index(["ПредметПериодОценка"])
    grades = array[index_start + 1 : index_finish]

    res_array: list[list[str | list[Any]]] = []
    for i in grades:
        text = i[0]
        lesson = re.match(r"\D*", text).group()
        lesson = rename_subject(lesson)
        bal_match = re.search(r"\d\.\d\d", text)
        bal = bal_match.group()
        marks = re.findall(r"\d+", text[bal_match.end() :])
        res_array.append([lesson, bal, marks])
    return res_array


def get_trimestr() -> str:
    today = datetime.now()
    current_year = today.year

    first_tr_date = datetime.strptime(f"{current_year}-09-01", "%Y-%m-%d")
    second_tr_date = datetime.strptime(f"{current_year}-11-18", "%Y-%m-%d")
    third_tr_date = datetime.strptime(f"{current_year+1}-02-23", "%Y-%m-%d")

    if today >= third_tr_date:
        return third_tr_date.strftime("%Y-%m-%d")
    elif today >= second_tr_date:
        return second_tr_date.strftime("%Y-%m-%d")
    elif today >= first_tr_date:
        return first_tr_date.strftime("%Y-%m-%d")
    else:
        return first_tr_date.strftime("%Y-%m-%d")
