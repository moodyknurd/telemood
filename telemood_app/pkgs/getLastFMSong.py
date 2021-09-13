from typing import List 

async def get_last_song(telemood):
    last_song: str = (await telemood.get_inline_bot_results("lastfmrobot"))["results"][0]["send_message"]["message"]
    name_tokens: List[str] = (await telemood.get_me())["first_name"].split()
    if "is now listening to" in last_song:
        if not "🎵" in name_tokens:
            name_tokens.insert(0, "🎵")
            name_tokens.append( "🎵")
    else:
        if "🎵" in name_tokens:
            name_tokens: List[str] = list(name_tokens[1:-1])
    new_name = " ".join(name_tokens)
    await telemood.update_profile(first_name = new_name)
