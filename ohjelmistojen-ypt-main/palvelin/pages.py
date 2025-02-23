"""Page templates for the miniature HTTP server application."""


indexPage = \
"""
<!DOCTYPE html>
<html>
    <head>
        <title>Example mini app page</title>
    </head>
<body>

<h1>Mini application contents</h1>
<p>
    <ul>
        <li>
            <a href="/page1">Page 1 -> </a>
        </li>
        <li>
            <a href="/page2">Page 2 -> </a>
        </li>
        <li>
            <a href="/page3">Page 3 -> </a>
        </li>
    </ul>
</p>

</body>
</html>
"""

pageOne = \
"""
<!DOCTYPE html>
<html>
<head>
<title>Page One</title>
</head>
<body>

<h1>This is the page one.</h1>
<p>
    These are the page one contents.
</p>

<p>
    <a href="/">Back to the front page -> </a>
</p>

</body>
</html>
"""

pageTwo = \
"""
<!DOCTYPE html>
<html>
<head>
<title>Page Two</title>
</head>
<body>

<h1>This is the page two.</h1>
<p>
    These are the page two contents.
</p>

<p>
    <a href="/">Back to the front page -> </a>
</p>

</body>
</html>
"""

pageThree = \
"""
<!DOCTYPE html>
<html>
<head>
<title>Page Three</title>
</head>
<body>

<h1>This is the page three.</h1>
<p>
    These are the page three contents.
</p>

<p>
    <a href="/">Back to the front page -> </a>
</p>

</body>
</html>
"""
