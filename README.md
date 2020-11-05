# Selenium-Python
Implement selenium in python for web crawling.

## Setup

Download the repo, then

```
pip install -r requirements.txt
```

## Demonstration

### 1. App finder
Find app which comment count over 1000.

```
python app_finder.py
```

### 2. Using Selenium with docker-compose
Deploy the program using docker-compose.

```
docker build -t selenium-python . --no-cache
```

```
docker-compose up --build -d
```

then check the log(`docker-compose logs -f --tail 100 crawler`), you can see
```
crawler_1  | DEBUG [11-05 09:18:45] [example.py: line 29] news: 直擊醫病痛點！「Right Time」App 為民眾掛號、候診省下 60 分鐘時間
crawler_1  | DEBUG [11-05 09:18:45] [example.py: line 29] news: 科學家發現新細胞有望治神經損傷！《Nature》子刊：可讓中樞神經再生
crawler_1  | DEBUG [11-05 09:18:45] [example.py: line 29] news: 反覆流產、不易受孕該怎麼辦？PRP療法有助改善子宮內膜環境
crawler_1  | DEBUG [11-05 09:18:45] [example.py: line 29] news: 人體再生肝臟有望！匹茲堡醫學院從「淋巴結」中再生健康肝臟
crawler_1  | DEBUG [11-05 09:18:45] [example.py: line 29] news: 這種療法安全嗎？為什麼治療費用會這麼高？一次解答細胞療法2大常見問題
```
something like this.
