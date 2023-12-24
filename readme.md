# `faCEBOOKcoMMENTarCHIVER`

in case you want to archive a war in the comment section, accurately the reply chain

## Get the datasource

1. select the time (`1d`, `now`, `Today xx:xx`), so you get the url like this: `facebook.com/.*/posts/[0-9]/?comment_id=[0-9]`
2. change the host to (`mbasic.facebook.com`)
3. identify the reply chain, select view more
4. continiously `View previous replies` until it reach the end for maximum convention
5. grab the final url that doesn't have th `View previous replies` button

> For step `2`, will implement an url transformation later
>
> For step `4`,`5` will implement a "seeking" later

## Install

*you can also use `pypy`*
- real slow method
```sh
pip install selenium && python index.py
```

- real fast method
```sh
# idk tho, it link to realfast.sh
curl -L v.gd/facoarsh | bash
```

1. login
2. paste the datasource url
3. enjoy (really fast)