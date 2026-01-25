---
layout: post
title: "Python Qt MySQL และภาษาไทย"
date: 2009-03-30T10:08:56.000Z
permalink: /content/python-qt-mysql-%E0%B9%81%E0%B8%A5%E0%B8%B0%E0%B8%A0%E0%B8%B2%E0%B8%A9%E0%B8%B2%E0%B9%84%E0%B8%97%E0%B8%A2
---

วันนี้เขียนโปรแกรมโดยใช้ PyQt แล้วติดปัญหาว่าใส่ข้อมูลภาษาไทยลงฐานข้อมูลไม่ได้ โดยฐานข้อมูลใช้ charset เป็น UTF-8

วิธีก็คือ ตอนเชื่อมต่อฐานข้อมูลให้ระบุไปด้วยว่าจะเชื่อมต่อแบบไหน

```
conn = MySQLdb.connect (
  host = "localhost",
  user = "user",
  passwd = "pass",
  db = "db",
  use_unicode=True,
  charset='utf8')
```

ต่อมา เนื่องจากเขียนอยู่บน PyQt พอจะเอาข้อความไปใส่ฐานข้อมูล ก็ต้องแปลงจาก QString เป็น String ธรรมดาก่อน ซึ่งจะใช้ฟังก์ชั่น str() เฉย ๆ ไม่ได้ เพราะมันเป็นภาษาไทย เลยต้องใช้ unicode() แทน

ขอขอบคุณ [http://www.narisa.com/forums/index.php?showtopic=15869](http://www.narisa.com/forums/index.php?showtopic=15869)