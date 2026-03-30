---
layout: post
title: "NS_ERROR_DOM_SECURITY_ERR in using canvas tag"
date: 2009-09-03T10:03:57.000Z
permalink: /content/nserrordomsecurityerr-using-canvas-tag
---

I've found an incredible image processing library for JavaScript called "[Pixastic](https://web.archive.org/web/20090918072035/http://www.pixastic.com/)". Of course I downloaded the code and tried it as a single HTML file in Firefox 3.5. Then, I just got the error NS_ERROR_DOM_SECURITY_ERR, which is an error thrown when you try to change some DOM information that is from another domain. So what's the problem while the image itself is exactly in the same place as the script?

Google just took me to [http://www.nihilogic.dk](https://web.archive.org/web/20101016125359/http://blog.nihilogic.dk/), which is eventually a blog of the author of Pixastic. There are some comments in there mentioning my problem. The solution is that: you need to put the script and you "hello world" page for the script in a server. Therefore, Firefox won't complain about the security thing. I copied the codes to my localhost and it just works!

I would like to thank [Jacob Seidelin](https://web.archive.org/web/20090918232340/http://blog.nihilogic.dk/2000/01/about.html) for creating this great tool.
