html = b"""
<html>
    <body>
        <form action="">
            x = <input type="number" name="a">
            y = <input type="number" name="b"><br><br>
            <input type="submit">
        </form>
        <p>
            x + y = %(add)d</br>
            x * y = %(mul)d</br>
            %(msg)s</br>
        <p/>
    </body>
</html>
"""
