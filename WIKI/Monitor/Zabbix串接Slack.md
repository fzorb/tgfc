# Zabbix 串接 slack 教學

此教學適用於 Slack Webhook (版本6)，Zabbix 內建 slack webhook 串接方式。
以下用 gb-outsite-zabbix 示範:

## 第一步 - slack api 設定
創立新的 app 應用

名稱取名對應的 zabbix，工作區塊選擇 TGFC

至 Basic Information，點選 Bots

點選 Review Scopes to Add

往下滑，滑到 Scopes，在 Add permision by Scope 地方選擇 `"chat:write"`

滑回最上面，點選 Install to Workspace

最後會產出一組 Token，複製起來等等會用到

回到 Slack 應用程式，創立頻道

邀請成員進入該頻道 /invite @app 應用名稱

## 第二步 - Zabbix 設定
至 報警媒介類型，點選 Slack

確認類型為 Webhook，bot_token 設為 `{$SLACKTOKEN}`

`{$SLACKTOKEN}` 設置剛剛複製的 Token，`{$ZABBIX.URL}` 設置 zabbix 網址

至 用戶，創建 報警媒介，收件人填寫要發送到的slack頻道名子 (要帶#)

至 動作 -> Trigger Actions，創建動作

在 動作 地方，計算方式選擇 `或`，並添加條件將所有群組加進去

到 操作 地方，將 `操作` `恢復操作` `更新操作`，都添加上發送設定

最後確認發送是否成功

> 該範例特殊步驟:
> 若有防火牆機制，zabbix搓slack 需要過防火牆，需請相關人員協助於防火牆添加 `hook.slack` url，否則會被阻擋而發送不到slack。
{.is-warning}
