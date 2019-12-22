from pelican.plugins.timegraphics import embed_url


def test_embed_url():
    url = embed_url(123466)
    assert url == "https://time.graphics/embed?v=1&id=123466"
