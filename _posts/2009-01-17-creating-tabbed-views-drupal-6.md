---
layout: post
title: "Creating Tabbed Views in Drupal 6"
date: 2009-01-17T17:58:00.000Z
permalink: /content/creating-tabbed-views-drupal-6
---

As a Drupal newbie, I am always confused with its simple mechanisms, such as routing and menus. I just spent about an hour figuring out how to create a view with tabs that lead to more specific lists of data, for example, in 'document' page there are three tabs, one is 'all' which is the default display listing all contents, one is 'homework' leading to a path 'document/homework', and the last one is 'report' leading to 'document/report'.

'document' page
- tab 'all' -> 'document/all'
- tab 'homework' -> 'document/homework'
- tab 'report' -> 'document/report'

After 30 minutes of googling, I found this (and yelled 'Eureka'), <a href="http://drupal.org/node/87195">Tutorial #3: Create two tabs to sort taxonomy view alphabetically and by created time</a>. The method is quite simple but Drupal gave me no clues or I made a poor search (or I was so n00b that I didn't know these things before).

Well, the way is:

<ol>
<li>Create a view.</li>
<li>Name the path (url) to be what you want the default tab to be, for example, 'document/all'.</li>
<li>Configure your view with sorting, filtering, etc.</li>
<li>Choose 'Default menu tab' in Menu option and name it.</li>
<li>Choose 'Normal menu item' to be the parent, since this tab is linked directly from a menu, i.e. 'document'</li>
<li>Finish this first tab.</li>
<li>Create another display.</li>
<li>Name the path of this one as a tab option, like 'document/homework'.</li>
<li>Configure it.</li>
<li>Choose 'Menu tab' for this one.</li>
<li>Finish this tab.</li>
<li>Repeat (8) - (11) for more tabs.</li>
</ol>

That's it. Simple, huh?
Please leave a comment if there's any mistake above.
