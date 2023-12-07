import discord
from discord.ext import commands
from bot_mantik import *
import math
import os
import random
import requests
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba {bot.user}! Ben bir botum!')
    await ctx.send(f"Hoşgeldin {ctx.author}!") 
@bot.command()
async def heh(ctx, count_heh=5):
    await ctx.send("he" * count_heh)

@bot.command()
async def topla(ctx,*args):
    try:
        sonuc=sum(int(arg) for arg in args)
        #for arg in args:
        #    sonuc+=int(arg) 
        await ctx.send(sonuc)
    except:
        await ctx.send("Lütfen doğru bir değer girin.")
@bot.command()
async def cikarma(ctx,*args):
    s1=0
    try:
        for arg in args:
            s1=int(arg)
        await ctx.send(s1)
    except:
        await ctx.send("Lütfen doğru bir değer girin.")
@bot.command()
async def carpma(ctx,*args):
    s2=1
    try:
        for arg in args:
            s2*=int(arg)
        await ctx.send(s2)
    except:
        await ctx.send("Lütfen doğru bir değer girin.")
@bot.command()
async def bolme(ctx,s1=1,s2=1,s3=1,s4=1,s5=1,s6=1,s7=1,s8=1,s9=1,s10=1):
    await ctx.send(s1/s2/s3/s4/s5/s6/s7/s8/s9/s10)  
@bot.command()
async def faktoriyel(ctx,s1=0):
    await ctx.send(math.factorial(s1))
@bot.command()
async def kuvvet(ctx,s1=0,s2=0):
    await ctx.send(s1**s2)
@bot.command()
async def joined(ctx):
    await ctx.send(f"Hoşgeldin {ctx.author}!")
@bot.command()
async def sifre(ctx,uzunluk=10):
    await ctx.send(p_g(uzunluk))
@bot.command()
async def zamanlayici(ctx,sure=10):
    await ctx.send(z(sure))
@bot.command()
async def r_s_y(ctx,b=0,s=100):
    await ctx.send(r_s_u(b,s))
@bot.command()
async def karekok(ctx,s1=1):
    await ctx.send(math.sqrt(s1))
@bot.command()
async def EBOB(ctx,s1=1,s2=1):
    await ctx.send(math.gcd(s1,s2))
@bot.command()
async def EKOK(ctx,s1=1,s2=1):
    await ctx.send(math.lcm(s1,s2))
@bot.command()
async def y_h(ctx,s1=1,s2=1):
    await ctx.send(h_y(s1,s2))
@bot.command()
async def c_h(ctx,c=1):
    await ctx.send(math.pi*c)
@bot.command()
async def yazi_tura(ctx,c):
    if c=="Yazı" or c=="Tura":
        x=y_t()
        if x==c:
            await ctx.send(f"Doğru bildin {x} çıktı.")
        else:
            await ctx.send(f"Bilemedin {x} çıktı.")
    else:
         await ctx.send("Lütfen Yazı veya Tura girin.")   
@bot.command()
async def z_a(ctx):
    zar=[1,2,3,4]
    olasilik=[0.20,0.25,0.50,0.05]
    await ctx.send(random.choices(zar,weights=olasilik,k=1)[0])

baskentler={
    "Türkiye":"Ankara",
    "Fransa":"Paris",
    "Birleşik_Krallık":"Londra"
}
@bot.command()
async def baskent_b(ctx,cevap):
    embed=discord.Embed(title="Başkent",color=discord.Color.red())
    embed.add_field(name="a",value=f"{cevap} başkenti {baskentler[cevap]}")
    await ctx.send(embed=embed)

@bot.command()
async def sayi_b(ctx):
    e=random.randint(1,100)
    await ctx.send("1 ile 100 arasında bir sayı seçtim ve bilmek için 8 hakkınız var.")
    s=0
    while True:
        tahmin_mesaji = await bot.wait_for("message", check=lambda m: m.author == ctx.author)
        y=tahmin_mesaji.content
        try:
            y=int(y)
        except:
            await ctx.send("Lütfen sayı girin.")
            continue
        s+=1
        if e==y:
            await ctx.send("Kazandın!")
            break
        elif s==8:
            await ctx.send("Bilemediniz hakkınız doldu.")
            break
        elif e>y:
            await ctx.send("Daha büyük bir sayı tahmin et.")
        else:
            await ctx.send("Daha küçük bir sayı tahmin et.")
@bot.command()
async def mem(ctx):
    with open('resimler/TRmem3.jpg', 'rb') as f:
      
        picture = discord.File(f)

    await ctx.send(file=picture)    
@bot.command()
async def hayvan(ctx):
    h_s=random.choices(os.listdir("hayvanlar"),weights=[0.30,0.20,0.30,0.20])
    with open(f'hayvanlar/{h_s}', 'rb') as f:
      
        picture = discord.File(f)

    await ctx.send(file=picture)    

@bot.command()
async def p_dili(ctx):
    p_d_s=random.choice(os.listdir("p_dilleri"))
    with open(f'p_dilleri/{p_d_s}', 'rb') as f:
      
        picture = discord.File(f)

    await ctx.send(file=picture)    

@bot.command()
async def r_s(ctx):
    olasilik=[0.40,0.40,0.10,0.10]
    r_s=random.choices(os.listdir("resimler"),weights=olasilik,k=1)[0]
    with open(f'resimler/{r_s}', 'rb') as f:
      
        picture2 = discord.File(f)

    await ctx.send(file=picture2) 



def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)
def k_d():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command()
async def k_r(ctx):
    
    image_url = k_d()
    await ctx.send(image_url)


def t_d():    
    url = 'https://randomfox.ca/floof/'
    res = requests.get(url)
    data = res.json()
    return data['image']


@bot.command()
async def t_r(ctx):
    
    image_url = t_d()
    await ctx.send(image_url)

def r_p():
    r_s=random.randint(1,800)
    url = f'https://pokeapi.co/api/v2/pokemon/{r_s}'
    res = requests.get(url)
    data = res.json()
    return data["sprites"]["front_default"]
    
@bot.command()
async def p_r(ctx):
    await ctx.send(r_p())
    
bot.run("Lütfen tokeninizi buraya giriniz.")
