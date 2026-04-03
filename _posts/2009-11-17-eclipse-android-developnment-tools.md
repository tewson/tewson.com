---
layout: post
title: "org.eclipse.gef 0.0.0 required for installing Android Development Tools on Eclipse 3.5.1"
date: 2009-11-17T10:45:14.000Z
permalink: /content/orgeclipsegef-000-required-installing-android-development-tools-eclipse-351
---

Today I wanted to try the Android SDK on my Ubuntu Karmic Koala, so I followed the instructions in the following URL.

[http://developer.android.com/sdk/index.html](http://developer.android.com/sdk/index.html)

I thought that an IDE would be useful so I installed Eclipse 3.5.1 and tried to install the Android Development Tools, or ADT. However, an error "org.eclipse.gef 0.0.0 required" (or something like that) appeared.

After googling for a while, I found a URL for the GEF SDK, which is Eclipse's Graphic Editing Framework, as the following URL.

[http://download.eclipse.org/tools/gef/updates/releases/](http://download.eclipse.org/tools/gef/updates/releases/)

So I added this update into Eclipse by

1. Go to the menu 'Help',
2. Choose 'Install New Software',
3. Place the GEF SDK updates URL into the box after 'Work with:',
4. Choose the right version of updates in the box below (for me, GEF SDK 3.5.1),
5. Click 'Next',
6. After Eclipse calculates all the dependencies, just click 'Finish' and let it install the plugin.

After installing GEF SDK, return to installation of ADT. You should be able to install it now.
