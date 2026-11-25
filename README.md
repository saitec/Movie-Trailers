<div align="center">

```
    🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅
    🍅                                                🍅
    🍅   ┌────────┐ ┌────────┐ ┌────────┐             🍅
    🍅   │ 🧟     │ │ 👍     │ │ 🦁     │  fresh      🍅
    🍅   │ WORLD  │ │ SOCIAL │ │ LION   │  tomatoes   🍅
    🍅   │ WAR Z  │ │NETWORK │ │ KING   │  ▶ play     🍅
    🍅   └────────┘ └────────┘ └────────┘             🍅
    🍅   ┌────────┐ ┌────────┐ ┌────────┐             🍅
    🍅   │ 🦇     │ │ 🪐     │ │ 🎩     │  my first   🍅
    🍅   │ DARK   │ │INTER-  │ │  THE   │  ever code  🍅
    🍅   │ KNIGHT │ │STELLAR │ │PRESTIGE│  (go easy)  🍅
    🍅   └────────┘ └────────┘ └────────┘             🍅
    🍅                                                🍅
    🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅
```

# 🍿 Movie Trailers

### *"this is my first shot at some code, so go easy on it. :)"*

**pushed: april 2016 · revived: november 2026 · where it all started**

*a [GitHub Run](https://github.com/saitec/github-run) revival by [sai](https://5aitec.com)*

</div>

---

> 🦕 **the oldest one.**
> this is the first repo i ever pushed. april 2016.
> a tiny Python project from Udacity's Intro to Programming Nanodegree.
> six movies. six posters. click one, watch the trailer.
> the original README said "this is my first shot at some code, so go easy on it."
> ten years later, i'm going easy on it. mostly. 😄
> the code is untouched. the old README is in [`README-2016.md`](README-2016.md).
> grab popcorn. this one's personal. 🍿

---

## 📍 tonight's programme

```
 1. 🎬  the trailer (the short version)
 2. 🎓  april 2016: learning to code online
 3. 🔧  the code: my first classes ever
 4. 🐛  the bugs 2016 me missed
 5. 🎞️  the six movies i picked (and what they say about me)
 6. 🌍  2016 → 2026: how the world changed
 7. 📺  how we watch movies now
 8. 🤖  AI goes to the movies
 9. 🛠️  what i'd build now
10. 📚  lessons from my first repo
11. 💌  p.s. (end credits)
```

---

## 🎬 1. the trailer (the short version)

A Python script.
It holds six movies as objects.
Each has a title, a storyline, a poster, and a trailer link.
Run it, and it writes a web page.
A grid of posters.
Click a poster. A popup plays the YouTube trailer. ▶️

That's it.
About ninety lines of my own Python.
The "hello world" of my coding life.
Everything since, every startup, every exit, every repo,
traces back to this one little grid of posters. 🌱

---

## 🎓 2. april 2016: learning to code online

Let me set the scene.

Online courses were booming.
Coursera, edX, Udacity, Khan Academy.
"Learn to code" was everywhere.
Udacity had "Nanodegrees".
Short, job-focused programs, often with real projects.
Their tagline energy was: anyone can learn this. 🚀

I joined Intro to Programming.
It walked you through HTML, CSS, and Python.
And this project was a big milestone in it.
Your first "real" Python program.
With classes. With objects. With a web page at the end.

```
   THE 2016 SELF-TAUGHT CODER PATH 🧭

   📺 watch a video
       │
       ▼
   ✍️ type along
       │
       ▼
   💥 error. copy it into Google.
       │
       ▼
   📚 Stack Overflow answer from 2011
       │
       ▼
   ✅ it works! no idea why.
       │
       ▼
   🔁 repeat 400 times
       │
       ▼
   🍿 a movie trailer website
```

Learning to code in 2016 had a specific feeling.
You'd follow a video perfectly, letter by letter.
And it still wouldn't run.
Turns out you typed a tab instead of four spaces.
Python cares. Python cares a lot. 🐍
Lonely at 1am. 🌙
Thrilling when something ran.
Confusing when it ran and you didn't know why.
The forums helped. Reviewers helped.
But mostly it was you, a video, and an error message.

---

## 🔧 3. the code: my first classes ever

Let's open the box. 📦

```
Movie-Trailers/
├── 🎬 main.py               ← the six movies + "make the page"
├── 🎞️ media.py              ← the Movie class (my first class!)
├── 🍅 fresh_tomatoes.py     ← writes the HTML page (from the course)
├── 🌐 fresh_tomatoes.html   ← the generated page
├── 📜 LICENSE
└── 📖 README.md             ← "go easy on it :)"
```

### 🎞️ media.py: my first class

```python
class Movie():
    def __init__(self, title, storyline, poster_image, trailer_video):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_video
```

My first class. Ever. 🥹
`Movie()` with empty brackets. Very beginner.
`__init__`, the magic setup function.
`self`, which confused me for weeks.
"Why do I have to write self everywhere?!" 😤

But look what it does.
It turns a movie into a *thing*.
A thing with properties.
That idea, objects that carry data, is everywhere in software.
Every app you use is built on it.
This was where I first got it.

### 🎬 main.py: the six movies

```python
__author__ = 'Sai'

from media import Movie
import fresh_tomatoes

world_war_z = Movie(
    'World War Z',
    'As the world is grasped by a mysterious infection...',
    'http://goo.gl/1pZBuW',
    'https://www.youtube.com/watch?v=HcwTxRuq-uk')
```

`__author__ = 'Sai'`. 🥹
Signing my first code like a painting.
Six movies, each built the same way.
Copy, paste, change the title, change the links.
Repetition is how you learn a pattern.
By movie six, I could write it with my eyes closed. 😌
Then one line at the bottom:
make the page and open it.

### 🍅 fresh_tomatoes.py: the page maker

This file came from the course.
It holds an HTML template.
Bootstrap for styling. jQuery for the popup.
It loops over the movies, fills in tiles, writes the file.
Then opens it in your browser.

```
   HOW THE PAGE GETS MADE 🏭

   🎬 Movie objects (main.py)
        │
        ▼
   🍅 fresh_tomatoes.open_movies_page(movies)
        │
        ├── 🧩 fill a tile per movie (poster + title)
        ├── 📄 stitch tiles into the HTML template
        ├── 💾 write fresh_tomatoes.html
        └── 🌐 open it in the browser
        │
        ▼
   🍿 click a poster → ▶️ YouTube trailer in a popup
```

Bootstrap and jQuery.
The two most 2016 web tools ever.
Every site used them.
Now? Most new projects use neither.
Frameworks rose. CSS got powerful. Browsers caught up.
But in 2016, Bootstrap + jQuery was the starter pack. 🎒

---

## 🐛 4. the bugs 2016 me missed

Okay. Code review time.
Ten years later. Kindly. 🫶

### 🐛 bug 1: the squished storylines

Look at this:

```python
'As the world is grasped by a mysterious infection that turns humans into zombies'
'Gerry, a former U.N. investigator has to leave his family'
'to determine the source of the infection',
```

Python joins strings that sit next to each other.
But it doesn't add spaces.
So this becomes:
`"...turns humans into zombiesGerry, a former U.N. investigator has to leave his familyto determine..."`

"zombiesGerry". 🧟‍♂️
"familyto".
Every storyline has these glued words.
2016 me never noticed, because the storyline didn't show on the page.
A silent bug. Living rent-free for a decade.
Thousands of people could have read it on GitHub.
Nobody filed an issue.
That's the internet's way of being polite. 😂

The fix is tiny:

```python
'...turns humans into zombies. '
'Gerry, a former U.N. investigator, has to leave his family '
'to determine the source of the infection.',
```

Add a space at the end of each line.
Ten years. One spacebar. ⌨️

### 🐛 bug 2: the shortened poster links

The posters use `goo.gl` links.
That was Google's link shortener.
Short. Neat. Very 2016.
Then Google wound the service down.
It stopped making new short links in 2019,
and later announced old links would stop working.
So some of these posters may not load anymore. 🖼️❌

Lesson: never store a link to a link.
Store the real address.
Shorteners are someone else's server.
Someone else's decision.

### 🐛 bug 3: "Python 3.x if running directly"

The README asks for Python 3.
That was actually forward-thinking!
In 2016, lots of people still used Python 2.
(My own college scripts that year were Python 2. 😅)
So 2016 me got this one right. 🏆

### 🐛 bug 4: no tests

Zero tests.
But for a first project? That's normal.
Nobody writes tests for their first poem either. 📝

---

## 🧰 bonus: the 2016 web toolbox, a museum tour

This project used the classic 2016 kit.
Let's walk the museum. 🏛️

**🅱️ Bootstrap.**
A CSS toolkit from Twitter's engineers.
Grids. Buttons. Navbars. Popups.
Every 2016 site looked a bit alike because of it.
Same rounded buttons. Same navbar. 😂
It's still around and still updated.
But it's no longer the default choice.

**💲 jQuery.**
The `$` sign that ruled the web.
It smoothed over browser differences.
Click handlers. Animations. Ajax calls.
Then browsers got consistent. JavaScript got better.
Most new projects don't need it now.
It's still on a huge number of old sites, quietly working.

**▶️ YouTube embeds.**
Paste a video ID into an iframe. Done.
This one barely changed in ten years.
Still the easiest way to put a video on a page.
Sometimes the oldest tools are the steadiest. 🪨

**🔗 goo.gl.**
Rest in peace. 🪦

**🐍 Python's built-in `webbrowser` module.**
The script opens the page for you with one line.
Still in Python today. Still delightful.

```
   2016 WEB KIT, WHERE ARE THEY NOW? 🔎

   🅱️ Bootstrap      → still alive, less default
   💲 jQuery         → retired from new projects, alive in old ones
   ▶️ YouTube embed  → basically unchanged 🪨
   🔗 goo.gl         → 🪦
   🐍 webbrowser     → still there, still cute
```

The pattern again:
platforms and standards last.
Libraries rotate.
Third-party shortcuts vanish.
Build on the boring, open stuff. 🧱

---

## 🎞️ 5. the six movies i picked (and what they say about me)

The course let you pick any movies.
These were mine:

```
   🎬 SAI'S 2016 MOVIE NIGHT

   🧟 World War Z          (2013)  zombies, a global crisis, a lone investigator
   👍 The Social Network   (2010)  a founder, a dorm room, a company that changed the world
   🦁 The Lion King        (1994)  the classic. no notes. 🥹
   🦇 The Dark Knight      (2008)  nolan
   🪐 Interstellar         (2014)  nolan
   🎩 The Prestige         (2006)  nolan
```

Three Christopher Nolan films out of six. 😂
I was clearly a Nolan kid.
Big ideas. Puzzles. Time. Obsession.
Honestly? Still am.

And look at the others.
A founder story.
A global crisis story.
A coming-of-age king story.
2016 me was telling you who he wanted to be.
I just didn't know it yet. 🪞

The Social Network especially.
A kid in a dorm builds something.
It grows bigger than anyone planned.
Friendships get tested. Lawyers show up. 😬
I watched it as a fun drama in 2016.
I watch it as a documentary-ish warning now.
Building companies is exactly that messy.
The code is the easy part.
People are the hard, beautiful part.

### 🎞️ what happened to those movies since

The world kept making movie history.

- 🦁 **The Lion King** got a photoreal CGI remake in 2019.
  Every animal looked real. Fully computer-made.
  A sign of where visual effects, and later AI video, were heading.
- 👍 **The Social Network**'s company renamed itself Meta in 2021.
  The movie's story got a very long sequel in real life.
- 🪐 **Nolan** made Oppenheimer in 2023.
  It won Best Picture at the Oscars in 2024.
  My 2016 taste, validated by the Academy. 😎
  Also: a three-hour film about physicists, a huge hit.
  Audiences wanted big ideas after all.
- 🧟 **Global crisis movies** hit different after 2020.
  Watching a pandemic movie after living through one? Oof.

---

## 🧑‍🏫 bonus: the "self" explanation i wish i had

I spent weeks confused by `self`.
So let me explain it the way 2016 me needed.
With movies. Obviously. 🍿

Imagine a cinema hall. 🎦
The `Movie` class is the *ticket template*.
It says every ticket has a title, a storyline, a poster, and a trailer.
But a template isn't a ticket.

When you write:

```python
interstellar = Movie('Interstellar', '...', poster, trailer)
```

you print a real ticket.
That ticket is an *object*.
Its title says "Interstellar". 🪐

Now, inside the class, the code needs to say
"put the title on *this* ticket".
Not every ticket. Not the template.
*This one.*
That's all `self` means.
"The ticket I'm currently printing." 🎟️

```
   CLASS vs OBJECT vs SELF 🎟️

   📄 class Movie         = the ticket template
   🎟️ interstellar         = one printed ticket
   👉 self                 = "this ticket, right now"

   self.title = title     → "write the title on THIS ticket"
```

Six movies. Six tickets. One template.
That's object-oriented programming in one cinema.

In 2026, a beginner asks an AI.
"Explain self like I'm at the movies."
And gets almost exactly this, in two seconds.
I got it after two weeks and four forum threads. 😂
Not bitter. Just jealous. 💚

---

## 🍿 bonus: movie night, 2016 vs 2026

Same friends. Same Saturday. Ten years apart.

### 🦕 2016

**7:00 pm.** Friends arrive. "What do we watch?" 🤔
**7:05.** Someone opens a laptop.
**7:10.** Debate. Comedy? Thriller? Nolan? (Always Nolan, if I'm there.)
**7:25.** Someone suggests a torrent. Someone else says no.
**7:30.** Check what's on a streaming app that just launched in India.
The catalogue is small.
**7:45.** Watch three trailers on YouTube. Buffering on 3G. 🐌
**8:00.** Finally pick a movie.
**8:05.** Laptop connected to TV with a cable that's slightly too short.
**8:10.** Movie starts. Everyone's on their phones by 8:40 anyway. 📱

### 🚀 2026

**7:00 pm.** Friends arrive. "What do we watch?" 🤔
**7:02.** Someone asks an AI:
"four people, one wants funny, one wants sci-fi, one wants short, one is me. go."
**7:03.** Six suggestions, with where to stream each.
**7:05.** Trailers play on the TV instantly. Vertical clips on phones too.
**7:08.** Quick vote. Winner picked.
**7:10.** Movie starts.
**7:40.** Everyone's on their phones anyway. 📱

Some things never change. 😂

The decision got faster.
The streaming got smoother.
The catalogue got bigger.
But "what do we watch?" is still the hardest question on a Saturday.
And phones still win the attention war by minute thirty.

That's the honest truth about tech.
It fixes the friction.
It doesn't fix humans. 🫶

---

## 🌍 6. 2016 → 2026: how the world changed

Okay. The big zoom out.

```
   2016                                         2026
    │                                             │
 🎓 learn to code from videos  ─────────►  🤖 learn to code with an AI tutor
 📚 Stack Overflow for errors  ─────────►  🤖 ask the AI. it explains + fixes.
 🍅 Bootstrap + jQuery          ────────►  ⚛️ frameworks, modern CSS, AI builders
 🔗 goo.gl short links          ────────►  🪦 goo.gl wound down
 📺 cable TV + early streaming  ────────►  📱 streaming everywhere, on phones
 🎟️ theatres are the default    ────────►  🏠 home first, theatres for events
 🎞️ VFX = huge studios          ────────►  🤖 AI video tools for everyone
 😷 "pandemic" = a zombie movie  ───────►  😷 we lived through one
```

### 🎓 learning to code changed completely

In 2016, you learned alone with videos and forums.
In 2026, you learn with an AI sitting next to you.
"Why is `self` needed?"
It explains. With an analogy. With your code.
"Why does my storyline say zombiesGerry?"
It spots the missing space in a second. 🔍

Udacity itself became part of Accenture in 2024.
The online course boom matured.
Some platforms grew. Some merged. Some faded.
And AI tutors changed what a course even is.

### 💻 what "a first project" looks like now

2016 first project: a static page with six movies.
2026 first project: often an app with an AI model inside.
"A movie recommender that chats with you."
"A trailer summariser."
The floor rose a lot.
Beginners now build what pros built ten years ago.
That's thrilling.
It also means beginners skip some fundamentals.
The AI writes the class. They never wrestle with `self`.
I think the wrestling matters.
So my advice below says: type it yourself, at least once.

### 😷 the pandemic hit theatres hard

In 2020, theatres closed.
Big movies moved release dates again and again.
Some went straight to streaming.
People got used to new films at home.
Theatres came back, but differently.
Big event films still pull crowds. 🎟️
Smaller films often live on streaming now.

---

## 📺 7. how we watch movies now

This repo is literally a trailer browser.
So let's talk about watching.

### 🇮🇳 2016 was a turning point in India

Netflix launched in India in January 2016.
Amazon Prime Video followed later that year.
Local streaming apps were growing too.
And cheap 4G data arrived at the end of 2016.
That combo changed everything.
Suddenly, a phone was a cinema. 📱🎬

### 📱 streaming everywhere

By 2026:
- Most movie watching in many homes happens on streaming.
- Phones are a main screen for lots of people.
- Trailers drop on social media first. Vertical cuts. 📱
- Recommendations are personalised by algorithms.

```
   HOW YOU FIND A MOVIE 🔍

   2016:  📰 reviews + 📺 TV ads + 🍅 a trailer site (like mine!)
   2026:  🤖 your app recommends · 📱 a clip in your feed · 💬 a friend's DM
```

### 🍅 the "trailer site" idea went mainstream

My little grid of posters?
That's basically what every streaming app's home screen is.
Rows of posters. Click one. A trailer autoplays.
2016 me built a baby Netflix home page.
Without knowing it. 😂

---

## 🤖 8. AI goes to the movies

This part is wild.

### 🎞️ AI makes video now

In 2016, making a trailer needed a studio.
Editors. Footage. Music. Weeks of work.
In 2026, AI video models make clips from text.
Sora. Veo. Kling. Seedance. MiniMax. More.
Some shots look like real cinema.

At ShopOS, our Sloosh platform makes ad videos for brands this way.
Product in. Prompt in. Video out. 🎬
That's my day job now.
Ten years after building a page that *played* trailers,
I help build tools that *make* them.

### 🎭 the fake trailer flood

There's a funny side effect.
YouTube filled up with AI-made fake trailers.
"Concept trailers" for movies that don't exist.
Some get millions of views.
Fans sometimes can't tell real from fake.
Studios and platforms had to respond.
Labels. Rules. Takedowns.

### 🧑‍🎨 what this means for filmmaking

Big studios use AI in effects, editing, dubbing.
Indie creators make short films alone.
Actors and writers pushed for protections.
Strikes in 2023 had AI on the table.
The debate isn't settled.
How do we use these tools without hurting the people who make art?
That's one of the real questions of this decade.

```
   VIDEO, 2016 → 2026 🎬

   2016:  🎥 cameras  →  ✂️ editors  →  🎞️ trailer  →  🍅 my grid
   2026:  ✍️ prompts  →  🤖 models   →  🎞️ clips    →  📱 everyone's feed
                 + 🎥 cameras still matter. a lot. (real > fake)
```

My personal rule for my own reels?
Real footage first.
AI only where it truly adds something.
Audiences can feel the difference.
And the real stuff ages better. 🍷

That's also why this GitHub Run exists in public.
Real code. Real fixes. Real notes from real days.
AI helps me write and check.
But the work underneath has to be true.
Otherwise it's just another fake trailer. 🎭

---

## 🛠️ 9. what i'd build now

If 2026 me rebuilt this first project.
Same spirit. New tools.

### 🎯 the idea: "trailer night"

A tiny web app for picking a movie with friends.
Fun. Fast. A bit silly. 🎉

```
   TRAILER NIGHT, 2026 🍿

   👥 3 friends join a link
         │
         ▼
   🗳️ each picks a mood: "funny" "mind-bending" "cry"
         │
         ▼
   🤖 AI suggests 6 movies that fit everyone
         │
         ▼
   🍅 a poster grid (hello, 2016 😊)
         │
         ▼
   ▶️ trailers play. everyone votes 👍👎
         │
         ▼
   🏆 winner! plus where to stream it
```

### 🧰 the parts

- **Python, still.** For old times' sake. 🐍
- **A small web frontend.** Modern, fast, phone-first.
- **An AI recommender.** Reads moods, mixes tastes.
- **Real trailers from official sources.** No fakes.
- **Real poster URLs.** No shorteners. Never again. 🔗
- **Tests.** Including one that checks storylines for "zombiesGerry". 😂

### 🎓 and a teaching version

I'd also make it a beginner tutorial.
"Build your first app with an AI tutor."
Same Movie class. Same grid.
But with an AI explaining every line as you go.
The course I wish I had in 2016. 🫶

---

## 🛤️ bonus: from a poster grid to four exits

People ask how you go from "first Python class" to building companies.
Honestly? One small project at a time.
This repo was step one.
The rest, roughly, in order of vibes:

```
   THE ROAD FROM THIS REPO 🛤️

   🍅 Movie-Trailers          first python. first class. first README.
     │
   📚 college scripts         scrapers, paper downloaders, small tools
     │
   🥽 VR & AR experiments      foveation, 360 video, A-Frame scenes
     │
   🏢 Scapic                  no-code AR/VR → acquired by Flipkart
     │
   🎨 Cope.Studio             creative tech → acquired by Polygon
     │
   🧰 Reality Tools           spatial tools → acquired by MotionPage
     │
   🔐 Dehidden                → acquired by Layer-E
     │
   🎓 Stanford GSB            went back to school. twice. 🌲
     │
   🛍️ ShopOS                  AI for commerce. building now.
     │
   👓 SeeIt                   open-source AI glasses. building now.
     │
   🏃 GitHub Run              and now, every day, in public.
```

None of those would exist without the habit this repo started.
Make a thing. Push it. Learn. Make the next thing.
The poster grid wasn't the point.
The habit was.

And look at the throughline.
Video, then 3D, then AI, then video again.
I built a page that *showed* trailers.
Then tools that *rendered* worlds.
Now tools that *make* the videos.
Same obsession. Ten years of upgrades. 🎞️

---

## 🧠 bonus: if you're starting today

My advice to a 2026 beginner. Short version.

- 🐍 **Pick one language and finish one project.** Python is still a great first pick.
- 🤖 **Use AI as a tutor, not a ghostwriter.** Ask it to explain. Then type it yourself.
- 🍿 **Build something about what you love.** I picked movies. Pick football, food, music, anything.
- 🐛 **Read your output.** "zombiesGerry" is waiting in your code too.
- 🔗 **Store real links.** Shorteners die. 🪦
- 🐙 **Push it public.** Even if it's tiny. Especially if it's tiny.
- ✍️ **Write a kind README.** "Go easy on it" is a perfectly good opener.
- 📅 **Come back in ten years.** Read it. Laugh. Feel proud. 🥹

---

## 📚 10. lessons from my first repo

What does your first ever code teach you, ten years on?

**1. Start small. Start anyway.** 🌱
Six movies. A grid. A popup.
That's all it was.
It's where everything started.
Your first thing doesn't need to matter. It needs to exist.

**2. Sign your work.** ✍️
`__author__ = 'Sai'`.
Owning it felt silly then.
It feels important now.
Put your name on what you make.

**3. Spaces matter.** ⌨️
"zombiesGerry" lived for ten years.
Tiny bugs hide in plain sight.
Read your output, not just your code.

**4. Don't trust someone else's shortcut.** 🔗
goo.gl went away.
Your links went with it.
Own the important stuff.

**5. Your taste is a clue.** 🪞
A founder movie. A crisis movie. Three Nolan puzzles.
2016 me picked stories about building, solving, and surviving.
Pay attention to what you're drawn to.
It's telling you something.

**6. "Go easy on it" is a great README line.** 🙏
Humble. Honest. Inviting.
Beginners should say it.
Experts should say it more often too.

**7. The thing you play with becomes the thing you build.** 🔁
I built a page that played trailers.
Now I build tools that make videos.
The toy was a preview. 🎞️

**8. Ten years is short and long.** ⏳
Short, because this code feels like yesterday.
Long, because the world it ran in is gone.
Cable TV, goo.gl, jQuery, 3G buffering.
The next ten will move even faster.
Write things down. Push them. Future you wants the receipts.

---

## 🗺️ the cheat sheet

| | 2016 🦕 | 2026 🚀 |
|---|---|---|
| 🎓 learning to code | videos + forums, alone at 1am | an AI tutor, any time |
| 🧰 web starter pack | Bootstrap + jQuery | modern frameworks + CSS |
| 🔗 short links | goo.gl, everywhere | goo.gl wound down. store real URLs. |
| 📺 watching movies | TV, theatres, early streaming | streaming first, phones everywhere |
| 🎞️ making trailers | studios + editors | studios + editors + AI tools |
| 🍅 a poster grid | my first project | every streaming app's home screen |
| 🎬 sai's job | watching trailers | building tools that make video |
| 😄 README vibe | "go easy on it :)" | still going easy on it |

---

## 🏃 run it (it should still work!)

This one is simple Python 3.
Good chance it runs.

```bash
git clone https://github.com/saitec/Movie-Trailers
cd Movie-Trailers
python3 main.py      # a browser tab opens with six posters 🍿
```

Some posters may not load (thanks, goo.gl 🪦).
The trailers should still play from YouTube.
And if you open `main.py`,
look for "zombiesGerry". 🧟‍♂️
It's my little easter egg now.

---

## 💌 11. p.s. (end credits)

```
   🎬  E N D   C R E D I T S  🎬

   written by ................. sai, age: young, very
   directed by ................ udacity's intro to programming
   page template .............. fresh_tomatoes.py (the course)
   styling .................... bootstrap, jquery, 2016 vibes
   special thanks ............. stack overflow, at 1am
   bug in a supporting role ... "zombiesGerry"
   revived by ................. sai + claude, ten years later
```

To 2016 me:
You wrote "go easy on it."
I will.
You wrote your first class, signed it, and shipped it.
That's more than most people ever do.
Everything after started with this grid of posters. 🍿

To anyone pushing their first repo today:
It's going to look silly in ten years.
Good. That means you grew.
The cringe is the proof.
No cringe, no growth. 📈
Push it anyway. Sign it. Go easy on yourself.

And if you want to talk movies, video, or your first project,
come say hi at [@5aitec](https://x.com/5aitec) or [5aitec.com](https://5aitec.com).
Nolan recommendations welcome. 🪐🎩🦇

---

<div align="center">

```
   2016:  🍅 "this is my first shot at some code, so go easy on it. :)"
   2026:  🎬 still shipping. still going easy. still a nolan kid.
   ──────────────────────────────────────────────────────────────
                     where it all started. 🌱
```

*part of the [GitHub Run](https://github.com/saitec/github-run): one fix, one insight, every day.*

</div>
