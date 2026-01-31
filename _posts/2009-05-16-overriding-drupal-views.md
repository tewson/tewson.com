---
layout: post
title: "Overriding Drupal Views with .tpl.php Files"
date: 2009-05-16T21:11:15.000Z
permalink: /content/overriding-drupal-views-tplphp-files
---

After being away from customising Drupal for a while, I have forgotten in some details about how to override (or customise) Views using my own .tpl.php files.

In my opinion, overriding Views this way is very comfortable because you just put a template file with a specific name in the theme's directory and let Drupal scan for this new template and that's it!

Beforehand, you need to know that specific name of your .tpl.php file. You have to take a look at "Theme: Information" in "Basic Settings" in the View edit page. Decide which kind of overriding you need here. The file names are ordered by level of specification.

You will find a button labeled "Rescan template files" here. You will need to activate your newly-created template file(s) here again in the future.

Then you can create your own .tpl.php file(s) now. You may wonder how your template file will look like. This is also where I got stuck - and got motivation to write this entry :)

The clue is that you can find all the default Views in the Views module's directory itself. In my case it's /sites/all/modules/views/theme. Copy what you need and enjoy theming :D
