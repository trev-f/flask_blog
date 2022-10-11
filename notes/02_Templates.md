# 02 - Templates

[Python Flask Tutorial: Full-Featured Web App Part 2 - Templates](https://www.youtube.com/watch?v=QnDWIZuWYW0&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&index=2)

## Serve static html page

To serve a static html page, simply put it in the `templates` directory and render it with `render_template()`:

```python
@app.route("/static_page")
def static_page():
    return render_template("static_page.html")
```