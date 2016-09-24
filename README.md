# blog
My personal blog https://haissamkaj.com

## Description

This blog is powered by [Pelican](http://blog.getpelican.com/). The content is intended to be served by Nginx.

## Deploy steps
- clone this repository in `/var/www/`, change rights as needed
- replace the content of `img` with your own profile and favicon
- adapt constants in `pelicanconf.py` and `publishconf.py`
- `pip install -r requirements.txt`
- run `cd /var/www/blog && make init` to pull Pelican themes
- generate the website with `cd /var/www/blog && pelican content` (the resulting pages will be in `output`)
- configure nginx (nginx.conf is commented and provided as an example)
- restart nginx
- profit

## TODO:
- enable analytics
