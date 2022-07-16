import traceback

from EmikoRobot import pbot as app
from EmikoRobot.utils.pluginhelper import fetch
from EmikoRobot.utils.inlinefuncs import *

__MODULE__ = "Inline"
__HELP__ = """See inline for help related to inline"""


@app.on_inline_query()
async def inline_query_handler(client, query):
    try:
        text = query.query.strip().lower()
        answers = []
        if text.strip() == "":
            answerss = await inline_help_func(__HELP__)
            await client.answer_inline_query(query.id, results=answerss, cache_time=10)
        elif text.split()[0] == "alive":
            answerss = await alive_function(answers)
            await client.answer_inline_query(query.id, results=answerss, cache_time=10)
        elif text.split()[0] == "tr":
            if len(text.split()) < 3:
                return await client.answer_inline_query(
                    query.id,
                    results=answers,
                    switch_pm_text="Translator | tr [LANG] [TEXT]",
                    switch_pm_parameter="inline",
                )
            lang = text.split()[1]
            tex = text.split(None, 2)[2].strip()
            answerss = await translate_func(answers, lang, tex)
            await client.answer_inline_query(
                query.id,
                results=answerss,
            )
        elif text.split()[0] == "ud":
            if len(text.split()) < 2:
                return await client.answer_inline_query(
                    query.id,
                    results=answers,
                    switch_pm_text="Urban Dictionary | ud [QUERY]",
                    switch_pm_parameter="inline",
                )
            tex = text.split(None, 1)[1].strip()
            answerss = await urban_func(answers, tex)
            await client.answer_inline_query(
                query.id,
                results=answerss,
            )
        elif text.split()[0] == "google":
            if len(text.split()) < 2:
                return await client.answer_inline_query(
                    query.id,
                    results=answers,
                    switch_pm_text="Google Search | google [QUERY]",
                    switch_pm_parameter="inline",
                )
            tex = text.split(None, 1)[1].strip()
            answerss = await google_search_func(answers, tex)
            await client.answer_inline_query(
                query.id,
                results=answerss,
            )

        elif text.split()[0] == "paste":
            if len(text.split()) < 2:
                return await client.answer_inline_query(
                    query.id,
                    results=answers,
                    switch_pm_text="paste | paste [TEXT]",
                    switch_pm_parameter="inline",
                )
            tex = text.split(None, 1)[1].strip()
            answerss = await paste_func(answers, tex)
            await client.answer_inline_query(query.id, results=answerss, cache_time=2)

        elif text.split()[0] == "wall":
            if len(text.split()) < 2:
                return await client.answer_inline_query(
                    query.id,
                    results=answers,
                    is_gallery=True,
                    switch_pm_text="Wallpapers Search | wall [QUERY]",
                    switch_pm_parameter="inline",
                )
            tex = text.split(None, 1)[1].strip()
            answerss = await wall_func(answers, tex)
            await client.answer_inline_query(query.id, results=answerss, cache_time=2)

        elif text.split()[0] == "saavn":
            if len(text.split()) < 2:
                return await client.answer_inline_query(
                    query.id,
                    results=answers,
                    switch_pm_text="saavn Search | saavn [QUERY]",
                    switch_pm_parameter="inline",
                )
            tex = text.split(None, 1)[1].strip()
            answerss = await saavn_func(answers, tex)
            await client.answer_inline_query(query.id, results=answerss)

        elif text.split()[0] == "torrent":
            if len(text.split()) < 2:
                return await client.answer_inline_query(
                    query.id,
                    results=answers,
                    switch_pm_text="Torrent Search | torrent [QUERY]",
                    switch_pm_parameter="inline",
                )
            tex = text.split(None, 1)[1].strip()
            answerss = await torrent_func(answers, tex)
            await client.answer_inline_query(
                query.id,
                results=answerss,
            )

        elif text.split()[0] == "yt":
            if len(text.split()) < 2:
                return await client.answer_inline_query(
                    query.id,
                    results=answers,
                    switch_pm_text="YouTube Search | yt [QUERY]",
                    switch_pm_parameter="inline",
                )
            tex = text.split(None, 1)[1].strip()
            answerss = await youtube_func(answers, tex)
            await client.answer_inline_query(query.id, results=answerss)

        elif text.split()[0] == "lyrics":
            if len(text.split()) < 2:
                return await client.answer_inline_query(
                    query.id,
                    results=answers,
                    switch_pm_text="Lyrics Search | lyrics [QUERY]",
                    switch_pm_parameter="inline",
                )
            tex = text.split(None, 1)[1].strip()
            answerss = await lyrics_func(answers, tex)
            await client.answer_inline_query(query.id, results=answerss)

        elif text.split()[0] == "search":
            if len(text.split()) < 2:
                return await client.answer_inline_query(
                    query.id,
                    results=answers,
                    switch_pm_text="Global Message Search. | search [QUERY]",
                    switch_pm_parameter="inline",
                )
            user_id = query.from_user.id
            tex = text.split(None, 1)[1].strip()
            answerss = await tg_search_func(answers, tex, user_id)
            await client.answer_inline_query(query.id, results=answerss, cache_time=2)

        elif text.split()[0] == "music":
            if len(text.split()) < 2:
                return await client.answer_inline_query(
                    query.id,
                    results=answers,
                    switch_pm_text="Music Search | music [QUERY]",
                    switch_pm_parameter="inline",
                )
            tex = text.split(None, 1)[1].strip()
            answerss = await music_inline_func(answers, tex)
            await client.answer_inline_query(query.id, results=answerss, cache_time=2)

        elif text.split()[0] == "wiki":
            if len(text.split()) < 2:
                return await client.answer_inline_query(
                    query.id,
                    results=answers,
                    switch_pm_text="Wikipedia | wiki [QUERY]",
                    switch_pm_parameter="inline",
                )
            tex = text.split(None, 1)[1].strip()
            answerss = await wiki_func(answers, tex)
            await client.answer_inline_query(query.id, results=answerss, cache_time=2)

        elif text.split()[0] == "speedtest":
            answerss = await speedtest_init(query)
            return await client.answer_inline_query(
                query.id, results=answerss, cache_time=2
            )
        elif text.split()[0] == "gh":
            if len(text.split()) < 2:
                return await client.answer_inline_query(
                    query.id,
                    results=answers,
                    switch_pm_text="gh | gh [USERNAME]",
                    switch_pm_parameter="inline",
                )
            results = []
            gett = text.split(None, 1)[1]
            text = gett + ' "site:github.com"'
            gresults = await GoogleSearch().async_search(text, 1)
            result = ""
            for i in range(4):
                try:
                    title = gresults["titles"][i].replace("\n", " ")
                    source = gresults["links"][i]
                    description = gresults["descriptions"][i]
                    result += f"[{title}]({source})\n"
                    result += f"`{description}`\n\n"
                except IndexError:
                    pass
            results.append(
                InlineQueryResultArticle(
                    title=f"Results for {gett}",
                    description=f" Github info of {title}\n  Touch to read",
                    input_message_content=InputTextMessageContent(
                        result, disable_web_page_preview=True
                    ),
                )
            )
            await client.answer_inline_query(query.id, cache_time=0, results=results)

        elif text.split()[0] == "ping":
            answerss = await ping_func(answers)
            await client.answer_inline_query(query.id, results=answerss, cache_time=2)

        elif text.split()[0] == "ytmusic":
            if len(text.split()) < 2:
                return await client.answer_inline_query(
                    query.id,
                    results=answers,
                    switch_pm_text="YT Music | ytmusic [url]",
                    switch_pm_parameter="inline",
                )
            tex = query.query.split(None, 1)[1].strip()
            answerss = await yt_music_func(answers, tex)
            await client.answer_inline_query(query.id, results=answerss, cache_time=2)
        elif text.split()[0] == "webss":
            if len(text.split()) < 2:
                return await client.answer_inline_query(
                    query.id,
                    results=answers,
                    switch_pm_text="webss | webss [url]",
                    switch_pm_parameter="inline",
                )
            tex = text.split(None, 1)[1].strip()
            answerss = await webss(tex)
            await client.answer_inline_query(query.id, results=answerss, cache_time=2)

        elif text.split()[0] == "info":
            if len(text.split()) < 2:
                return await client.answer_inline_query(
                    query.id,
                    results=answers,
                    switch_pm_text="User Info | info [USERNAME|ID]",
                    switch_pm_parameter="inline",
                )
            tex = text.split()[1].strip()
            answerss = await info_inline_func(answers, tex)
            await client.answer_inline_query(query.id, results=answerss, cache_time=2)

        elif text.split()[0] == "tmdb":
            if len(text.split()) < 2:
                answerss = await tmdb_func(answers, "")
                return await client.answer_inline_query(
                    query.id,
                    results=answerss,
                    switch_pm_text="TMDB Search | tmdb [QUERY]",
                    switch_pm_parameter="inline",
                )
            tex = text.split()[1].strip()
            answerss = await tmdb_func(answers, tex)
            await client.answer_inline_query(query.id, results=answerss, cache_time=2)
        elif text.split()[0] == "pokedex":
            if len(text.split()) < 2:
                await client.answer_inline_query(
                    query.id,
                    results=answers,
                    switch_pm_text="Pokemon [text]",
                    switch_pm_parameter="pokedex",
                )
                return
            pokedex = text.split(None, 1)[1].strip()
            Pokedex = await pokedexinfo(answers, pokedex)
            await client.answer_inline_query(query.id, results=Pokedex, cache_time=2)
        elif text.split()[0] == "paste":
            tex = text.split(None, 1)[1]
            answerss = await paste_func(answers, tex)
            await client.answer_inline_query(query.id, results=answerss, cache_time=2)

        elif text.split()[0] == "fakegen":
            results = []
            fake = Faker()
            name = str(fake.name())
            fake.add_provider(internet)
            address = str(fake.address())
            ip = fake.ipv4_private()
            cc = fake.credit_card_full()
            email = fake.ascii_free_email()
            job = fake.job()
            android = fake.android_platform_token()
            pc = fake.chrome()
            res = f"<b><u> Fake Information Generated</b></u>\n<b>Name :-</b><code>{name}</code>\n\n<b>Address:-</b><code>{address}</code>\n\n<b>IP ADDRESS:-</b><code>{ip}</code>\n\n<b>credit card:-</b><code>{cc}</code>\n\n<b>Email Id:-</b><code>{email}</code>\n\n<b>Job:-</b><code>{job}</code>\n\n<b>android user agent:-</b><code>{android}</code>\n\n<b>Pc user agent:-</b><code>{pc}</code>"
            results.append(
                InlineQueryResultArticle(
                    title="Fake infomation gathered",
                    description="Click here to see them",
                    input_message_content=InputTextMessageContent(
                        res, parse_mode="HTML", disable_web_page_preview=True
                    ),
                )
            )
            await client.answer_inline_query(query.id, cache_time=0, results=results)

        elif text.split()[0] == "image":
            if len(text.split()) < 2:
                return await client.answer_inline_query(
                    query.id,
                    results=answers,
                    is_gallery=True,
                    switch_pm_text="Image Search | image [QUERY]",
                    switch_pm_parameter="inline",
                )
            tex = text.split(None, 1)[1].strip()
            answerss = await image_func(answers, tex)
            await client.answer_inline_query(
                query.id, results=answerss, cache_time=3600
            )

        elif text.split()[0] == "exec":
            await execute_code(query)

        elif text.strip() == "tasks":
            user_id = query.from_user.id
            answerss = await task_inline_func(user_id)
            await client.answer_inline_query(query.id, results=answerss, cache_time=1)

    except Exception as e:
        e = traceback.format_exc()
        print(e, " InLine")
