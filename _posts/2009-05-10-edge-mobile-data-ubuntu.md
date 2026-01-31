---
layout: post
title: "ต่อเน็ตผ่าน EDGE ของ DTAC ด้วย Nokia 3110c บน Ubuntu Jaunty Jackalope"
date: 2009-05-10T13:40:44.000Z
permalink: /content/%E0%B8%95%E0%B9%88%E0%B8%AD%E0%B9%80%E0%B8%99%E0%B9%87%E0%B8%95%E0%B8%9C%E0%B9%88%E0%B8%B2%E0%B8%99-edge-%E0%B8%82%E0%B8%AD%E0%B8%87-dtac-%E0%B8%94%E0%B9%89%E0%B8%A7%E0%B8%A2-nokia-3110c-%E0%B8%9A%E0%B8%99-ubuntu-jaunty-jackalope
---

มันฟังดูเป็นส่วนผสมที่ไม่ค่อยมีใครมีนะ (DTAC+Nokia 3110 classic+Ubuntu Jaunty Jackalope) แต่เอาน่า เผื่อมันจะเป็นประโยชน์กับใครได้บ้าง อย่างที่ผมได้รับความช่วยเหลือมาแล้ว

เรื่องของเรื่องก็คือ ด้วยความเห่อมือถือใหม่ที่ใช้ EDGE/GPRS ได้ ก็เอามาต่อกับคอมพิวเต้อร์เพื่อเล่นอินเตอร์เน็ตบ้างเป็นครั้งคราว (ในกรณีที่ขี้เกียจลงจากห้องมาใช้เน็ตฟรีของมหาวิทยาลัย) ตอนที่ใช้ Ubuntu เวอร์ชั่น 8.10 Intrepid Ibex นั้น น่าประทับใจมาก คือเสียบมือถือปุ๊บ คลิกเลือก DTAC ใน Network Manager ก็ต่อได้เลย สองคลิกเท่านั้น! เทียบกับ Windows ที่ต้องลงโปรแกรม Nokia PC Suite แล้วเมพกว่าเห็น ๆ

ปัญหาก็คือ หลังจากอัพเกรดเวอร์ชั่นของ Ubuntu จาก 8.10 เป็น 9.04 Jaunty Jackalope แล้วเนี่ย มันต่ออินเตอร์เน็ตอีกไม่ได้ โดยปัญหาเหมือนว่าจะเป็นการถอดชื่อเว็บไซ้ท์ออกเป็นหมายเลข IP ไม่ได้ (มันจะขึ้น looking for xxx.com ในแถบด้านล่างของ Firefox อยู่นาน) เลย[ถามใน Twitter](http://twitter.com/tewson/status/1754256552) ได้ [@phisite](http://twitter.com/phisite) กับ [@wiennat](http://twitter.com/wiennat) มาช่วยตอบว่า ให้ไปเอาค่า DNS เก่าออก (คลิกขวาที่ Network Manager Panel -> Edit Connections -> Mobile Broadband -> DTAC -> Edit -> IPv4 Settings -> เลือก Method เป็น Automatic (PPP)) เท่านั้นก็เรียบร้อย

สำหรับสาเหตุนั้นเดาว่าเมื่อเร็ว ๆ นี้ DTAC เพิ่งเปลี่ยน DNS แล้ว Jackalope มันจำค่า DNS เดิมจาก Ibex มา

ขอขอบคุณ [@phisite](http://twitter.com/phisite) และ [@wiennat](http://twitter.com/wiennat) (เรียงตามตัวอักษร)
