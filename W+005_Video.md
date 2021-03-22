# W+005: Download Douyin Videos

1. Open Douyin link in a browser:

- https://v.douyin.com/eLeFbwF/

The page is redirected to another address:

- https://www.iesdouyin.com/share/video/6940213957147905314/?region=MY&mid=6783385252397058055&u_code=37k23caifjfk&titleType=title&did=792071704423691&iid=4328111372767279&utm_source=copy_link&utm_campaign=client_share&utm_medium=android&app=aweme&scheme_type=1

2. Using Right-Click Inspect element to obtain actual address of video:

- http://v3-dy-o.zjcdn.com/248befda77b51d4cb357a68e66a30e02/6058836d/video/tos/cn/tos-cn-ve-15/388823b236fe4cf3b69bcacfd2236fca/?a=1128&br=4280&bt=1070&btag=4&cd=0%7C0%7C1&ch=0&cr=0&cs=0&cv=1&dr=0&ds=3&er=&l=202103221845380101981130403B0038E3&lr=aweme_search_suffix&mime_type=video_mp4&net=0&pl=0&qs=0&rc=anBmZzl4NnU8NDMzZmkzM0ApZmk1OGlpPGVlNzhlNzY2NGcpaGRqbGRoaGRmaG5uX2NoaWI1YC0tYy0vc3M1Yl9jNi5iYC80LzMxYTZhOmNwb2wrbStqdDo%3D&vl=&vr=

<img src="https://github.com/udexon/Webpp/blob/main/img/Douyin01.png" width=600>

Download video using `wget` or similar utilities:

```sh
$ wget 'http://v3-dy-o.zjcdn.com/248befda77b51d4cb357a68e66a30e02/6058836d/video/tos/cn/tos-cn-ve-15/388823b236fe4cf3b69bcacfd2236fca/?a=1128&br=4280&bt=1070&btag=4&cd=0%7C0%7C1&ch=0&cr=0&cs=0&cv=1&dr=0&ds=3&er=&l=202103221845380101981130403B0038E3&lr=aweme_search_suffix&mime_type=video_mp4&net=0&pl=0&qs=0&rc=anBmZzl4NnU8NDMzZmkzM0ApZmk1OGlpPGVlNzhlNzY2NGcpaGRqbGRoaGRmaG5uX2NoaWI1YC0tYy0vc3M1Yl9jNi5iYC80LzMxYTZhOmNwb2wrbStqdDo%3D&vl=&vr=' 
```
