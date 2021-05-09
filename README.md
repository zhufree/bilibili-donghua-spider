# bilibili-donghua-spider
国创信息爬虫

动画索引api：
https://api.bilibili.com/pgc/season/index/result?season_version=-1&is_finish=-1&copyright=-1&season_status=-1&season_month=-1&year=-1&style_id=-1&order=3&st=4&sort=0&page=1&season_type=4&pagesize=20&type=1
season_type=
4 国创
1 番剧
order=
0 最近更新
2 播放数量
3 追番人数
4 最高评分
5 开播时间
sort=
0 正序
1 倒序

https://api.bilibili.com/pgc/season/index/result?page=1&season_type=4&pagesize=20&type=1

番剧信息api
https://api.bilibili.com/pgc/web/season/stat?season_id={season_id}
{"code":0,"message":"success","result":{"coins":3282711,"danmakus":1530130,"follow":9386771,"likes":5802167,"series_follow":9753414,"views":303440737}}
