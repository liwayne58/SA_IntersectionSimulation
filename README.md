<!-- video -->
<p align="center">
  <video src="__assets__/Demo.mp4" controls></video>
</p>

<!-- tag line -->
<h1 align='center'>動態交通訊號控制系統</h1>

<!-- primary badges -------------------------------------->
<p align="center">
  <img src='https://img.shields.io/badge/license-MIT-blue.svg' />
  <img src='https://img.shields.io/badge/Python-3.x-blue' />
  <img src='https://img.shields.io/badge/Pygame-2.x-green' />
  <img src='https://img.shields.io/badge/WebSocket-Server-yellow' />
</p>

<p align="center">
    <a href="__assets__/README-EN.md">English Version</a>
</p>

## 專案介紹
此專案是「動態交通信號控制系統」的路口模擬子系統，

作為雲林科技大學「系統分析與設計」課程的專題作品，

本模擬器使用 Pygame 建立虛擬路口環境，透過 WebSocket 與 Java 核心進行即時通訊。

專案旨在解決現有交通訊號控制系統的限制，開發一個更智慧的動態交通控制解決方案。

> [!NOTE]
> 對 Java 核心感興趣請到 [此專案](https://github.com/liwayne58/SA_DynamicSmartTrfficSignalCS) ! <br>
> 對系統分析與設計文件感興趣請到 [文件](/__assets__/Documents/)

### 背景
- 目前多數交通信號系統使用固定計時器
- 無法適應即時交通流量變化
- 導致交通堵塞、延誤與環境污染問題

### 解決方案
本系統採用創新的方法：
- 基於電腦視覺的動態交通控制器
- 利用 CCTV 或政府資料庫影像計算交通密度
- 即時檢測車輛數量與類型（轎車、機車、救護車等）
- 動態調整綠燈時間
- 優先處理緊急車輛與擁堵方向

> [!Important]
> 由於需要展示專案, 所以選擇透過 Pygame 模擬交通道路阻塞, 並且直接由 Python 傳送道路車流數據至 Java 核心


## 功能列表
1. 交通模擬
   - 使用 Pygame 模擬道路交通流量
   - 支援多種車輛類型
   - 即時交通號誌狀態顯示

2. 即時通訊
   - WebSocket 伺服器
   - 與 Java 核心實時數據交換

3. 模擬控制
   - 多車道管理
   - 車輛生成控制
   - 交通號誌時序控制
   - 車流統計分析

## 安裝指南

### 環境要求
- Python 3.x
- Pygame
- webSocket-server

### 安裝步驟
1. 克隆專案
```bash
git clone https://github.com/liwayne58/SA_IntersectionSimulation.git
```

2. 安裝依賴套件
```bash
pip install -r requirements.txt
```

3. 啟動模擬器
```bash
python main.py
```

### 配置說明
- WebSocket 預設連接位址：127.0.0.1:5587
- 可在 `Model/WebSocket.py` 中修改連接設定

## 系統架構
- 前端：Python Pygame 模擬界面
- 通訊：WebSocket 服務
- 後端：Java 服務器
- 算法：權重計算系統

## License
本專案採用 MIT License 授權。

## 原始專案
本專案基於 [Basic-Traffic-Intersection-Simulation](https://github.com/mihir-m-gandhi/Basic-Traffic-Intersection-Simulation) By [Mihir Gandhi](https://github.com/mihir-m-gandhi) 進行修改與擴展，原始專案採用 MIT License。

同時也可以參考此 [影片資訊](https://www.youtube.com/watch?v=ZzKuR2kSqM4)

## 聯絡方式
- Email: wayneli058@gmail.com