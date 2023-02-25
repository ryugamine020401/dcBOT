# 環境建置
* 安裝pipenv
```bash
pip install pipenv
```
* 進入虛擬環境
```bash
pipenv shell
```
* 安裝相關套件
```bash
pipenv install
```

# Setting.json設置
必須在與bot.py同一個目錄下建立一個 `Setting.json` 檔案，以以下方式建立。
- 兩個不同屬性要以逗點隔開，頻道id是`int`。

```json
{
  "TOCKEN" : "",
  "PATH" : "",
  "Timer_channel_ID" : 

}
```





