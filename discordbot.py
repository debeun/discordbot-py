import discord
from discord.ext import commands

# 봇 설정
bot = commands.Bot(command_prefix='*')  # 봇의 명령 접두사를 '*'로 설정합니다.

# 봇이 준비되었을 때 실행되는 이벤트
@bot.event
async def on_ready():
    print(f'봇이 준비되었습니다: {bot.user.name}')

# 관리자만 해당 명령어를 사용할 수 있도록 체크하는 함수
def is_admin(ctx):
    return ctx.author.guild_permissions.administrator

# 임베드로 결과를 표시하는 함수
async def show_result(ctx, member, message):
    embed = discord.Embed(title=message, color=0x00ff00)  # 임베드 생성
    embed.set_author(name=member.name, icon_url=member.avatar_url)  # 봇 이름과 아이콘 설정

    await ctx.send(embed=embed)  # 임베드를 보내기

# 역할을 추가하는 함수
async def add_role(ctx, member, role_id, role_name):
    role = ctx.guild.get_role(role_id)
    if role in member.roles:
        await show_result(ctx, member, f"✖️이미 있는 역할입니다.✖️")
    else:
        await member.add_roles(role)
        await show_result(ctx, member, f"✅{role_name} 지급 완료")

# 역할을 제거하는 함수
async def remove_role(ctx, member, role_id, role_name):
    role = ctx.guild.get_role(role_id)
    if role not in member.roles:
        await show_result(ctx, member, f"✖️{role_name} 역할이 없습니다.✖️")
    else:
        await member.remove_roles(role)
        await show_result(ctx, member, f"✖️{role_name} 역할을 뺏습니다!✖️")

# 명령어 목록을 임베드로 출력
@bot.command()
async def 명령어(ctx):
    embed = discord.Embed(title="명령어 목록", color=0x3498db)
    embed.add_field(name="*role베이직", value="베이직 역할을 추가합니다.", inline=False)
    embed.add_field(name="*no베이직", value="베이직 역할을 제거합니다.", inline=False)
    embed.add_field(name="*role프리미엄", value="프리미엄 역할을 추가합니다.", inline=False)
    embed.add_field(name="*no프리미엄", value="프리미엄 역할을 제거합니다.", inline=False)
    embed.add_field(name="*roleLegend", value="레전드 역할을 추가합니다.", inline=False)
    embed.add_field(name="*no레전드", value="레전드 역할을 제거합니다.", inline=False)
    embed.add_field(name="*role블랙리스트", value="블랙리스트 역할을 추가합니다.", inline=False)
    embed.add_field(name="*no블랙리스트", value="블랙리스트 역할을 제거합니다.", inline=False)
    await ctx.send(embed=embed)

# 잘못된 명령어 처리
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await show_result(ctx, ctx.author, f"✖️{ctx.message.content} 명령어가 존재하지 않아요!✖️")

# !role베이직 명령어 처리
@bot.command()
@commands.check(is_admin)
async def role베이직(ctx, member: discord.Member):
    role_id = 1160559972376117361  # 역할 아이디를 여기에 입력
    await add_role(ctx, member, role_id, "베이직")

# !no베이직 명령어 처리
@bot.command()
@commands.check(is_admin)
async def no베이직(ctx, member: discord.Member):
    role_id = 1160559972376117361  # 역할 아이디를 여기에 입력
    await remove_role(ctx, member, role_id, "베이직")

# !role프리미엄 명령어 처리
@bot.command()
@commands.check(is_admin)
async def role프리미엄(ctx, member: discord.Member):
    role_id = 1160560356830228533  # 역할 아이디를 여기에 입력
    await add_role(ctx, member, role_id, "프리미엄")

# !no프리미엄 명령어 처리
@bot.command()
@commands.check(is_admin)
async def no프리미엄(ctx, member: discord.Member):
    role_id = 1160560356830228533  # 역할 아이디를 여기에 입력
    await remove_role(ctx, member, role_id, "프리미엄")

# !roleLegend 명령어 처리
@bot.command()
@commands.check(is_admin)
async def roleLegend(ctx, member: discord.Member):
    role_id = 1160560555648634951  # 역할 아이디를 여기에 입력
    await add_role(ctx, member, role_id, "레전드")

# !no레전드 명령어 처리
@bot.command()
@commands.check(is_admin)
async def no레전드(ctx, member: discord.Member):
    role_id = 1160560555648634951  # 역할 아이디를 여기에 입력
    await remove_role(ctx, member, role_id, "레전드")

# !role블랙리스트 명령어 처리
@bot.command()
@commands.check(is_admin)
async def role블랙리스트(ctx, member: discord.Member):
    role_id = 1160556167408406589  # 역할 아이디를 여기에 입력
    await add_role(ctx, member, role_id, "블랙리스트")

# !no블랙리스트 명령어 처리
@bot.command()
@commands.check(is_admin)
async def no블랙리스트(ctx, member: discord.Member):
    role_id = 1160556167408406589  # 역할 아이디를 여기에 입력
    await remove_role(ctx, member, role_id, "블랙리스트")

# 봇 토큰을 사용하여 봇을 실행합니다.
bot.run('MTE2MDU2MzIwMzEyNjg3MDA1Nw.GLK6CA.FdvBUo-_Ljberv9xoPCGFS6Gg22k3hKidM-0Ew')  # 봇 토큰을 여기에 입력합니다.
