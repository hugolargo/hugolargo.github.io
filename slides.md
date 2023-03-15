# Music of the Masses
<font color="#1DB954">Finding the glitches in Spotify's Top 200</font>

<h1 style="font-size:1.5vw">Michael Döringer</h1>

<h1 style="font-size:1.5vw">Cardamon Loops | Data Analytics | Spiced Academy</h1>

------------------

## <font color="#1DB954">Table of content</font>

- Intro: the data and the significance of Spotify's charts
- General ananlysis: popular music around the world
- Non-contemporary incidents: spotting old songs in the charts

------------------

## <font color="#1DB954">Data structure</font>

![5.212.985 rows x 13 columns](df_for_presentation.jpg)
<p></p> 

The 200 most streamed songs for 70 countries for each week since 2013 + the global numbers

- Artist name + song title
- Weekly plays
- Chart date
- Spotify track ID --> Release date

------------------

![The most popular songs worldwide](plots/song bubbles.svg)

------------------

![The most popular artists worldwide](plots/artist name cloud.svg)

------------------

![Favorite artist of each country](plots/artist world map.svg)

------------------


## <font color="#1DB954">Finding old songs</font>

- looking at the global charts for worldwide trends
- adding more data from Spotify Web API: release dates for each song
- filterting the data for release years before 2010

------------------

## <font color="#1DB954">Some statistics</font>

<p align="left">Global Charts 2013-2022:</p>

- <font color="#1DB954">86.295</font> entries
- <font color="#1DB954">5.984</font> unique songs
- songs from before 2010: <font color="#1DB954">188</font> unique songs
- relation: <font color="#1DB954">3.1 %</font>


------------------

![Old songs entering the weekly charts](plots/Weekly old songs entering charts.svg)

------------------

- 35 unique song titles contain the word „Christmas“: 2.6 % left

- 99 unique songs charting in December: 1.5 % left 

- the truth lies in between: only <font color="#1DB954">2.6-1.5%</font> of Spotify's Top 200 are older/non-contemporary/non-christmas songs

**<font color="#1DB954">Let's find out which songs these are and why they suddenly rise in global popularity!</font>**

------------------

## <font color="#1DB954">Old songs with 10+M streams</font>

<style scoped>
table {
  font-size: 25px;
}
</style>

| **Chart appearance** | **Artist/Song** | **Release year** |
|:----------------:|:-----------:|:------------:|
|       2017       |     ???     |     2000     |
|       2017       |     ???     |     2003     |
|       2019       |     ???     |     1975     |
|       2020       |     ???     |     1977     |
|       2022       |     ???     |     1985     |
|       2022       |     ???     |     1986     |
|       2022       |     ???     |     1991     |
|       2022       |     ???     |     1999     |
|       2022       |     ???     |     1995     |
...

------------------

![Kate Bush - Running Up That Hill](plots/Kate Bush/Dashboard - Kate Bush.svg)

------------------

Featured in "Stranger Things"

<iframe data-autoplay width="100%" height="600" src="https://www.youtube.com/embed/PXtOGS3E0vo"></iframe>

------------------

![Fleetwood Mac - Dreams](plots/Fleetwood Mac/Dashboard - Fleetwood Mac.svg)

------------------

Viral on TikTok

<iframe data-autoplay width="100%" height="600" src="https://www.youtube.com/embed/OtzVKUCZE5w">
</iframe>
</section>

------------------

![Linkin Park](plots/Linkin Park/Dashboard - Linkin Park.svg)

------------------

Singer died

<img src="plots/Linkin Park/linkin_park.jpg" alt="Chester Bennington">

------------------

![Dr. Dre, Eminem, Snoop Dogg... ](plots/Eminem + Dr. Dre/Dashboard - Eminem & Dr. Dre.svg)

------------------

Superbowl Halftime Show Performance

<iframe data-autoplay width="100%" height="600" src="https://www.youtube.com/embed/GTHUoETtpuc">
</iframe>

------------------

## <font color="#1DB954">Thank you for listening</font>

**Tech used:**
<p></p> 

- Python
- Pandas
- Plotly
- spotipy
- Tableau
- Pandoc
